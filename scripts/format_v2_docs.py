#!/usr/bin/env python3
"""
Post-process PDF-extracted text into properly formatted Markdown
for WIPI 2.2.0 API documentation.

Reads .md files under src/content/docs/v2/ (except index.md) and reformats
them in-place to match the v1.2.1 reference format.

Usage:
    python3 scripts/format_v2_docs.py
"""

import re
import os
import sys

V2_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "src", "content", "docs", "v2")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

API_PREFIXES = ("MH_", "MC_", "MJ_", "MM_", "MS_")

# Identifiers that should be wrapped in backticks when found inline
INLINE_CODE_RE = re.compile(
    r'(?<![`\w])'
    r'('
    r'(?:MH_|MC_|MJ_|MM_|MS_)[A-Za-z0-9_]+(?:\(\))?'
    r'|M_(?:Int32|Uint32|Int16|Uint16|Int8|Uint8|Int64|Uint64|Byte|Char|Boolean|Ucode|Sint32|Sint16)'
    r'|M_E_[A-Z_]+'
    r'|(?:TRUE|FALSE|NULL)(?![A-Za-z_])'
    r'|DECLARE_INDIRECTBUF(?:\(\))?'
    r'|MC_GETDPTR(?:\(\))?'
    r'|INDIRECT_BUF_HEAD'
    r')'
    r'(?![`\w])'
)

# Known macro patterns that ARE API headers even though all-caps
MACRO_HEADER_PATTERNS = [
    r'^MC_PRGTYPE_\w+$',
    r'^MC_DIR_\w+$',
    r'^MC_NETWORK_ACCESS_REQ_MASK$',
    r'^MC_SERIAL_ACCESS_REQ_MASK$',
    r'^MC_SYSTEM\d+_ACCESS_REQ_MASK$',
    r'^MC_GETDPTR$',
    r'^MC_GRP_\w+$',
    r'^MC_GRP\w+$',
]

# Event/enum value patterns - NOT API function headers
EVENT_PATTERNS = [
    r'^MH_KEY_PRESSEVENT$',
    r'^MH_KEY_RELEASEEVENT$',
    r'^MH_KEY_REPEATEVENT$',
    r'^MH_\w+_EVENT$',
    r'^MH_EXIT_EVENT$',
    r'^MH_IODEVICEEV_\w+$',
    r'^MH_IODEV_EVENT$',
    r'^MH_NETEV_\w+$',
    r'^MH_MDAEV_\w+$',
    r'^MH_GPSEV_\w+$',
    r'^MH_CS_\w+$',
    r'^MH_ANN_\w+$',
    r'^MH_SERIAL_\w+$',
    r'^MH_SMS_\w+$',
    r'^MH_CALL_\w+$',
    r'^MH_PPP_\w+$',
    r'^MH_SOCKET_\w+$',
    r'^MH_KEY_\w+$',      # MH_KEY_0, MH_KEY_UP, etc.
]

SECTION_LABELS = {
    "프로토타입": "프로토타입",
    "설명": "설명",
    "매개 변수": "매개 변수",
    "매개변수": "매개 변수",
    "반환 값": "반환 값",
    "반환값": "반환 값",
    "부작용": "부작용",
    "참고 항목": "참고 항목",
    "참고항목": "참고 항목",
}

SECTION_LABEL_SET = set(SECTION_LABELS.keys()) | set(SECTION_LABELS.values())

C_TYPE_KEYWORDS = (
    'void', 'int', 'char', 'short', 'long', 'unsigned', 'signed', 'float', 'double',
    'M_Int32', 'M_Uint32', 'M_Int16', 'M_Uint16', 'M_Byte', 'M_Char', 'M_Boolean',
    'M_Int8', 'M_Uint8', 'M_Int64', 'M_Uint64', 'M_Ucode', 'M_Sint32', 'M_Sint16',
)

# PUA characters used as bullets in PDF extraction
PUA_RE = re.compile('[\uf06c\uf0e7\uf0e8]')

