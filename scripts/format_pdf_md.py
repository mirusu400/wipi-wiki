#!/usr/bin/env python3
"""
Postprocess PDF-extracted Markdown for readability.

Input files come from scripts/extract_pdf.py. Each line of the PDF is dumped
as-is which produces:
  - Korean paragraphs broken mid-line at PDF column edges
  - "?" glyphs in place of bullet/diamond markers
  - Sub-section labels (프로토타입 / 설명 / 매개 변수 / ...) on their own
    line, followed by content
  - C prototypes / example snippets mixed in as plain text

This script rewrites those files in place:
  - Joins broken Korean paragraph lines
  - Converts "? Name" API entry markers to "### Name" headings
  - Recognizes standalone identifier lines as API entry headings
  - Detects short Korean concept headings and promotes to "### Heading"
  - Wraps prototype blocks and surrounding C-style lines in ```c fences
  - Renders the standard subsection labels as bold lines
  - Converts "? <Korean text>" bullets in body prose to "- <text>" bullets
  - Formats `param - desc` lines under 매개 변수 as bullet list items

Usage:
    python3 scripts/format_pdf_md.py docs/c-api docs/hal docs/overview docs/appendix
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


# Labels that delimit subsections within an API entry.
LABELS = {
    "프로토타입": "프로토타입",
    "설명": "설명",
    "매개 변수": "매개 변수",
    "매개변수": "매개 변수",
    "반환 값": "반환 값",
    "반환값": "반환 값",
    "리턴 값": "반환 값",
    "리턴값": "반환 값",
    "부작용": "부작용",
    "참고 항목": "참고 항목",
    "비고": "비고",
    "예제": "예제",
    "에러": "에러",
    "에러 코드": "에러 코드",
}

API_MARKER_RE = re.compile(r"^\?\s+([A-Za-z_][\w]*)\s*$")
BULLET_QMARK_RE = re.compile(r"^[\?\u25a0\u25c6]\s+(.+)$")
BARE_IDENT_RE = re.compile(r"^[A-Z_][A-Z0-9_]{3,}$")
PARAM_LINE_RE = re.compile(r"^([A-Za-z_][\w]*)\s*[-\u2013]\s*(.+)$")
SENTENCE_END_RE = re.compile(r"[.?!]\s*$|다\.\s*$|요\.\s*$|음\.\s*$|니다\.\s*$")
HANGUL_RE = re.compile(r"[가-힣]")
LATIN_RE = re.compile(r"[A-Za-z0-9]")

C_DECL_START = re.compile(
    r"^(typedef|struct|union|enum|#define|#include|extern|static|const)\b"
)
C_CONTROL_START = re.compile(
    r"^(if|else|for|while|do|switch|case|return|break|continue)\b"
)
C_TYPE_DECL = re.compile(
    r"^(void|int|char|float|double|long|short|unsigned|signed|M_\w+)\s+\*?\w+\s*[\(=;\[]"
)
C_FUNC_CALL_START = re.compile(
    r"^(MC_|MH_|M_[A-Z]|DECLARE_|strcpy|strcat|strcmp|strlen|memcpy|memset|sprintf|printf)\w*\s*\([^)]*\)\s*[;{]"
)


def is_subheading_kr(s: str) -> bool:
    if len(s) == 0 or len(s) > 25:
        return False
    if any(c in s for c in "().,;:=[]{}?!\"'"):
        return False
    if SENTENCE_END_RE.search(s):
        return False
    return bool(HANGUL_RE.search(s))


def is_code_like(s: str) -> bool:
    if re.match(r"^\s*(//|/\*|\*/)", s):
        return True
    if re.match(r"^[\{\}]\s*$", s):
        return True
    if C_DECL_START.match(s):
        return True
    if re.search(r";\s*$", s):
        return True
    if C_TYPE_DECL.match(s):
        return True
    if C_FUNC_CALL_START.match(s):
        return True
    if C_CONTROL_START.match(s) and ("(" in s or "{" in s):
        return True
    # Bare assignment statement
    if re.match(r"^[A-Za-z_]\w*\s*=\s*", s) and not HANGUL_RE.search(s):
        return True
    return False


def join_paragraph(lines: list[str]) -> str:
    if not lines:
        return ""
    out = lines[0]
    for nxt in lines[1:]:
        if not nxt:
            continue
        if not out:
            out = nxt
            continue
        sep = "" if out.endswith(("(", "[", "‘", "“")) else " "
        out += sep + nxt
    return out


def format_text(raw: str) -> str:
    out: list[str] = []
    para: list[str] = []
    in_code = False
    code_lang = "c"
    current_label: str | None = None
    proto_active = False  # inside 프로토타입 label

    def open_code(lang: str = "c") -> None:
        nonlocal in_code, code_lang
        if not in_code:
            out.append(f"```{lang}")
            in_code = True
            code_lang = lang

    def close_code() -> None:
        nonlocal in_code, proto_active
        if in_code:
            out.append("```")
            out.append("")
            in_code = False
            proto_active = False

    def flush_para() -> None:
        nonlocal para
        if para:
            joined = join_paragraph(para)
            if joined.strip():
                out.append(joined)
                out.append("")
            para = []

    def emit_blank() -> None:
        if out and out[-1] != "":
            out.append("")

    lines = raw.split("\n")
    for raw_line in lines:
        stripped = raw_line.rstrip()
        s = stripped.strip()

        # Markdown header (from extract_pdf.py) — pass through.
        # Note: must be "# " with space — exclude C preprocessor #define/#include.
        if re.match(r"^#{1,6} ", stripped):
            flush_para()
            close_code()
            emit_blank()
            out.append(stripped)
            out.append("")
            current_label = None
            continue

        # Blank line
        if not s:
            flush_para()
            close_code()
            current_label = None
            continue

        # API entry marker "? Name"
        m = API_MARKER_RE.match(s)
        if m:
            flush_para()
            close_code()
            emit_blank()
            out.append(f"### {m.group(1)}")
            out.append("")
            current_label = None
            continue

        # Subsection label
        if s in LABELS:
            label = LABELS[s]
            flush_para()
            close_code()
            current_label = label
            out.append(f"**{label}**")
            out.append("")
            if label == "프로토타입":
                proto_active = True
                open_code("c")
            continue

        # Inside prototype block — everything is code until label/blank/marker
        if proto_active:
            out.append(s)
            continue

        # Bare identifier line as API name (no '?')
        if BARE_IDENT_RE.match(s) and current_label is None:
            close_code()
            flush_para()
            emit_blank()
            out.append(f"### {s}")
            out.append("")
            continue

        # Short Korean concept heading. In code mode, only accept it if the
        # previous line closes a brace ("}") — otherwise the line is a
        # Korean comment fragment continuing the example.
        if current_label is None and is_subheading_kr(s):
            prev = out[-1].strip() if out else ""
            if not in_code or prev == "}":
                close_code()
                flush_para()
                emit_blank()
                out.append(f"### {s}")
                out.append("")
                continue

        # Body bullet that was originally a '?' diamond/bullet
        bm = BULLET_QMARK_RE.match(s)
        if bm and not BARE_IDENT_RE.match(bm.group(1).split()[0] if bm.group(1) else ""):
            flush_para()
            close_code()
            out.append(f"- {bm.group(1)}")
            continue

        # Parameter line under 매개 변수
        if current_label == "매개 변수":
            pm = PARAM_LINE_RE.match(s)
            if pm:
                flush_para()
                close_code()
                out.append(f"- `{pm.group(1)}` — {pm.group(2)}")
                continue

        # Code-like statement / declaration
        if is_code_like(s):
            flush_para()
            open_code("c")
            out.append(s)
            continue

        # Inside an ongoing code block: keep the line in the block unless it
        # is unmistakably prose (Korean text with a sentence terminator).
        # The PDF-extracted code examples have wrapped Korean comments,
        # ellipses, and stand-alone identifiers scattered through them, and
        # they belong in the same fence; only a complete Korean sentence
        # signals the prose has resumed.
        if in_code:
            if HANGUL_RE.search(s) and SENTENCE_END_RE.search(s):
                close_code()
                # fall through to paragraph handling
            else:
                out.append(s)
                continue

        # Default: accumulate paragraph
        para.append(s)
        if SENTENCE_END_RE.search(s):
            flush_para()

    flush_para()
    close_code()

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    total = 0
    for arg in argv[1:]:
        root = Path(arg)
        if not root.exists():
            print(f"skip missing: {root}", file=sys.stderr)
            continue
        targets = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for md in targets:
            if md.suffix != ".md":
                continue
            # Skip hand-written index pages — they already use markdown tables
            # and other syntax that should not be re-flowed.
            if md.name == "index.md":
                continue
            original = md.read_text(encoding="utf-8")
            formatted = format_text(original)
            if formatted != original:
                md.write_text(formatted, encoding="utf-8")
                total += 1
                print(f"reformatted {md}")
    print(f"\nupdated {total} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
