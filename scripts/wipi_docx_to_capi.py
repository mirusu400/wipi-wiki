"""Regenerate WIPI C API Markdown from PDF→docx chunks.

The PDF was converted to docx in 99-page chunks. Code samples in the original
PDF became <w:txbxContent> (textbox) blocks inside the docx. A naïve body
iteration misses textbox paragraphs, which is why the existing extract dropped
line breaks inside C code blocks. This script:

  1. Walks ALL <w:p> elements in document order (including textbox-nested
     paragraphs and table cells), across multiple docx files in sequence.
  2. Identifies "5.1.X." section markers and routes everything between them
     to the matching output file.
  3. Classifies each paragraph as heading / code / body / bullet using:
       - paragraph style (3/4/5/6 = Heading 1-4)
       - font (Courier New / 새굴림 / monospace-like → code)
       - leading bullet markers (■, ●, ?, etc.)
       - bold + large size = heading.
  4. Coalesces consecutive code paragraphs into a single fenced ```c block.

Usage:
    python scripts/wipi_docx_to_capi.py docs/c-api vendor/wipi_pdf_chunks/WIPI*part0[2-6]*.docx
"""
from __future__ import annotations
import os, re, sys, zipfile, glob
from xml.etree import ElementTree as ET

NS = {
    'w':   'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r':   'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}
W = NS['w']
W_T = '{%s}t' % W
W_TAB = '{%s}tab' % W
W_BR = '{%s}br' % W

# Section configuration registry, keyed by mode name.
# Each entry: (section_num → out filename, section_num → display title,
#              ordered list of section numbers, sentinel that stops emission).
SECTION_CONFIGS = {
    'capi': {
        'file': {
            '5.1.1':  'kernel.md',     '5.1.2':  'graphics.md',
            '5.1.3':  'database.md',   '5.1.4':  'filesystem.md',
            '5.1.5':  'network.md',    '5.1.6':  'media.md',
            '5.1.7':  'serial.md',     '5.1.8':  'phone.md',
            '5.1.9':  'misc.md',       '5.1.10': 'utility.md',
            '5.1.11': 'ui-components.md', '5.1.12': 'c-stdlib.md',
        },
        'title': {
            '5.1.1':  '커널',     '5.1.2':  '그래픽',
            '5.1.3':  '데이터베이스', '5.1.4':  '파일시스템',
            '5.1.5':  'NETWORK',  '5.1.6':  '매체 처리기',
            '5.1.7':  'SERIAL',   '5.1.8':  'PHONE',
            '5.1.9':  'MISC',     '5.1.10': 'UTILITY',
            '5.1.11': '사용자 인터페이스 컴포넌트', '5.1.12': '표준 C 라이브러리',
        },
        # Sentinels that close current section without opening a new one.
        'stop_pattern': re.compile(r'^5\.2(\.|$|\s)'),
        'stop_titles': {'자바 API', '자바  API'},
    },
    'hal': {
        'file': {
            '4.1': 'types.md',   '4.2': 'platform-api.md',
            '4.3': 'system.md',  '4.4': 'call.md',
            '4.5': 'handset.md', '4.6': 'network.md',
            '4.7': 'serial.md',  '4.8': 'media.md',
            '4.9': 'time.md',    '4.10': 'utility.md',
            '4.11': 'file.md',   '4.12': 'input-method.md',
            '4.13': 'font.md',   '4.14': 'frame-buffer.md',
            '4.15': 'virtual-key.md',
        },
        'title': {
            '4.1': 'TYPE DEFINITION', '4.2': '플랫폼이 제공하는 API',
            '4.3': 'System',          '4.4': 'CALL',
            '4.5': 'HandSet Device',  '4.6': '네트워크',
            '4.7': 'Serial',          '4.8': 'MEDIA',
            '4.9': 'TIME',            '4.10': 'UTILITY',
            '4.11': 'FILE',           '4.12': 'InputMethod',
            '4.13': 'Font',           '4.14': 'Frame Buffer',
            '4.15': 'Virtual Key',
        },
        # Stop when we hit "C API" (section 5 umbrella) or 5.1.X.
        'stop_pattern': re.compile(r'^5(\.\d+)*(\.|$|\s)'),
        'stop_titles': {'C API', 'C  API'},
    },
}

# Mutable globals selected per run (set by main()).
SECTION_FILE: dict = {}
SECTION_TITLE: dict = {}
SECTION_ORDER: list = []
TITLE_TO_NUM: dict = {}
STOP_PATTERN = None
STOP_TITLES: set = set()

# Subsection labels that should render bold (under each API entry).
API_LABELS = {
    '프로토타입', '설명', '매개 변수', '매개변수',
    '반환 값', '반환값', '리턴 값', '리턴값',
    '부작용', '참고 항목', '비고', '예제', '에러', '에러 코드',
}
LABEL_NORMALIZE = {
    '매개변수': '매개 변수',
    '반환값':   '반환 값',
    '리턴 값':  '반환 값',
    '리턴값':   '반환 값',
}

CODE_FONTS = {'Courier New', '새굴림', 'NewGulim', 'Consolas', 'Monospace'}

# Lines that look like C code (no detection from font needed).
C_LINE_RE = re.compile(
    r'^(typedef|#define|#include|extern|struct|union|enum|inline|static|const|'
    r'void|int|char|float|double|long|short|unsigned|signed|return|if|else|'
    r'for|while|switch|case|break|continue|do|goto|M_\w+|MC_\w+|MH_\w+)\b'
)
HANGUL_RE = re.compile(r'[가-힣]')


def looks_like_code(text):
    """Heuristic: paragraph that has C syntax and minimal Korean."""
    s = text.strip()
    if not s:
        return False
    korean = len(HANGUL_RE.findall(s))
    if korean > 0 and korean / max(len(s), 1) > 0.15:
        return False  # mostly Korean
    if C_LINE_RE.match(s):
        return True
    # } / { only lines, or single-statement-like
    if re.match(r'^[{}\[\];]+$', s):
        return True
    return False

NOISE_LINES = {
    '모바일 표준 플랫폼 규격 V1.2',
    '무선 인터넷 표준화 포럼',
    '모바일 표준 플랫폼 규격 V1.2.1',
    '무선인터넷 표준화 포럼',
}

SECTION_RE = re.compile(r'^(\d+\.\d+\.\d+(?:\.\d+)*)\.?\s*(.*)$')
PAGENUM_RE = re.compile(r'^\d{1,4}$')


# ---------- low-level docx walkers ----------

def run_text(r):
    parts = []
    for child in r:
        tag = child.tag
        if tag == W_T:
            parts.append(child.text or '')
        elif tag == W_TAB:
            parts.append('\t')
        elif tag == W_BR:
            parts.append('\n')
    return ''.join(parts)


def run_font(r):
    rPr = r.find('w:rPr', NS)
    if rPr is None:
        return None
    rFonts = rPr.find('w:rFonts', NS)
    if rFonts is None:
        return None
    for attr in ('{%s}ascii' % W, '{%s}hAnsi' % W, '{%s}cs' % W, '{%s}eastAsia' % W):
        v = rFonts.get(attr)
        if v:
            return v
    return None


def run_is_bold(r):
    rPr = r.find('w:rPr', NS)
    if rPr is None:
        return False
    b = rPr.find('w:b', NS)
    return b is not None and b.get('{%s}val' % W) not in ('false', '0')


def run_size(r):
    rPr = r.find('w:rPr', NS)
    if rPr is None:
        return None
    sz = rPr.find('w:sz', NS)
    if sz is None:
        return None
    try:
        return int(sz.get('{%s}val' % W))
    except (TypeError, ValueError):
        return None


def para_style(p):
    pPr = p.find('w:pPr', NS)
    if pPr is None:
        return None
    pStyle = pPr.find('w:pStyle', NS)
    if pStyle is None:
        return None
    return pStyle.get('{%s}val' % W)


def para_text(p):
    out = []
    for r in p.findall('w:r', NS):
        out.append(run_text(r))
    return ''.join(out)


def para_runs(p):
    return p.findall('w:r', NS)


def para_is_code(p):
    """True if any significant run uses a code font."""
    runs = [r for r in para_runs(p)
            if any((t.text or '').strip() for t in r.findall('w:t', NS))]
    if not runs:
        return False
    code_runs = sum(1 for r in runs if run_font(r) in CODE_FONTS)
    return code_runs >= len(runs) * 0.5  # majority by run count


def para_is_heading_bold(p):
    """Big bold paragraph (sz >= 28 in halfpoints, i.e. 14pt+) with no code font."""
    runs = [r for r in para_runs(p)
            if any((t.text or '').strip() for t in r.findall('w:t', NS))]
    if not runs:
        return False
    if any(run_font(r) in CODE_FONTS for r in runs):
        return False
    if not all(run_is_bold(r) for r in runs):
        return False
    szs = [run_size(r) for r in runs if run_size(r)]
    if not szs:
        return False
    return max(szs) >= 28


def walk_paragraphs(body):
    """Yield (paragraph element, container_kind) for every <w:p> in document
    order, including paragraphs nested inside textboxes (w:txbxContent) and
    table cells. container_kind ∈ {'body', 'textbox', 'table'} on the deepest
    container (heuristic – we use the *closest* nesting ancestor)."""
    # Just iterate all w:p in doc order; tag the kind by inspecting ancestors.
    # ET doesn't store parent pointers, so build one.
    parents = {c: p for p in body.iter() for c in p}
    for p in body.iter('{%s}p' % W):
        kind = 'body'
        cur = p
        while cur in parents:
            tag = parents[cur].tag.split('}')[1]
            if tag == 'txbxContent':
                kind = 'textbox'
                break
            if tag == 'tc':
                kind = 'table'
                break
            cur = parents[cur]
        yield p, kind


# ---------- emit logic ----------

class SectionEmitter:
    def __init__(self):
        self.buffers: dict[str, list[str]] = {k: [] for k in SECTION_FILE}
        self.current: str | None = None
        self.opened: set[str] = set()
        self.code_open = False  # currently inside a ```c fence
        self._last_emit_was_blank = True
        # When entered after 프로토타입 / 예제, the next paragraphs are code
        # until we see another known label.
        self.force_code_mode = False
        self.current_label: str | None = None

    def _buf(self):
        return self.buffers.get(self.current)

    def _close_code(self):
        if self.code_open:
            buf = self._buf()
            if buf is not None:
                buf.append('```')
            self.code_open = False
            self._last_emit_was_blank = False

    def _ensure_blank(self):
        b = self._buf()
        if b and b[-1].strip():
            b.append('')

    def open_section(self, num):
        if num not in SECTION_FILE:
            return
        self._close_code()
        self.current = num
        self.opened.add(num)
        title = SECTION_TITLE.get(num, '')
        self._buf().clear()
        self._buf().append(f'# {num}. {title}')
        self._buf().append('')
        self._last_emit_was_blank = True

    def emit_heading(self, level, text):
        if not self.current:
            return
        self._close_code()
        self._ensure_blank()
        text = re.sub(r'\s+', ' ', text.strip())
        b = self._buf()
        b.append('#' * level + ' ' + text)
        b.append('')
        self.force_code_mode = False

    def emit_label(self, label):
        if not self.current:
            return
        self._close_code()
        self._ensure_blank()
        self._buf().append(f'**{label}**')
        self._buf().append('')
        # Next paragraphs after 프로토타입/예제 are code by default.
        self.force_code_mode = label in ('프로토타입', '예제')
        self.current_label = label

    def emit_code_line(self, line):
        if not self.current:
            return
        if not self.code_open:
            self._ensure_blank()
            self._buf().append('```c')
            self.code_open = True
        self._buf().append(line)

    def emit_body(self, text):
        if not self.current:
            return
        self._close_code()
        self.force_code_mode = False
        # In 매개 변수 section, format "param - desc" lines as bullet items.
        if self.current_label == '매개 변수':
            m = re.match(r'^([A-Za-z_]\w*)\s*[-–]\s*(.+)$', text.strip())
            if m:
                self._buf().append(f'- `{m.group(1)}` — {m.group(2)}')
                return
        text = text.strip()
        if not text:
            return
        b = self._buf()
        if b and b[-1].strip():
            # join continuation lines into existing paragraph? No, treat
            # each docx para as its own MD para. Just add blank separator.
            b.append('')
        b.append(text)

    def emit_bullet(self, text):
        if not self.current:
            return
        self._close_code()
        text = text.strip()
        if not text:
            return
        self._buf().append('- ' + text)

    def finalize(self, out_dir):
        self._close_code()
        for num, fname in SECTION_FILE.items():
            path = os.path.join(out_dir, fname)
            buf = self.buffers[num]
            if not buf:
                continue
            # collapse multi-blank lines
            collapsed = []
            blank = 0
            for line in buf:
                if not line.strip():
                    blank += 1
                    if blank <= 1:
                        collapsed.append('')
                else:
                    blank = 0
                    collapsed.append(line)
            content = '\n'.join(collapsed).rstrip() + '\n'
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'wrote {path}: {len(content)} bytes, {len(buf)} lines')