# ---------------------------------------------------------------------------
# Classification helpers
# ---------------------------------------------------------------------------

def is_event_name(name):
    """Check if name matches any event/enum constant pattern."""
    for pat in EVENT_PATTERNS:
        if re.match(pat, name):
            return True
    return False


def is_api_function_header(name):
    """Check if a name should become a ### heading (function or macro)."""
    name = name.strip()
    if not name:
        return False
    if not re.match(r'^[A-Z][A-Za-z0-9_]+$', name):
        return False

    # Special names
    if name in ("TIMERCB", "MCTimer") or name.startswith("DECLARE_INDIRECTBUF"):
        return True

    has_prefix = any(name.startswith(p) for p in API_PREFIXES)
    if not has_prefix:
        return False

    # Filter out event/enum names
    if is_event_name(name):
        return False

    # Has lowercase letters after prefix = function name
    after_first_underscore = name.split('_', 1)[1] if '_' in name else ''
    if any(c.islower() for c in after_first_underscore):
        return True

    # Known macro patterns
    for pat in MACRO_HEADER_PATTERNS:
        if re.match(pat, name):
            return True

    # MC_ all-caps are likely macros/defines that deserve their own section
    if name.startswith("MC_"):
        return True

    return False


def normalize_event_name(text):
    """
    Clean up event names with spurious spaces like 'MH_ MEDIA _EVENT'.
    Only matches if the entire text (after cleanup) is a single event name.
    Returns the cleaned event name, or None.
    """
    text = text.strip()
    if not text:
        return None

    # Direct match first (no spaces in name)
    if is_event_name(text):
        return text

    # Try removing internal spaces for names like "MH_ MEDIA _EVENT"
    # Only do this if text starts with a known prefix
    if any(text.startswith(p) for p in API_PREFIXES):
        cleaned = re.sub(r'\s+', '', text)
        if is_event_name(cleaned):
            return cleaned

    return None


def is_c_code_start(line):
    """Check if line looks like the start of a C code block."""
    s = line.strip()
    if not s:
        return False
    if re.match(r'^(typedef\s+|enum\s+[\w_]|struct\s+[\w_]|#define\s+)', s):
        return True
    # C type followed by identifier (declaration or function pointer)
    for t in C_TYPE_KEYWORDS:
        if s.startswith(t + ' ') or s.startswith(t + '\t') or s.startswith(t + '*'):
            rest = s[len(t):].strip()
            if re.match(r'^[\*\w]', rest):
                return True
    return False


def is_param_line(line):
    """Check if line is a parameter with [in]/[out]/[in/out] marker."""
    return bool(re.match(r'^\[(?:in|out|in/out)\]\s+', line.strip()))


def is_table_caption(line):
    """Check if line is a table caption like <표 2-2-1>..."""
    return bool(re.match(r'^<표\s*[\d\-]+>', line.strip()))


def is_section_label(text):
    """Check if text is a section label like 프로토타입, 설명, etc."""
    return text.strip() in SECTION_LABEL_SET


def is_subsection_header(line):
    """Check if a leading-space line is a sub-section header (Korean text, short)."""
    stripped = line.strip()
    if not stripped or len(stripped) > 80:
        return False
    if is_api_function_header(stripped):
        return False
    if is_section_label(stripped):
        return False
    if is_param_line(stripped):
        return False
    if is_c_code_start(stripped):
        return False
    if re.match(r'^[\[\("]', stripped):
        return False
    # Must be Korean/alphanumeric text, not code-like
    if re.match(r'^[가-힣A-Za-z0-9_/() ]+$', stripped):
        return True
    return False


# ---------------------------------------------------------------------------
# Text processing helpers
# ---------------------------------------------------------------------------

def join_broken_text(lines):
    """Join PDF-broken text lines into a single paragraph."""
    if not lines:
        return ""
    result = lines[0].strip()
    for line in lines[1:]:
        s = line.strip()
        if s:
            result += ' ' + s
    return re.sub(r'  +', ' ', result)


