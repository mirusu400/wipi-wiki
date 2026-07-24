#!/usr/bin/env python3
"""
format_v2_java.py -- Reformats v2.2 Java API markdown files extracted from PDF.

Strategy: Process line-by-line, detecting Java patterns embedded in plain text
and splitting them into proper markdown with code blocks and headings.
"""

import re
import sys
from pathlib import Path


# ── Section markers ──
SECTION_MARKERS = {
    '필드 상세 설명': '## 필드 상세',
    '필드 상세설명': '## 필드 상세',
    '메쏘드 상세 설명': '## 메서드 상세',
    '메쏘드 상세설명': '## 메서드 상세',
    '메소드 상세 설명': '## 메서드 상세',
    '메소드 상세설명': '## 메서드 상세',
    '생성자 상세 설명': '## 생성자 상세',
    '생성자 상세설명': '## 생성자 상세',
}

SECTION_MARKER_RE = re.compile(
    '(' + '|'.join(re.escape(k) for k in sorted(SECTION_MARKERS.keys(), key=len, reverse=True)) + ')'
)

# Match "Methods inherited from class pkg.ClassName" and capture the method list
# The method list is comma-separated words, ending before a section marker or
# a class/interface header or another sentence.
INHERITED_RE = re.compile(
    r'Methods inherited from class ([\w.]+)\s+'
    r'([\w]+(?:,\s*[\w]+)*)'
)

# Method/constructor signature
METHOD_SIG_RE = re.compile(
    r'((?:public|protected|private)'
    r'(?:\s+static)?'
    r'(?:\s+(?:abstract|final|native|synchronized))*'
    r'(?:\s+[\w.\[\]<>]+)?'  # return type (absent for constructors)
    r'\s+(\w+)\s*'
    r'\(([^)]*)\))'
    r'(\s+throws\s+[\w.,\s]+?)?'
    r'(?=\s|$)'
)

# Field declaration (no parentheses)
FIELD_DECL_RE = re.compile(
    r'((?:public|protected|private)'
    r'(?:\s+static)?'
    r'(?:\s+final)?'
    r'\s+[\w.\[\]<>]+\s+\w+)'
    r'(?:\s+(.*))?$',
    re.DOTALL
)

# Class/Interface header with hierarchy (e.g., "Class Kernel java.lang.Object | +--...")
CLASS_IFACE_HIER_RE = re.compile(
    r'(Class|Interface)\s+(\w+)\s+'
    r'((?:java|org)\.[\w.]+(?:\s*\|\s*\+--[\w.]+)+)'
)

# Class/Interface header without hierarchy (e.g., "Interface ImageObserver public interface...")
CLASS_IFACE_SIMPLE_RE = re.compile(
    r'(Class|Interface)\s+(\w+)\s+'
    r'((?:public|protected|private)(?:\s+(?:abstract|static|final))*'
    r'\s+(?:class|interface)\s+\w+)'
)

# Combined: try hierarchy first, then simple
def match_class_iface(text, pos=0):
    """Try to match a Class/Interface header, with or without hierarchy."""
    m = CLASS_IFACE_HIER_RE.search(text, pos)
    if m:
        return m, True  # has hierarchy
    m = CLASS_IFACE_SIMPLE_RE.search(text, pos)
    if m:
        return m, False  # no hierarchy
    return None, False

# "name public [static] type name(...)" pattern -- method name prefixed before signature
NAME_SIG_RE = re.compile(
    r'(\w+)\s+'
    r'((?:public|protected|private)'
    r'(?:\s+static)?'
    r'(?:\s+(?:abstract|final|native|synchronized))*'
    r'(?:\s+[\w.\[\]<>]+)?'
    r'\s+\1\s*'
    r'\(([^)]*)\))'
    r'(\s+throws\s+[\w.,\s]+?)?'
    r'(?=\s|$)'
)


def parse_frontmatter(text):
    if text.startswith('---'):
        end = text.find('---', 3)
        if end != -1:
            end += 3
            return text[:end], text[end:].lstrip('\n')
    return '', text


