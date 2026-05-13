"""Convert a Sun spec docx (CLDC/MIDP/etc) to clean Markdown.

Handles:
- Heading styles "1".."5" → ## .. ######
- Tables → GitHub-flavoured Markdown
- Images → saves to <image_dir>/<prefix>-imgN.<ext> and inserts ![]() refs
- Strips: cover page, copyright boilerplate, TOC entries, recurring footers
- Coalesces chapter-marker pairs ("1장" + "소개 및 배경")

Usage:
    python docx_to_md.py <input.docx> <out.md> <image_dir> <image_prefix>
"""
import sys, os, re, zipfile, shutil
from xml.etree import ElementTree as ET

NS = {
    'w':   'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r':   'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'a':   'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
}
W = NS['w']
A = NS['a']
R = NS['r']

# ---------- DOCX parsing ----------

def load_rels(z):
    rels = {}
    with z.open('word/_rels/document.xml.rels') as f:
        tree = ET.parse(f)
    for rel in tree.getroot():
        rels[rel.get('Id')] = rel.get('Target')
    return rels

def run_text(r):
    parts = []
    for child in r:
        tag = child.tag.split('}')[1]
        if tag == 't':
            parts.append(child.text or '')
        elif tag == 'tab':
            parts.append('\t')
        elif tag == 'br':
            parts.append('\n')
        elif tag == 'noBreakHyphen':
            parts.append('-')
    return ''.join(parts)

def is_bold_run(r):
    rPr = r.find('w:rPr', NS)
    if rPr is None:
        return False
    b = rPr.find('w:b', NS)
    return b is not None and b.get('{%s}val' % W) not in ('false', '0')

def para_all_bold(p):
    runs = p.findall('w:r', NS)
    runs = [r for r in runs if (r.find('w:t', NS) is not None and (r.find('w:t', NS).text or '').strip())]
    if not runs:
        return False
    return all(is_bold_run(r) for r in runs)

def is_code_run(r):
    rPr = r.find('w:rPr', NS)
    if rPr is None:
        return False
    rFonts = rPr.find('w:rFonts', NS)
    if rFonts is None:
        return False
    for attr in ('{%s}ascii' % W, '{%s}hAnsi' % W, '{%s}cs' % W):
        v = (rFonts.get(attr) or '').lower()
        if 'courier' in v or 'mono' in v or 'consolas' in v:
            return True
    return False

def para_text_with_runs(p):
    """Return list of (text, is_code) for runs in paragraph."""
    items = []
    for child in p:
        tag = child.tag.split('}')[1]
        if tag == 'r':
            t = run_text(child)
            if t:
                items.append((t, is_code_run(child)))
        elif tag == 'hyperlink':
            # treat all runs inside as one item
            sub = ''
            for r in child.findall('w:r', NS):
                sub += run_text(r)
            if sub:
                items.append((sub, False))
    return items

def merge_runs_to_markdown(items):
    """Collapse adjacent runs of same code/non-code, produce MD with inline `code`."""
    if not items:
        return ''
    merged = []
    cur_text, cur_code = items[0]
    for t, c in items[1:]:
        if c == cur_code:
            cur_text += t
        else:
            merged.append((cur_text, cur_code))
            cur_text, cur_code = t, c
    merged.append((cur_text, cur_code))
    out = []
    for t, c in merged:
        if c and t.strip():
            # escape backticks in inline code
            out.append('`' + t + '`')
        else:
            out.append(t)
    return ''.join(out)

def style_of(p):
    pPr = p.find('w:pPr', NS)
    if pPr is None:
        return ''
    pStyle = pPr.find('w:pStyle', NS)
    if pStyle is None:
        return ''
    return pStyle.get('{%s}val' % W, '')

def numPr_of(p):
    pPr = p.find('w:pPr', NS)
    if pPr is None:
        return None
    return pPr.find('w:numPr', NS)

def blip_embed(p):
    for blip in p.iter('{%s}blip' % A):
        e = blip.get('{%s}embed' % R)
        if e:
            return e
    return None

def cell_text_lines(tc):
    lines = []
    for p in tc.findall('w:p', NS):
        items = para_text_with_runs(p)
        line = merge_runs_to_markdown(items).strip()
        if line:
            lines.append(line)
    return lines

def table_to_md(tbl):
    rows = []
    for tr in tbl.findall('w:tr', NS):
        cells = []
        for tc in tr.findall('w:tc', NS):
            cell = ' '.join(cell_text_lines(tc))
            cell = cell.replace('|', '\\|').replace('\n', ' ')
            cells.append(cell)
        rows.append(cells)
    if not rows:
        return ''
    width = max(len(r) for r in rows)
    for r in rows:
        while len(r) < width:
            r.append('')
    out = []
    out.append('| ' + ' | '.join(rows[0]) + ' |')
    out.append('|' + '|'.join(['---'] * width) + '|')
    for r in rows[1:]:
        out.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(out)