def join_broken_code(lines):
    """Join broken C code lines, preserving line breaks at statement boundaries."""
    if not lines:
        return ""
    result = []
    current = lines[0].rstrip()
    for line in lines[1:]:
        s = line.strip()
        # Join if current line doesn't end with a statement terminator
        # and next line doesn't start a new statement
        if (current and not current.rstrip().endswith((';', '{', '}', ')', ',', '*/', '\\'))
            and not s.startswith(('#', '//', '/*', 'typedef', 'enum', 'struct'))
            and not re.match(r'^[A-Z_]+\s*=', s)):
            current += ' ' + s
        else:
            result.append(current)
            current = s
    result.append(current)
    return '\n'.join(result)


def wrap_inline_code(text):
    """Wrap known API identifiers in backticks within prose text."""
    if not text or text.strip().startswith(('```', '#', '|')):
        return text

    def replacer(m):
        return '`' + m.group(1) + '`'

    return INLINE_CODE_RE.sub(replacer, text)


# ---------------------------------------------------------------------------
# Normalization (strip previous formatting for idempotency)
# ---------------------------------------------------------------------------

def strip_existing_formatting(body):
    """Strip any formatting from previous runs to make the script idempotent."""
    lines = body.split('\n')
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Handle PUA characters - split on them
        if PUA_RE.search(line):
            parts = PUA_RE.split(line)
            for j, part in enumerate(parts):
                part = part.strip()
                if not part:
                    continue
                if is_api_function_header(part):
                    new_lines.append(f' {part}')
                elif j > 0 and is_subsection_header(f' {part}'):
                    new_lines.append(f' {part}')
                else:
                    new_lines.append(part)
            i += 1
            continue

        # Remove ### headings -> leading-space format
        heading_match = re.match(r'^###\s+(.+)$', stripped)
        if heading_match:
            name = heading_match.group(1).strip()
            if is_api_function_header(name):
                new_lines.append(f' {name}')
            else:
                new_lines.append(line)
            i += 1
            continue

        # Remove #### sub-section headings
        sub_heading_match = re.match(r'^####\s+(.+)$', stripped)
        if sub_heading_match:
            name = sub_heading_match.group(1).strip()
            new_lines.append(f' {name}')
            i += 1
            continue

        # Remove **bold** section labels -> plain
        bold_match = re.match(r'^\*\*(.+?)\*\*$', stripped)
        if bold_match:
            label_text = bold_match.group(1)
            if label_text in SECTION_LABELS.values() or label_text in SECTION_LABELS:
                new_lines.append(label_text)
                i += 1
                continue

        # Unwrap code fences
        if stripped == '```c' or stripped == '```':
            if stripped == '```':
                i += 1
                continue
            i += 1
            while i < len(lines):
                inner = lines[i]
                inner_stripped = inner.strip()
                if inner_stripped == '```':
                    i += 1
                    break
                if inner_stripped == '```c':
                    i += 1
                    continue
                new_lines.append(inner_stripped)
                i += 1
            continue

        # Remove bullet-format param lines: "- `param` - [in] desc"
        bullet_param = re.match(r'^- `(\w+)` - \[(in|out|in/out)\] (.*)$', stripped)
        if bullet_param:
            new_lines.append(f'[{bullet_param.group(2)}] {bullet_param.group(1)} {bullet_param.group(3)}')
            i += 1
            continue

        # Remove bullet-format plain param: "- `param` - desc"
        bullet_plain = re.match(r'^- `(\w+)` - (.+)$', stripped)
        if bullet_plain:
            new_lines.append(f'{bullet_plain.group(1)} {bullet_plain.group(2)}')
            i += 1
            continue

        # Remove bullet-format constants: "- `TRUE`" etc.
        bullet_const = re.match(r'^- `(\w+)`$', stripped)
        if bullet_const:
            new_lines.append(bullet_const.group(1))
            i += 1
            continue

        # Remove > **<표...>** blockquote formatting
        table_bq = re.match(r'^>\s*\*\*(<표.+?>.*?)\*\*$', stripped)
        if table_bq:
            new_lines.append(table_bq.group(1))
            i += 1
            continue

        # Remove inline backticks around known identifiers
        line_clean = re.sub(
            r'`((?:MH_|MC_|MJ_|MM_|MS_|M_E_|M_Int|M_Uint|M_Byte|M_Char|M_Boolean|M_Ucode|M_Sint|TRUE|FALSE|NULL|DECLARE_INDIRECTBUF|MC_GETDPTR|INDIRECT_BUF_HEAD)\w*(?:\(\))?)`',
            r'\1', stripped)
        if line_clean != stripped:
            new_lines.append(line_clean)
            i += 1
            continue

        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines)