def split_hierarchy(raw):
    parts = re.split(r'\s*\|\s*', raw.strip())
    lines = []
    for i, part in enumerate(parts):
        lines.append('  ' * i + part)
    return '\n'.join(lines)


def split_text(text):
    """
    Split text into typed segments. Each segment is (type, content).
    Types: 'text', 'class', 'method', 'field', 'section', 'inherited'
    """
    segments = []
    remaining = text.strip()

    while remaining:
        remaining = remaining.strip()
        if not remaining:
            break

        best_match = None
        best_pos = len(remaining)
        best_type = None

        # Find earliest Class/Interface header
        ci_m = CLASS_IFACE_RE.search(remaining)
        if ci_m and ci_m.start() < best_pos:
            best_pos = ci_m.start()
            best_match = ci_m
            best_type = 'class'

        # Find earliest section marker
        sm_m = SECTION_MARKER_RE.search(remaining)
        if sm_m and sm_m.start() < best_pos:
            best_pos = sm_m.start()
            best_match = sm_m
            best_type = 'section'

        # Find earliest name+sig pattern
        ns_m = NAME_SIG_RE.search(remaining)
        if ns_m and ns_m.start() < best_pos:
            best_pos = ns_m.start()
            best_match = ns_m
            best_type = 'name_sig'

        # Find earliest standalone method signature (only if no name+sig found at same pos)
        sig_m = METHOD_SIG_RE.search(remaining)
        if sig_m and sig_m.start() < best_pos:
            best_pos = sig_m.start()
            best_match = sig_m
            best_type = 'method'

        if best_match is None:
            # No patterns found -- all plain text
            segments.append(('text', remaining))
            break

        # Add any text before the match
        if best_pos > 0:
            before = remaining[:best_pos].strip()
            if before:
                segments.append(('text', before))

        if best_type == 'class':
            # Consume from here to the end (class header can contain lots of stuff)
            class_text = remaining[best_pos:]
            segments.append(('class', class_text))
            break  # class consumes rest

        elif best_type == 'section':
            marker = best_match.group(1)
            segments.append(('section', marker))
            remaining = remaining[best_match.end():].strip()
            continue

        elif best_type == 'name_sig':
            name = best_match.group(1)
            sig = best_match.group(2).strip()
            throws = (best_match.group(4) or '').strip()
            segments.append(('method', {'name': name, 'sig': sig, 'throws': throws}))
            remaining = remaining[best_match.end():].strip()
            continue

        elif best_type == 'method':
            sig = best_match.group(1).strip()
            name = best_match.group(2)
            throws = (best_match.group(4) or '').strip()
            segments.append(('method', {'name': name, 'sig': sig, 'throws': throws}))
            remaining = remaining[best_match.end():].strip()
            continue

    return segments


def format_class_text(text):
    """Format a Class/Interface header block. Returns list of output lines."""
    output = []

    # Try with hierarchy first
    ci_m = CLASS_IFACE_HIER_RE.match(text)
    has_hier = ci_m is not None

    if not ci_m:
        ci_m = CLASS_IFACE_SIMPLE_RE.match(text)

    if not ci_m:
        return [text]

    ci_type = ci_m.group(1)
    class_name = ci_m.group(2)
    rest = text[ci_m.end():].strip()

    output.append(f'\n---\n\n## {ci_type} {class_name}\n')

    if has_hier:
        hierarchy = ci_m.group(3)
        output.append(f'```text\n{split_hierarchy(hierarchy)}\n```\n')
    else:
        # group(3) is the declaration for simple form; prepend it to rest
        rest = ci_m.group(3) + ' ' + rest

    # Direct Known Subclasses
    dks = re.match(r'(Direct Known Subclasses:\s*[\w,\s]+?)\s+(All\s|public|protected|private|abstract)', rest)
    if dks:
        output.append(f'*{dks.group(1).strip()}*\n')
        rest = rest[dks.start(2):]

    # All Implemented Interfaces
    aii = re.match(r'(All Implemented Interfaces:\s*[\w.,\s]+?)\s+(public|protected|private|abstract)', rest)
    if aii:
        output.append(f'*{aii.group(1).strip()}*\n')
        rest = rest[aii.start(2):]

    # Class declaration
    decl = re.match(
        r'((?:public|protected|private)(?:\s+(?:abstract|static|final))*'
        r'\s+(?:class|interface)\s+\w+(?:\s+extends\s+[\w.]+)?'
        r'(?:\s+implements\s+[\w.,\s]+?)?)'
        r'(?:\s+|$)',
        rest
    )
    if decl:
        output.append(f'```java\n{decl.group(1).strip()}\n```\n')
        rest = rest[decl.end():].strip()

    # Description + inherited methods
    # Find ALL "Methods inherited from class ..." blocks
    inherited_parts = []
    desc_text = rest

    while True:
        inh_m = INHERITED_RE.search(desc_text)
        if not inh_m:
            break

        before = desc_text[:inh_m.start()].strip()
        if before:
            output.append(f'{before}\n')

        inherited_parts.append(f'*Methods inherited from class {inh_m.group(1)}: {inh_m.group(2)}*')
        desc_text = desc_text[inh_m.end():].strip()

    for ip in inherited_parts:
        output.append(f'{ip}\n')

    # Process what's left (section markers, methods, constructors, more classes)
    if desc_text:
        processed = process_inline_text(desc_text)
        output.append(processed)

    return output