# ---------- Filtering noise ----------

NOISE_PATTERNS = [
    re.compile(r'^Connected Limited Device Configuration\s*[•·]\s*\d{4}'),
    re.compile(r'^\d{1,4}\s*Connected Limited Device Configuration'),
    re.compile(r'^[ivxlcdm]+\s*Connected Limited', re.I),
    re.compile(r'^목차\s*[ivx\d]+$'),
    re.compile(r'^머리말\s*[ivx\d]+$'),
    re.compile(r'^4150 Network Circle'),
    re.compile(r'^Santa Clara'),
    re.compile(r'^Copyright \d{4} Sun Microsystems'),
    re.compile(r'^NOTICE; LIMITED LICENSE'),
    re.compile(r'^RESTRICTED RIGHTS LEGEND'),
    re.compile(r'^LIMITATION OF LIABILITY'),
    re.compile(r'^Java™ 2 Platform, Micro Edition'),
    re.compile(r'^This document does not represent'),
    re.compile(r'^Specification: JSR'),
    re.compile(r'^Version: \d'),
    re.compile(r'^Status: '),
    re.compile(r'^Release: '),
    re.compile(r'^\(LFI#'),
    re.compile(r'^Sun also grants'),
    re.compile(r'^You need not include'),
    re.compile(r'^For the purposes of'),
    re.compile(r'^This Agreement will terminate'),
    re.compile(r'^No right, title'),
    re.compile(r'^THE SPECIFICATION'),
    re.compile(r'^MERCHANTABILITY'),
    re.compile(r'^CONTENTS OF THE SPECIFICATION'),
    re.compile(r'^OR IMPLEMENTATION'),
    re.compile(r'^CHANGES WILL BE INCORPORATED'),
    re.compile(r'^MAY MAKE IMPROVEMENTS'),
    re.compile(r'^PROGRAM\(S\) DESCRIBED'),
    re.compile(r'^Specification will be governed'),
    re.compile(r'^TO THE EXTENT NOT PROHIBITED'),
    re.compile(r'^CAUSED AND REGARDLESS'),
    re.compile(r'^You will indemnify'),
    re.compile(r'^If this Software is being acquired'),
    re.compile(r'^You may wish to report'),
    re.compile(r'^Sun Microsystems, Inc\.'),
    re.compile(r'^재활용\s*$'),
    re.compile(r'^Confidential$', re.I),
]

def is_noise(line):
    s = line.strip()
    if not s:
        return False
    for p in NOISE_PATTERNS:
        if p.search(s):
            return True
    # very long english copyright sentences
    if len(s) > 60 and not re.search(r'[가-힣]', s) and s.endswith('.'):
        if re.search(r'\b(license|specification|copyright|warranty|liability|agreement|implementation)\b', s, re.I):
            return True
    return False

# TOC line detection: "1.2 Some title 5"-ish (ends with page number digits)
TOC_LINE = re.compile(r'^[\d.A-Z]+\s+.+\s+\d+\s*$')

def looks_like_toc(line):
    s = line.strip()
    if TOC_LINE.match(s) and len(s) < 120:
        return True
    # "그림 1 ... 10" style
    if re.match(r'^그림\s*\d+.*\s+\d+\s*$', s):
        return True
    return False

# ---------- Main pipeline ----------

