#!/usr/bin/env python3
"""
Extract WIPI 2.2.0 PDF into section-split Markdown files.

Usage:
    python3 scripts/extract_pdf_v2.py <pdf_path> <docs_v2_dir>

The 2.2.0 spec is split into 편 (parts) with independent section numbering.
This script tracks 편 boundaries to disambiguate identical section numbers
across parts.

Uses pdfplumber (which embeds pdfminer.six) so Adobe-Korea1 CID fonts
decode correctly without requiring system poppler-data.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pdfplumber


# ---------------------------------------------------------------------------
# 편 definitions: (title_keyword, start_page_0idx, end_page_0idx_exclusive)
# Pages are 0-indexed PDF pages.
# ---------------------------------------------------------------------------
PARTS = [
    ("제1편", 10, 27),    # 규격 구조 및 기능
    ("제2편", 27, 278),   # HAL API
    ("제3편", 278, 790),  # C API
    ("제4편", 790, 1254), # Java API
    ("제5편", 1254, 1321),# 선택 규격
    ("부속서", 1321, 1356),
]

# ---------------------------------------------------------------------------
# Section map per 편.  Keys are "편idx:section_num".
# The section_num is the number as it appears in the PDF text.
# ---------------------------------------------------------------------------
SECTION_MAP: dict[str, str] = {
    # 제1편: 규격 구조 및 기능
    "0:1":     "overview/introduction.md",
    "0:2":     "overview/architecture.md",
    "0:3":     "overview/platform.md",
    "0:4":     "overview/references.md",

    # 제2편: HAL API
    "1:2.1":   "hal/types.md",
    "1:2.2":   "hal/platform-api.md",
    "1:2.3":   "hal/system.md",
    "1:2.4":   "hal/timer.md",
    "1:2.5":   "hal/unicode.md",
    "1:2.6":   "hal/font.md",
    "1:2.7":   "hal/input-method.md",
    "1:2.8":   "hal/virtual-key.md",
    "1:2.9":   "hal/generic-io.md",
    "1:2.10":  "hal/terminal-resource.md",
    "1:2.11":  "hal/call.md",
    "1:2.12":  "hal/handset.md",
    "1:2.13":  "hal/lcd.md",
    "1:2.14":  "hal/file.md",
    "1:2.15":  "hal/network.md",
    "1:2.16":  "hal/serial.md",
    "1:2.17":  "hal/media.md",
    "1:2.18":  "hal/sms.md",

    # 제3편: C API
    "2:2.1":   "c-api/kernel.md",
    "2:2.2":   "c-api/graphics.md",
    "2:2.3":   "c-api/filesystem.md",
    "2:2.4":   "c-api/database.md",
    "2:2.5":   "c-api/network.md",
    "2:2.6":   "c-api/serial.md",
    "2:2.7":   "c-api/ui-components.md",
    "2:2.8":   "c-api/utility.md",
    "2:2.9":   "c-api/generic-io.md",
    "2:2.10":  "c-api/terminal-resource.md",
    "2:2.11":  "c-api/media.md",
    "2:2.12":  "c-api/phone.md",
    "2:2.13":  "c-api/sms.md",
    "2:2.14":  "c-api/security.md",
    "2:2.15":  "c-api/device-control.md",
    "2:2.16":  "c-api/math.md",
    "2:3":     "c-api/c-stdlib.md",

    # 제4편: Java API
    "3:2.2.1": "java-api/kernel.md",
    "3:2.2.2": "java-api/low-level-io.md",
    "3:3.1.1": "java-api/graphics.md",
    "3:3.1.2": "java-api/file.md",
    "3:3.1.3": "java-api/database.md",
    "3:3.1.4": "java-api/ui.md",
    "3:3.1.5": "java-api/generic-io.md",
    "3:3.1.6": "java-api/terminal-resource.md",
    "3:3.1.7": "java-api/media.md",
    "3:3.1.8": "java-api/sms.md",
    "3:3.1.9": "java-api/device-control.md",
    "3:4.1":   "java-api/unicode.md",

    # 제5편: 선택 규격
    "4:1":     "optional/dynamic-api.md",
    "4:2":     "optional/vgi.md",

    # 부속서
    "5:1":     "appendix/api-interop.md",
    "5:2":     "appendix/security-policy.md",
    "5:3":     "appendix/error-codes.md",
    "5:4":     "appendix/examples.md",
    "5:5":     "appendix/wcard.md",
}

# Ordered sequence per 편 index
SEQUENCES: dict[int, list[str]] = {}
for key in SECTION_MAP:
    pidx_str, secnum = key.split(":", 1)
    pidx = int(pidx_str)
    SEQUENCES.setdefault(pidx, []).append(secnum)

# Umbrella sections per 편 (close previous but produce no file)
UMBRELLAS: dict[int, set[str]] = {
    1: {"1", "2"},           # HAL: "1. HAL 개념 정의", "2. HAL 규격"
    2: {"1", "2"},           # C API: "1. 필수 C API 개요", "2. C API"
    3: {"1", "2", "2.1", "2.2", "3", "3.1", "3.2", "4"},  # Java API
    4: set(),
    5: set(),
    0: set(),
}

HEADER_RE = re.compile(
    r"^(모바일\s*표준\s*플랫폼\s*규격|"
    r"한국\s*무선\s*인터넷\s*표준화\s*포럼|"
    r"정보통신단체표준|"
    r"TTAK\.KO|TTAS\.KO|"
    r"Wireless Internet Platform)"
)
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)*)\.\s+(\S.*?)\s*$")
PAGENUM_RE = re.compile(r"^\d{1,4}$")
# TOC dot-leader lines like "2.1. 변수 타입 .........................2"
TOC_DOTS_RE = re.compile(r"\.{4,}")


def is_subsection_of(num: str, parent: str) -> bool:
    return num.startswith(parent + ".")


def get_part_index(pg_idx: int) -> int | None:
    """Return the 편 index for a given 0-based page index."""
    for i, (_, start, end) in enumerate(PARTS):
        if start <= pg_idx < end:
            return i
    return None


def extract(pdf_path: Path, out_dir: Path) -> None:
    buffers: dict[str, list[str]] = {k: [] for k in SECTION_MAP}
    titles: dict[str, str] = {}
    current: str | None = None  # full key like "2:2.3"
    current_sec: str | None = None  # just the section number
    ptrs: dict[int, int] = {i: 0 for i in range(len(PARTS))}
    active_part: int | None = None

    with pdfplumber.open(str(pdf_path)) as pdf:
        for pg_idx, page in enumerate(pdf.pages):
            part_idx = get_part_index(pg_idx)
            if part_idx is None:
                continue

            if part_idx != active_part:
                active_part = part_idx
                current = None
                current_sec = None

            text = page.extract_text() or ""
            seq = SEQUENCES.get(part_idx, [])
            ptr = ptrs[part_idx]
            umbrellas = UMBRELLAS.get(part_idx, set())

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
                if TOC_DOTS_RE.search(stripped):
                    continue

                m = SECTION_RE.match(stripped)
                if m:
                    num, title = m.group(1), m.group(2)

                    if num in umbrellas:
                        current = None
                        current_sec = None
                        continue

                    full_key = f"{part_idx}:{num}"
                    if ptr < len(seq) and num == seq[ptr]:
                        current = full_key
                        current_sec = num
                        titles[current] = title
                        buffers[current] = [f"# {num}. {title}", ""]
                        ptr += 1
                        ptrs[part_idx] = ptr
                        continue

                    if current_sec and is_subsection_of(num, current_sec):
                        depth = num.count(".") - current_sec.count(".")
                        level = min(depth + 1, 5)
                        buffers[current].append("")
                        buffers[current].append(f"{'#' * level} {num}. {title}")
                        buffers[current].append("")
                        continue

                if current:
                    buffers[current].append(stripped)

    for key, rel in SECTION_MAP.items():
        path = out_dir / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if not buffers[key]:
            pidx_str, secnum = key.split(":", 1)
            body = f"# {secnum}.\n\n_본문이 추출되지 않았습니다._\n"
        else:
            lines = buffers[key]
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