def process_inline_text(text):
    """
    Process text that may contain section markers, method signatures,
    class headers, etc., all concatenated together.
    Returns formatted markdown string.
    """
    if not text.strip():
        return ''

    output_parts = []
    remaining = text.strip()

    while remaining:
        remaining = remaining.strip()
        if not remaining:
            break

        # 1. Check for Class/Interface header (with or without hierarchy)
        ci_m, _ = match_class_iface(remaining)
        if ci_m:
            before = remaining[:ci_m.start()].strip()
            if before:
                output_parts.append(process_plain_text(before))
            output_parts.extend(format_class_text(remaining[ci_m.start():]))
            break  # class text consumes the rest

        # 2. Check for section markers
        sm_m = SECTION_MARKER_RE.search(remaining)
        if sm_m:
            before = remaining[:sm_m.start()].strip()
            if before:
                output_parts.append(process_plain_text(before))
            marker = sm_m.group(1)
            output_parts.append(f'\n{SECTION_MARKERS[marker]}\n')
            remaining = remaining[sm_m.end():].strip()
            continue

        # 3. Check for name+sig pattern: "methodName public type methodName(...)"
        ns_m = NAME_SIG_RE.search(remaining)
        if ns_m:
            before = remaining[:ns_m.start()].strip()
            if before:
                output_parts.append(process_plain_text(before))

            name = ns_m.group(1)
            sig = ns_m.group(2).strip()
            throws = (ns_m.group(4) or '').strip()

            block = f'\n### {name}\n\n```java\n{sig}'
            if throws:
                block += f' {throws}'
            block += '\n```\n'
            output_parts.append(block)

            remaining = remaining[ns_m.end():].strip()
            continue

        # 4. Check for standalone method signature
        sig_m = METHOD_SIG_RE.search(remaining)
        if sig_m:
            before = remaining[:sig_m.start()].strip()
            if before:
                # Check if 'before' ends with the method name
                name = sig_m.group(2)
                if before.endswith(name):
                    desc_before = before[:-len(name)].rstrip()
                    if desc_before:
                        output_parts.append(process_plain_text(desc_before))
                    # Treat as name+sig
                    sig = sig_m.group(1).strip()
                    throws = (sig_m.group(4) or '').strip()
                    block = f'\n### {name}\n\n```java\n{sig}'
                    if throws:
                        block += f' {throws}'
                    block += '\n```\n'
                    output_parts.append(block)
                    remaining = remaining[sig_m.end():].strip()
                    continue
                else:
                    output_parts.append(process_plain_text(before))

            sig = sig_m.group(1).strip()
            name = sig_m.group(2)
            throws = (sig_m.group(4) or '').strip()

            block = f'```java\n{sig}'
            if throws:
                block += f' {throws}'
            block += '\n```\n'
            output_parts.append(block)

            remaining = remaining[sig_m.end():].strip()
            continue

        # 5. No patterns - plain text
        output_parts.append(process_plain_text(remaining))
        break

    return '\n'.join(output_parts)


