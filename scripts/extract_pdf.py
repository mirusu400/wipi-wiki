#!/usr/bin/env python3
"""
Extract WIPI 1.2.1 PDF into section-split Markdown files.

Usage:
    python3 scripts/extract_pdf.py <pdf_path> <docs_dir>

Splits the spec into per-section Markdown files according to SECTION_MAP.
Skips the Java 5.2.x sections — the richer JavaDoc-derived Markdown
already lives under docs/java-api/.

Uses pdfplumber (which embeds pdfminer.six) so Adobe-Korea1 CID fonts
decode correctly without requiring system poppler-data.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pdfplumber


SECTION_MAP: dict[str, str] = {
    "1":      "overview/introduction.md",
    "2":      "overview/architecture.md",
    "3":      "overview/platform.md",
    "4.1":    "hal/types.md",
    "4.2":    "hal/platform-api.md",
    "4.3":    "hal/system.md",
    "4.4":    "hal/call.md",
    "4.5":    "hal/handset.md",
    "4.6":    "hal/network.md",
    "4.7":    "hal/serial.md",
    "4.8":    "hal/media.md",
    "4.9":    "hal/time.md",
    "4.10":   "hal/utility.md",
    "4.11":   "hal/file.md",
    "4.12":   "hal/input-method.md",
    "4.13":   "hal/font.md",
    "4.14":   "hal/frame-buffer.md",
    "4.15":   "hal/virtual-key.md",
    "5.1.1":  "c-api/kernel.md",
    "5.1.2":  "c-api/graphics.md",
    "5.1.3":  "c-api/database.md",
    "5.1.4":  "c-api/filesystem.md",
    "5.1.5":  "c-api/network.md",
    "5.1.6":  "c-api/media.md",
    "5.1.7":  "c-api/serial.md",
    "5.1.8":  "c-api/phone.md",
    "5.1.9":  "c-api/misc.md",
    "5.1.10": "c-api/utility.md",
    "5.1.11": "c-api/ui-components.md",
    "5.1.12": "c-api/c-stdlib.md",
    "6":      "appendix/references.md",
    "7.1":    "appendix/euc-kr-extended.md",
    "7.2":    "appendix/api-management.md",
    "7.3":    "appendix/security.md",
    "7.4":    "appendix/media-ext.md",
}

# Order matters: we advance through the body in the order the sections
# appear so spurious matches (e.g. an in-text "1." numbered list) do
# not cause a false section transition.
SEQUENCE: list[str] = list(SECTION_MAP.keys())

# Chapter / umbrella headers that close the previous mapped section but
# produce no file of their own.
UMBRELLA: set[str] = {"4", "5", "5.1", "5.2", "7"}

HEADER_RE = re.compile(r"^(모바일 표준 플랫폼 규격|무선 인터넷 표준화 포럼)")
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)*)\.\s+(\S.*?)\s*$")
PAGENUM_RE = re.compile(r"^\d{1,4}$")

# TOC and cover live in the first six pages.
BODY_START_PAGE = 6  # 0-based index


def is_subsection_of(num: str, parent: str) -> bool:
    return num.startswith(parent + ".")


def extract(pdf_path: Path, out_dir: Path) -> None:
    buffers: dict[str, list[str]] = {k: [] for k in SECTION_MAP}
    titles: dict[str, str] = {}
    current: str | None = None
    ptr = 0  # index into SEQUENCE — next expected mapped section

    with pdfplumber.open(str(pdf_path)) as pdf:
        for pg_idx, page in enumerate(pdf.pages):
            if pg_idx < BODY_START_PAGE:
                continue
            text = page.extract_text() or ""
            for raw in text.split("\n"):
                stripped = raw.strip()
                if not stripped:
                    if current:
                        buffers[current].append("")
                    continue
                if HEADER_RE.match(stripped):
                    continue
                if PAGENUM_RE.match(stripped):
                    continue

                m = SECTION_RE.match(stripped)
                if m:
                    num, title = m.group(1), m.group(2)

                    if num in UMBRELLA:
                        current = None
                        continue

                    if ptr < len(SEQUENCE) and num == SEQUENCE[ptr]:
                        current = num
                        titles[current] = title
                        buffers[current] = [f"# {num}. {title}", ""]
                        ptr += 1
                        continue

                    if current and is_subsection_of(num, current):
                        depth = num.count(".") - current.count(".")
                        level = min(depth + 1, 5)
                        buffers[current].append("")
                        buffers[current].append(f"{'#' * level} {num}. {title}")
                        buffers[current].append("")
                        continue
                    # Otherwise: numeric-looking but not a transition.
                    # Treat as content if a section is active.

                if current:
                    buffers[current].append(stripped)

    for key, rel in SECTION_MAP.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if not buffers[key]:
            body = f"# {key}.\n\n_본문이 추출되지 않았습니다._\n"
        else:
            lines = buffers[key]
            # Collapse runs of >2 blank lines
            collapsed: list[str] = []
            blanks = 0
            for line in lines:
                if line == "":
                    blanks += 1
                    if blanks <= 1:
                        collapsed.append(line)
                else:
                    blanks = 0
                    collapsed.append(line)
            body = "\n".join(collapsed).rstrip() + "\n"
        path.write_text(body, encoding="utf-8")
        print(f"wrote {rel}  ({len(body)} bytes)")


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    pdf_path = Path(argv[1])
    out_dir = Path(argv[2])
    if not pdf_path.is_file():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    extract(pdf_path, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