def main(inp, outp, img_dir, prefix):
    z = zipfile.ZipFile(inp)
    rels = load_rels(z)
    with z.open('word/document.xml') as f:
        tree = ET.parse(f)
    body = tree.getroot().find('w:body', NS)

    os.makedirs(img_dir, exist_ok=True)
    # Map rId -> saved filename (relative path for ![]() insertion)
    saved_images = {}
    image_counter = [0]
    # md path relative root for image link
    md_dir = os.path.dirname(os.path.abspath(outp))
    img_dir_abs = os.path.abspath(img_dir)

    def save_image(rid):
        if rid in saved_images:
            return saved_images[rid]
        target = rels.get(rid)
        if not target:
            return None
        src = 'word/' + target.lstrip('/')
        if not src.startswith('word/media/'):
            # rel target may be 'media/imageX.jpg' relative to word/_rels/document.xml.rels
            src = 'word/' + target if target.startswith('media/') else 'word/' + target
        try:
            data = z.read(src)
        except KeyError:
            # try without leading word/
            try:
                data = z.read(target)
            except KeyError:
                return None
        ext = os.path.splitext(target)[1] or '.png'
        image_counter[0] += 1
        fname = f'{prefix}-img{image_counter[0]}{ext}'
        full = os.path.join(img_dir, fname)
        with open(full, 'wb') as f:
            f.write(data)
        # rel link from md to image
        rel = os.path.relpath(full, md_dir).replace('\\', '/')
        saved_images[rid] = rel
        return rel

    out_lines = []
    # started: True after we hit "머리말" (preface) heading.
    # Until then, drop everything (cover, copyright, TOC, figure list).
    # If document has no "머리말", start from the beginning.
    has_preface = False
    for p in body.iter('{%s}p' % W):
        s = style_of(p)
        if s != '1':
            continue
        items = para_text_with_runs(p)
        t = merge_runs_to_markdown(items).strip()
        if t == '머리말':
            has_preface = True
            break
    started = not has_preface
    # TOC-block headings to skip
    toc_headings = {'규격', '차례', '목차', '그림', '표', 'CONTENTS', 'FIGURES', 'TABLES',
                    'TRADEMARKS', 'NOTICE; LIMITED LICENSE GRANTS', 'REPORT',
                    'LIMITATION OF LIABILITY', 'RESTRICTED RIGHTS LEGEND',
                    'Version: 1.1', 'Status: FCS'}

    def normspace(t):
        # "1.1CLDC" → "1.1 CLDC"; insert space only when number is followed by a letter.
        t = re.sub(r'^(\d+(?:\.\d+)+)([가-힣A-Za-z])', r'\1 \2', t)
        # Replace tab between section number and title with a single space.
        t = re.sub(r'^(\d+(?:\.\d+)*)\t+', r'\1 ', t)
        return t

    for child in body:
        tag = child.tag.split('}')[1]
        if tag == 'p':
            s = style_of(child)
            items = para_text_with_runs(child)
            txt = merge_runs_to_markdown(items).strip()
            img_rid = blip_embed(child)

            # Drop empty paragraphs (no text, no image)
            if not txt and not img_rid:
                continue

            # Preface marker - first real content heading
            if s == '1' and txt.strip() == '머리말':
                started = True
                out_lines.append('')
                out_lines.append('## 머리말')
                out_lines.append('')
                continue

            # TOC-block heading 1 (before preface): skip
            if s == '1' and txt.strip() in toc_headings:
                continue

            # Before content has started: drop everything
            if not started:
                continue

            # Heading styles 1..5 → markdown headings
            if s in ('1', '2', '3', '4', '5'):
                if is_noise(txt):
                    continue
                if looks_like_toc(txt):
                    continue
                norm = normspace(txt)
                # Prefer dot-count of leading section number for level (more reliable
                # than docx style on inconsistently styled docs).
                m = re.match(r'^(\d+(?:\.\d+)*)\.?\s', norm)
                if m:
                    level = 1 + m.group(1).count('.') + 1  # "1"→h2, "1.1"→h3, "1.1.1"→h4
                else:
                    level = int(s) + 1
                level = min(level, 6)
                hashes = '#' * level
                out_lines.append('')
                out_lines.append(f'{hashes} {norm}')
                out_lines.append('')
                continue

            # Body paragraph
            if is_noise(txt):
                continue

            # Promote to heading if short, all-bold, and starts with dotted section number.
            m_h = re.match(r'^(\d+(?:\.\d+)*)\.?\s', txt)
            if m_h and len(txt) < 80 and para_all_bold(child):
                level = min(1 + m_h.group(1).count('.') + 1, 6)
                hashes = '#' * level
                out_lines.append('')
                out_lines.append(f'{hashes} {normspace(txt)}')
                out_lines.append('')
                continue

            # Image
            if img_rid:
                rel = save_image(img_rid)
                if rel:
                    # alt text from any text in this paragraph or next caption
                    alt = txt or os.path.basename(rel)
                    # If paragraph has noisy concatenated diagram labels, strip
                    if len(alt) > 80:
                        alt = ''
                    out_lines.append('')
                    out_lines.append(f'![{alt}]({rel})')
                    out_lines.append('')
                    continue

            # Bullet: numPr or "■" prefix
            numPr = numPr_of(child)
            if numPr is not None or txt.startswith('■'):
                clean = txt.lstrip('■').lstrip('•').lstrip('●').lstrip().strip()
                if clean:
                    out_lines.append('- ' + clean)
                continue

            # Default
            out_lines.append(txt)
            out_lines.append('')

        elif tag == 'tbl':
            if not started:
                continue
            md = table_to_md(child)
            if md.strip():
                out_lines.append('')
                out_lines.append(md)
                out_lines.append('')

    # Collapse multiple blank lines
    final = []
    blank = 0
    for line in out_lines:
        if not line.strip():
            blank += 1
            if blank <= 1:
                final.append('')
        else:
            blank = 0
            final.append(line)

    with open(outp, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final).rstrip() + '\n')
    print(f'Wrote {outp}: {len(final)} lines, {len(saved_images)} images saved')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