def process_plain_text(text):
    """Process text that has no embedded Java signatures or class headers."""
    text = text.strip()
    if not text:
        return ''

    # Check for field declaration
    field_m = FIELD_DECL_RE.match(text)
    if field_m and '(' not in field_m.group(1):
        decl = field_m.group(1).strip()
        desc = (field_m.group(2) or '').strip()
        result = f'```java\n{decl}\n```'
        if desc:
            result += f'\n\n{desc}'
        return result

    return text


def process_bullet_line(line):
    """
    Handle bullet-point lines that may contain mangled method signatures.
    e.g. "- `public` - static int getAccessLevel() description..."
    """
    stripped = line.strip()

    # Pattern: "- `public` - static type methodName(...) description"
    # This happens when PDF extraction put a method signature inside a param list
    m = re.match(
        r'^- `(public|protected|private)` - (static\s+)?(.+)$',
        stripped
    )
    if m:
        access = m.group(1)
        static = (m.group(2) or '').strip()
        rest_text = m.group(3).strip()

        # Try to reconstruct: "public static rest_text"
        reconstructed = f'{access}'
        if static:
            reconstructed += f' {static}'
        reconstructed += f' {rest_text}'

        # Check if this looks like a method signature
        sig_m = METHOD_SIG_RE.match(reconstructed)
        if sig_m:
            sig = sig_m.group(1).strip()
            name = sig_m.group(2)
            throws = (sig_m.group(4) or '').strip()
            body = reconstructed[sig_m.end():].strip()

            result = f'\n### {name}\n\n```java\n{sig}'
            if throws:
                result += f' {throws}'
            result += '\n```\n'
            if body:
                result += f'\n{body}'
            return result

    # Pattern: "- `paramName` - description methodName"
    # where the trailing methodName is a method name prefix for the next concatenated method
    # We can't split this reliably without seeing the next line, so leave as-is
    return line


def reformat_file(filepath):
    """Read, process, and write back a single file."""
    content = filepath.read_text(encoding='utf-8')
    frontmatter, body = parse_frontmatter(content)

    lines = body.split('\n')
    output = []

    if frontmatter:
        output.append(frontmatter)
        output.append('')

    i = 0
    in_code_block = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track existing code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            output.append(line)
            i += 1
            continue

        if in_code_block:
            output.append(line)
            i += 1
            continue

        # #### headings -> ### headings
        if stripped.startswith('#### '):
            heading_name = stripped[5:].strip()
            output.append(f'\n### {heading_name}')
            output.append('')
            i += 1
            continue

        # Bold section headers
        if stripped in ('**매개 변수**', '**반환 값**', '**참고 항목**', '**설명**'):
            output.append('')
            output.append(line)
            output.append('')
            i += 1
            continue

        # Bullet points
        if stripped.startswith('- `'):
            processed = process_bullet_line(stripped)
            output.append(processed)
            i += 1
            continue

        if stripped.startswith('- '):
            output.append(line)
            i += 1
            continue

        # Empty lines
        if not stripped:
            output.append('')
            i += 1
            continue

        # Regular text - process for embedded Java patterns
        processed = process_inline_text(stripped)
        output.append(processed)
        i += 1

    result = '\n'.join(output)

    # Clean up
    result = re.sub(r'\n{3,}', '\n\n', result)
    if not result.endswith('\n'):
        result += '\n'

    filepath.write_text(result, encoding='utf-8')


def main():
    if len(sys.argv) < 2:
        target_dir = Path('/Users/seongjinkim/lab/wipi-wiki/src/content/docs/v22/java-api')
    else:
        target_dir = Path(sys.argv[1])

    if not target_dir.is_dir():
        print(f'Error: {target_dir} is not a directory', file=sys.stderr)
        sys.exit(1)

    md_files = sorted(target_dir.glob('*.md'))
    count = 0
    for f in md_files:
        if f.name == 'index.md':
            continue
        print(f'Processing {f.name}...')
        reformat_file(f)
        print(f'  Done.')
        count += 1

    print(f'\nProcessed {count} files.')


if __name__ == '__main__':
    main()