# ---------- main pipeline ----------

def process_docx(docx_path, emitter):
    z = zipfile.ZipFile(docx_path)
    with z.open('word/document.xml') as f:
        tree = ET.parse(f)
    body = tree.getroot().find('w:body', NS)

    # Symbol-font private-use code points that PDF→docx emits as bullet
    # markers (rendered as ● or ◆ in the original PDF).
    bullet_chars = ''

    for p, kind in walk_paragraphs(body):
        txt = para_text(p)
        # Strip leading symbol-font bullets so heading patterns can match.
        txt = txt.lstrip(bullet_chars + ' \t')
        # Re-strip in case interior trailing whitespace
        txt = txt.strip()
        if not txt:
            continue
        if txt in NOISE_LINES:
            continue
        if PAGENUM_RE.match(txt):
            continue

        style = para_style(p)

        # Stop sentinel.
        if STOP_PATTERN.match(txt) or txt.strip() in STOP_TITLES:
            emitter._close_code()
            emitter.current = None
            continue

        # Section start? "N.X.Y. Title"
        m = SECTION_RE.match(txt)
        if m:
            num = m.group(1)
            if num in SECTION_FILE:
                emitter.open_section(num)
                continue

        # Section start by bare title in a heading style (docx dropped numbering).
        # HAL uses style "4" (Heading 2), C API uses style "3" (Heading 1).
        if style in ('3', '4'):
            num = TITLE_TO_NUM.get(txt)
            if num and num not in emitter.opened:
                emitter.open_section(num)
                continue

        if not emitter.current:
            continue

        # Code paragraph (font-based)
        if para_is_code(p):
            # Preserve internal line breaks if any
            for ln in txt.split('\n'):
                emitter.emit_code_line(ln)
            continue

        # Textbox paragraphs are usually code samples even without code font
        if kind == 'textbox':
            # Heuristic: if the line has mostly ASCII / few Korean chars and
            # contains C-ish punctuation, treat as code.
            korean = len(re.findall(r'[가-힣]', txt))
            ascii_punct = len(re.findall(r'[(){};=]', txt))
            if korean < len(txt) * 0.4 or ascii_punct >= 1:
                for ln in txt.split('\n'):
                    emitter.emit_code_line(ln)
                continue

        # API entry labels (프로토타입 / 설명 / ...)
        if txt in API_LABELS or txt in LABEL_NORMALIZE:
            emitter.emit_label(LABEL_NORMALIZE.get(txt, txt))
            continue

        # In forced code mode (after 프로토타입/예제), emit as code.
        if emitter.force_code_mode:
            for ln in txt.split('\n'):
                emitter.emit_code_line(ln)
            continue

        # Auto-detect C-ish lines (typedef, #define, struct, etc.).
        if looks_like_code(txt):
            for ln in txt.split('\n'):
                emitter.emit_code_line(ln)
            continue

        # Heading by style 3/4/5/6
        if style in ('3', '4', '5', '6'):
            level = {'3': 2, '4': 3, '5': 3, '6': 4}[style]
            # "API_NAME 설명" → split into heading + 설명 label
            mh = re.match(r'^(\S+)\s+(설명|프로토타입|매개\s*변수|반환\s*값|부작용|참고\s*항목|예제)\s*$', txt)
            if mh:
                emitter.emit_heading(level, mh.group(1))
                lbl = re.sub(r'\s+', ' ', mh.group(2))
                emitter.emit_label(LABEL_NORMALIZE.get(lbl, lbl))
            else:
                emitter.emit_heading(level, txt)
            continue

        # Bullet markers
        if txt.startswith(('■ ', '● ', '◆ ', '• ', '- ')):
            emitter.emit_bullet(txt.lstrip('■●◆•- ').strip())
            continue
        if txt.startswith('?') and len(txt) > 2 and txt[1] in ' \t':
            emitter.emit_bullet(txt[1:].strip())
            continue

        # Bold + large = unclassified heading
        if para_is_heading_bold(p):
            emitter.emit_heading(3, txt)
            continue

        emitter.emit_body(txt)