# ---------------------------------------------------------------------------
# Main formatting engine
# ---------------------------------------------------------------------------

class Formatter:
    def __init__(self, lines):
        self.lines = lines
        self.i = 0
        self.output = []

    def peek(self, offset=0):
        idx = self.i + offset
        return self.lines[idx] if idx < len(self.lines) else None

    def at_end(self):
        return self.i >= len(self.lines)

    def advance(self):
        self.i += 1

    def emit(self, text):
        self.output.append(text)

    def emit_blank(self):
        if self.output and self.output[-1] != '':
            self.output.append('')

    def skip_blanks(self):
        count = 0
        while not self.at_end() and not self.lines[self.i].strip():
            self.i += 1
            count += 1
        return count

    def peek_next_nonblank_idx(self):
        j = self.i
        while j < len(self.lines) and not self.lines[j].strip():
            j += 1
        return j

    def at_function_boundary(self):
        """Check if current line is a function header or section label."""
        if self.at_end():
            return True
        line = self.lines[self.i]
        stripped = line.strip()

        if is_section_label(stripped):
            return True

        # Leading-space function header
        if re.match(r'^\s+\S', line) and is_api_function_header(stripped):
            return True

        # PUA-prefixed function header
        if PUA_RE.search(line):
            for part in PUA_RE.split(line):
                if is_api_function_header(part.strip()):
                    return True

        return False

    def _is_boundary_at(self, j):
        if j >= len(self.lines):
            return True
        line = self.lines[j]
        stripped = line.strip()
        if is_section_label(stripped):
            return True
        if re.match(r'^\s+\S', line) and is_api_function_header(stripped):
            return True
        if PUA_RE.search(line):
            for part in PUA_RE.split(line):
                if is_api_function_header(part.strip()):
                    return True
        return False

    # ---- Section collectors ----

    def collect_prototype(self):
        """Collect prototype lines and format as ```c code block."""
        self.skip_blanks()
        code_lines = []
        while not self.at_end():
            stripped = self.lines[self.i].strip()
            if not stripped:
                if code_lines:
                    break
                self.advance()
                continue
            if self.at_function_boundary() or is_table_caption(stripped):
                break
            code_lines.append(stripped)
            self.advance()

        if code_lines:
            joined = join_broken_code(code_lines)
            self.emit('')
            self.emit('```c')
            self.emit(joined)
            self.emit('```')
        self.emit('')

    def collect_params(self):
        """Collect parameter descriptions and format as bullet list."""
        self.skip_blanks()
        self.emit('')

        while not self.at_end():
            stripped = self.lines[self.i].strip()

            if not stripped:
                j = self.peek_next_nonblank_idx()
                if j >= len(self.lines) or self._is_boundary_at(j):
                    break
                if is_param_line(self.lines[j].strip()):
                    self.i = j
                    continue
                break

            if self.at_function_boundary() or is_table_caption(stripped):
                break

            param_match = re.match(r'^\[(in|out|in/out)\]\s+(\w+)\s*(.*)', stripped)
            if param_match:
                direction = param_match.group(1)
                pname = param_match.group(2)
                desc = param_match.group(3).strip()
                self.advance()
                while not self.at_end():
                    cont = self.lines[self.i].strip()
                    if (not cont or is_section_label(cont)
                            or is_param_line(cont) or self.at_function_boundary()
                            or is_table_caption(cont)):
                        break
                    desc += ' ' + cont
                    self.advance()
                desc = re.sub(r'  +', ' ', desc).strip()
                self.emit(f'- `{pname}` - [{direction}] {desc}')
            else:
                # Plain param: "name description..."
                plain = re.match(r'^(\w+)\s+(.*)', stripped)
                if plain and not is_section_label(stripped):
                    pname = plain.group(1)
                    pdesc = plain.group(2).strip()
                    self.advance()
                    while not self.at_end():
                        cont = self.lines[self.i].strip()
                        if (not cont or is_section_label(cont)
                                or is_param_line(cont) or self.at_function_boundary()):
                            break
                        if re.match(r'^[a-zA-Z]\w*\s+\S', cont) and not cont.startswith(('에', '를', '가', '의', '을', '는', '이')):
                            break
                        pdesc += ' ' + cont
                        self.advance()
                    pdesc = re.sub(r'  +', ' ', pdesc).strip()
                    self.emit(f'- `{pname}` - {pdesc}')
                else:
                    self.emit(stripped)
                    self.advance()

        self.emit('')

    def collect_return_value(self):
        """Collect return value descriptions."""
        self.skip_blanks()
        self.emit('')

        while not self.at_end():
            stripped = self.lines[self.i].strip()

            if not stripped:
                j = self.peek_next_nonblank_idx()
                if j >= len(self.lines) or self._is_boundary_at(j):
                    break
                self.emit('')
                self.advance()
                continue

            if self.at_function_boundary():
                break

            err_match = re.match(r'^(M_E_\w+)\s+(.*)', stripped)
            if err_match:
                desc = err_match.group(2).strip()
                self.advance()
                while not self.at_end():
                    cont = self.lines[self.i].strip()
                    if (not cont or is_section_label(cont)
                            or self.at_function_boundary() or re.match(r'^M_E_\w+', cont)):
                        break
                    desc += ' ' + cont
                    self.advance()
                desc = re.sub(r'  +', ' ', desc).strip()
                self.emit(f'- `{err_match.group(1)}` - {desc}')
            elif stripped in ('성공', '실패'):
                self.emit(stripped)
                self.emit('')
                self.advance()
            elif re.match(r'^(TRUE|FALSE)\b', stripped):
                word = stripped.split()[0]
                rest = stripped[len(word):].strip()
                # Collect continuation
                self.advance()
                while not self.at_end():
                    cont = self.lines[self.i].strip()
                    if (not cont or is_section_label(cont)
                            or self.at_function_boundary()
                            or re.match(r'^(TRUE|FALSE|M_E_)\w*', cont)
                            or cont in ('성공', '실패')):
                        break
                    rest += ' ' + cont
                    self.advance()
                rest = re.sub(r'  +', ' ', rest).strip()
                if rest:
                    self.emit(f'- `{word}` - {rest}')
                else:
                    self.emit(f'- `{word}`')
            elif stripped.startswith('0') or stripped in ('양수', '음수') or re.match(r'^-?\d+', stripped):
                self.emit(f'- {stripped}')
                self.advance()
            else:
                # General text
                desc_lines = [stripped]
                self.advance()
                while not self.at_end():
                    cont = self.lines[self.i].strip()
                    if (not cont or is_section_label(cont)
                            or self.at_function_boundary()
                            or re.match(r'^M_E_\w+', cont)
                            or cont in ('성공', '실패')
                            or re.match(r'^(TRUE|FALSE)\b', cont)):
                        break
                    desc_lines.append(cont)
                    self.advance()
                self.emit(join_broken_text(desc_lines))

        self.emit('')

    def collect_general_section(self):
        """Collect general section content (설명, 부작용, 참고 항목)."""
        self.skip_blanks()
        self.emit('')

        while not self.at_end():
            line = self.lines[self.i]
            stripped = line.strip()

            if not stripped:
                j = self.peek_next_nonblank_idx()
                if j >= len(self.lines) or self._is_boundary_at(j) or is_table_caption(self.lines[j].strip()):
                    break
                self.emit('')
                self.advance()
                continue

            if self.at_function_boundary() or is_table_caption(stripped):
                break
            if is_c_code_start(stripped):
                break
            if re.match(r'^\s+\S', line) and is_subsection_header(line):
                break

            # Collect paragraph lines
            para = []
            while not self.at_end():
                cur = self.lines[self.i]
                s = cur.strip()
                if not s:
                    break
                if self.at_function_boundary() or is_table_caption(s):
                    break
                if is_c_code_start(s):
                    break
                if re.match(r'^\s+\S', cur) and is_subsection_header(cur):
                    break
                para.append(s)
                self.advance()

            if para:
                self.emit(join_broken_text(para))

        self.emit('')

    def collect_c_code_block(self):
        """Collect a C code block (enum, struct, typedef, etc.) and wrap in ```c."""
        code_lines = []
        brace_depth = 0
        start = self.i
        _max_lines = 200  # safety limit

        while not self.at_end() and (self.i - start) < _max_lines:
            stripped = self.lines[self.i].strip()

            if not stripped:
                if brace_depth > 0:
                    code_lines.append('')
                    self.advance()
                    continue
                break

            if brace_depth <= 0 and self.i > start and self.at_function_boundary():
                break

            brace_depth += stripped.count('{') - stripped.count('}')
            code_lines.append(stripped)
            self.advance()

            if brace_depth <= 0 and self.i > start:
                # For single-statement lines (ending with ;), break immediately
                if stripped.rstrip().endswith(';') and self.i == start + 1:
                    break
                if self.i > start + 1:
                    # Check if next non-blank line continues the code
                    if not self.at_end():
                        next_s = self.lines[self.i].strip()
                        if not next_s:
                            j = self.peek_next_nonblank_idx()
                            if j < len(self.lines) and is_c_code_start(self.lines[j].strip()):
                                code_lines.append('')
                                self.advance()
                                continue
                        elif is_c_code_start(next_s) or next_s.startswith('typedef '):
                            continue
                        elif stripped.endswith(','):
                            continue
                    break

        if code_lines:
            self.emit_blank()
            self.emit('```c')
            for cl in code_lines:
                self.emit(cl)
            self.emit('```')
            self.emit('')

    def collect_event_descriptions(self):
        """
        Collect event description pairs: EVENT_NAME on one line, desc on next.
        Format as bullet list: - `EVENT_NAME` - description
        """
        self.emit('')
        items = []

        while not self.at_end():
            stripped = self.lines[self.i].strip()

            if not stripped:
                self.advance()
                j = self.peek_next_nonblank_idx()
                if j >= len(self.lines):
                    break
                next_s = self.lines[j].strip()
                norm = normalize_event_name(next_s)
                if norm:
                    continue
                break

            if self.at_function_boundary() or is_table_caption(stripped):
                break

            # Try to normalize the event name (handles "MH_ MEDIA _EVENT")
            norm = normalize_event_name(stripped)
            if norm:
                event_name = norm
                self.advance()
                # Collect description lines until next event or boundary
                desc_lines = []
                while not self.at_end():
                    dline = self.lines[self.i]
                    d = dline.strip()
                    if not d:
                        break
                    d_norm = normalize_event_name(d)
                    if d_norm:
                        break
                    if self.at_function_boundary() or is_table_caption(d):
                        break
                    if is_c_code_start(d):
                        break
                    # Stop at leading-space subsection headers
                    if re.match(r'^\s+\S', dline) and is_subsection_header(dline):
                        break
                    desc_lines.append(d)
                    self.advance()
                desc = join_broken_text(desc_lines) if desc_lines else ''
                items.append((event_name, desc))
            else:
                # Not an event name - stop
                break

        for name, desc in items:
            if desc:
                self.emit(f'- `{name}` - {desc}')
            else:
                self.emit(f'- `{name}`')

        self.emit('')

    def format_table_block(self):
        """Format a table caption and its following data."""
        stripped = self.lines[self.i].strip()
        self.emit_blank()
        self.emit(f'> **{stripped}**')
        self.emit('')
        self.advance()

        # Collect remaining table data until boundary
        while not self.at_end():
            line = self.lines[self.i]
            s = line.strip()
            if not s:
                j = self.peek_next_nonblank_idx()
                if j >= len(self.lines) or self._is_boundary_at(j) or is_table_caption(self.lines[j].strip()):
                    break
                # Check if next non-blank is a bare event name (event description block)
                next_s = self.lines[j].strip()
                norm = normalize_event_name(next_s)
                if norm and norm == next_s.strip():
                    break
                self.emit('')
                self.advance()
                continue
            if self.at_function_boundary() or is_table_caption(s):
                break
            # Check if we've hit C code
            if is_c_code_start(s):
                break
            # Check for leading-space subsection header
            if re.match(r'^\s+\S', line) and is_subsection_header(line):
                break
            # Check for bare event name on its own line (start of event description block)
            norm = normalize_event_name(s)
            if norm:
                # Table rows have event name + additional data on same line
                # Bare event names (event description) have just the name
                words_after = s.replace(norm, '', 1).strip() if norm in s else ''
                # If the name is alone or the original has spaces (like "MH_ MEDIA _EVENT")
                cleaned = re.sub(r'\s+', '', s)
                if cleaned == norm:
                    break
            self.emit(s)
            self.advance()

        self.emit('')


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def detect_title(body):
    """Extract title from first # heading."""
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped.startswith('# '):
            return stripped[2:].strip()
    return None


