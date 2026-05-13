#!/usr/bin/env python3
"""
Extract CLDC 1.1 Korean PDF specification to a single Markdown file.

The CLDC PDF is short (~58 pages) and has a clear chapter structure:
  머리말 / 1. 소개 / 2. 목표 / 3. 높은 수준의 구조 / 4. Java 언어 규격 유지 /
  5. Java 가상 머신 규격 유지 / 6. CLDC 라이브러리 / A. 부록

The first 3 pages are an English cover + license — we skip them. The remainder
is post-processed to:
  - drop running headers / page numbers
  - promote chapter / sub-chapter numbers to Markdown headings
  - merge lines that the PDF wrapped mid-sentence (Korean)

Usage:
    python3 scripts/extract_cldc_pdf.py vendor/cldc-1_1-fr-spec-ko/CLDCSpecification1.1.pdf docs/cldc/spec.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pdfplumber


PAGE_HEADER_RE = re.compile(
    r"^(Connected Limited Device Configuration|CLDC|J2ME|"
    r"\d+\s+Connected Limited Device Configuration|"
    r"Connected Limited Device Configuration\s+.*2003년)"
)
PAGE_NUM_RE = re.compile(r"^\d{1,3}$")
ROMAN_PAGE_RE = re.compile(r"^[ivxlcm]+$", re.IGNORECASE)
CHAPTER_RE = re.compile(r"^(\d+)\s+([^\d].+)$")
SUBCHAPTER_RE = re.compile(r"^(\d+\.\d+(?:\.\d+)?)\s+([^\d].+)$")
APPENDIX_RE = re.compile(r"^([A-Z])\.\s+(.+)$")
HANGUL_RE = re.compile(r"[가-힣]")


def is_noise(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if PAGE_NUM_RE.match(s) or ROMAN_PAGE_RE.match(s):
        return True
    if PAGE_HEADER_RE.match(s):
        return True
    if "(cid:" in s:
        return True
    return False


def clean_text(t: str) -> str:
    # Replace pdfplumber's (cid:127) (bullet dot) etc
    return re.sub(r"\(cid:\d+\)", "·", t)


def looks_like_heading(s: str) -> tuple[int, str] | None:
    """Return (level, title) if s is a heading."""
    # 5.2.1.1 ... (4-level)
    m = re.match(r"^(\d+\.\d+\.\d+\.\d+)\s+(\S.*)$", s)
    if m:
        return 5, f"{m.group(1)} {m.group(2)}"
    m = re.match(r"^(\d+\.\d+\.\d+)\s+(\S.*)$", s)
    if m:
        return 4, f"{m.group(1)} {m.group(2)}"
    m = SUBCHAPTER_RE.match(s)
    if m:
        return 3, f"{m.group(1)} {m.group(2)}"
    m = CHAPTER_RE.match(s)
    if m and 1 <= int(m.group(1)) <= 9 and len(s) < 60:
        return 2, f"{m.group(1)}. {m.group(2)}"
    m = APPENDIX_RE.match(s)
    if m and len(s) < 60:
        return 2, f"부록 {m.group(1)}. {m.group(2)}"
    return None


def extract(pdf_path: Path, skip_pages: int = 3, body_starts_at: int = 11) -> str:
    out: list[str] = []
    out.append("# CLDC 1.1 규격 (한국어)")
    out.append("")
    out.append(
        "> Connected Limited Device Configuration Specification Version 1.1 "
        "(Sun Microsystems, 2003년 3월). `vendor/cldc-1_1-fr-spec-ko/"
        "CLDCSpecification1.1.pdf` 한국어 원본을 텍스트 추출한 결과."
    )
    out.append("")

    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for idx, page in enumerate(pdf.pages):
            if idx < skip_pages:
                continue
            raw = page.extract_text() or ""
            raw = clean_text(raw)
            lines = raw.split("\n")
            # Drop noise lines (headers / page numbers)
            cleaned: list[str] = []
            for ln in lines:
                if is_noise(ln):
                    continue
                cleaned.append(ln.rstrip())
            if not cleaned:
                continue
            out.append(f"<!-- page {idx + 1}/{total} -->")
            heading_active = (idx + 1) >= body_starts_at
            for ln in cleaned:
                s = ln.strip()
                if not s:
                    out.append("")
                    continue
                h = looks_like_heading(s) if heading_active else None
                if h:
                    level, title = h
                    out.append("")
                    out.append(f"{'#' * level} {title}")
                    out.append("")
                else:
                    out.append(s)
            out.append("")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    src = Path(argv[1])
    dst = Path(argv[2])
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(extract(src), encoding="utf-8")
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