def main():
    global SECTION_FILE, SECTION_TITLE, SECTION_ORDER, TITLE_TO_NUM
    global STOP_PATTERN, STOP_TITLES
    if len(sys.argv) < 4:
        print('usage: wipi_docx_to_capi.py <mode:capi|hal> <out_dir> <docx1> [docx2 ...]',
              file=sys.stderr)
        return 2
    mode = sys.argv[1]
    if mode not in SECTION_CONFIGS:
        print(f'unknown mode {mode!r}; pick one of {list(SECTION_CONFIGS)}', file=sys.stderr)
        return 2
    cfg = SECTION_CONFIGS[mode]
    SECTION_FILE = dict(cfg['file'])
    SECTION_TITLE = dict(cfg['title'])
    SECTION_ORDER = list(SECTION_FILE.keys())
    TITLE_TO_NUM = {SECTION_TITLE[k]: k for k in SECTION_ORDER}
    STOP_PATTERN = cfg['stop_pattern']
    STOP_TITLES = set(cfg['stop_titles'])

    out_dir = sys.argv[2]
    docx_paths = []
    for arg in sys.argv[3:]:
        # glob expansion (Windows shells may not expand)
        expanded = glob.glob(arg)
        if expanded:
            docx_paths.extend(sorted(expanded))
        else:
            docx_paths.append(arg)
    print(f'Processing {len(docx_paths)} docx files:')
    for p in docx_paths:
        print(' ', os.path.basename(p))

    os.makedirs(out_dir, exist_ok=True)
    emitter = SectionEmitter()
    for p in docx_paths:
        process_docx(p, emitter)
    emitter.finalize(out_dir)


if __name__ == '__main__':
    main()