def format_file(filepath):
    """Process a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and body
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            existing_fm = parts[1]
            body = parts[2]
        else:
            existing_fm = ""
            body = content
    else:
        existing_fm = ""
        body = content

    # Strip previous formatting for idempotency
    body = strip_existing_formatting(body)

    # Extract title
    title = detect_title(body)
    if not title and existing_fm:
        tm = re.search(r'title:\s*"(.+?)"', existing_fm)
        if tm:
            title = tm.group(1)
    if not title:
        title = os.path.splitext(os.path.basename(filepath))[0].replace('-', ' ').title()

    # Build frontmatter
    frontmatter = f'---\ntitle: "{title}"\n---\n'

    # Remove the first # heading from body
    lines = body.split('\n')
    new_lines = []
    removed = False
    for line in lines:
        if not removed and line.strip().startswith('# '):
            removed = True
            continue
        new_lines.append(line)

    # Run the formatter
    fmt = Formatter(new_lines)
    process_body(fmt)

    # Apply inline code wrapping to prose lines (not code blocks, headings, tables)
    final_lines = []
    in_code = False
    for line in fmt.output:
        if line.strip().startswith('```'):
            in_code = not in_code
            final_lines.append(line)
            continue
        if in_code:
            final_lines.append(line)
            continue
        if line.strip().startswith(('#', '|')):
            final_lines.append(line)
            continue
        # For bullet params, only wrap in the description part
        m = re.match(r'^(- `\w+` - (?:\[(?:in|out|in/out)\] )?)(.*)', line)
        if m:
            final_lines.append(m.group(1) + wrap_inline_code(m.group(2)))
            continue
        final_lines.append(wrap_inline_code(line))

    body_text = '\n'.join(final_lines)
    body_text = re.sub(r'\n{4,}', '\n\n\n', body_text)
    body_text = '\n'.join(l.rstrip() for l in body_text.split('\n'))
    body_text = body_text.lstrip('\n')

    result = frontmatter + '\n' + body_text
    if not result.endswith('\n'):
        result += '\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result)


def process_body(fmt):
    """Main processing loop - state machine that dispatches to collectors."""
    _prev_i = -1
    _stuck = 0
    while not fmt.at_end():
        if fmt.i == _prev_i:
            _stuck += 1
            if _stuck > 5:
                # Safety: force advance to prevent infinite loop
                fmt.emit(fmt.lines[fmt.i])
                fmt.advance()
                continue
        else:
            _stuck = 0
        _prev_i = fmt.i
        line = fmt.lines[fmt.i]
        stripped = line.strip()

        # Skip blank lines
        if not stripped:
            fmt.advance()
            continue

        # --- Sub-heading: ## X.X. Title (overview files) ---
        heading2_match = re.match(r'^##\s+(.+)$', stripped)
        if heading2_match:
            fmt.emit_blank()
            fmt.emit(f'## {heading2_match.group(1)}')
            fmt.emit('')
            fmt.advance()
            continue

        # --- Function/macro header (leading space + API name) ---
        if re.match(r'^\s+\S', line):
            name = stripped
            if is_api_function_header(name):
                fmt.emit_blank()
                fmt.emit(f'### {name}')
                fmt.emit('')
                fmt.advance()
                continue
            elif is_subsection_header(line):
                fmt.emit_blank()
                fmt.emit(f'#### {name}')
                fmt.emit('')
                fmt.advance()
                continue

        # --- Section labels (프로토타입, 설명, etc.) ---
        if is_section_label(stripped):
            label = SECTION_LABELS.get(stripped, stripped)
            fmt.emit(f'**{label}**')
            fmt.advance()

            if label == "프로토타입":
                fmt.collect_prototype()
            elif label == "매개 변수":
                fmt.collect_params()
            elif label == "반환 값":
                fmt.collect_return_value()
            else:
                fmt.collect_general_section()
            continue

        # --- Table caption ---
        if is_table_caption(stripped):
            fmt.format_table_block()
            continue

        # --- Event description block ---
        norm = normalize_event_name(stripped)
        if norm:
            # Look ahead: is this an event-description block (event names followed by descriptions)?
            # Or is it a standalone event name reference?
            # Check if next non-blank line is a description (not code, not section, not event)
            j = fmt.i + 1
            while j < len(fmt.lines) and not fmt.lines[j].strip():
                j += 1
            if j < len(fmt.lines):
                next_s = fmt.lines[j].strip()
                next_norm = normalize_event_name(next_s)
                # If next line is another event name OR a description, it's an event block
                if (next_norm or
                    (not is_section_label(next_s) and not is_c_code_start(next_s)
                     and not is_api_function_header(next_s)
                     and not is_table_caption(next_s))):
                    fmt.collect_event_descriptions()
                    continue

            # Standalone event reference - just output
            fmt.emit(f'`{norm}`')
            fmt.advance()
            continue

        # --- C code blocks ---
        if is_c_code_start(stripped):
            fmt.collect_c_code_block()
            continue

        # --- Regular text paragraph ---
        para_lines = []
        while not fmt.at_end():
            cur_line = fmt.lines[fmt.i]
            s = cur_line.strip()
            if not s:
                break
            if fmt.at_function_boundary() or is_table_caption(s):
                break
            if is_c_code_start(s):
                break
            norm_check = normalize_event_name(s)
            if norm_check:
                break
            # Stop at leading-space subsection headers
            if re.match(r'^\s+\S', cur_line) and is_subsection_header(cur_line):
                break
            para_lines.append(s)
            fmt.advance()

        if para_lines:
            text = join_broken_text(para_lines)
            fmt.emit(text)
            fmt.emit('')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    root = os.path.abspath(V2_ROOT)
    if not os.path.isdir(root):
        print(f"Error: {root} not found")
        sys.exit(1)

    files_processed = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for fn in sorted(filenames):
            if not fn.endswith('.md'):
                continue
            if fn == 'index.md':
                continue
            filepath = os.path.join(dirpath, fn)
            relpath = os.path.relpath(filepath, root)
            print(f"Processing: {relpath}")
            try:
                format_file(filepath)
                files_processed += 1
            except Exception as e:
                print(f"  ERROR: {e}")
                import traceback
                traceback.print_exc()

    print(f"\nDone. Processed {files_processed} files.")


if __name__ == '__main__':
    main()
