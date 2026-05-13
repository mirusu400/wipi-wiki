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
    r"Connected Limited Device Configuration\s+.*2003년|"
    r"[ivxlcmIVXLCM]+\s+Connected Limited Device Configuration|"
    r"[ivxlcmIVXLCM]+\s+Connected,\s+Limited\s+Device\s+Configuration|"
    r"CLDC 바이트 코드 유형 검사기 규격)"
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
    # Running page footer/header like "1장 소개 및 배경 3" or "머리말 xv"
    if re.match(r"^\d+장\s+.+\s+\d+$", s):
        return True
    if re.match(r"^(머리말|목차|그림|부록)\s+[ivxlcm\d]+$", s, re.IGNORECASE):
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
    m = re.match(r"^(\d+)장\s+(.+)$", s)
    if m and len(s) < 60:
        return 2, f"{m.group(1)}장 {m.group(2)}"
    m = re.match(r"^(\d+)\.\s+(\S.*)$", s)
    if m and 1 <= int(m.group(1)) <= 9 and len(s) < 25:
        return 2, f"{m.group(1)}. {m.group(2)}"
    m = CHAPTER_RE.match(s)
    if m and 1 <= int(m.group(1)) <= 9 and len(s) < 60:
        return 2, f"{m.group(1)}. {m.group(2)}"
    m = APPENDIX_RE.match(s)
    if m and len(s) < 60:
        return 2, f"부록 {m.group(1)}. {m.group(2)}"
    return None


BULLET_RE = re.compile(r"^[■●◆▶◯○]\s*(.+)$")
NUMBERED_RE = re.compile(r"^(\d+)\.\s+(.+)$")


def smart_join(lines: list[str]) -> str:
    """Join wrapped lines. No space at Hangul-Hangul boundary (PDF wraps
    Korean text mid-word); single space otherwise."""
    if not lines:
        return ""
    result = lines[0]
    for nxt in lines[1:]:
        if not nxt:
            continue
        prev_end = result[-1:]
        nxt_start = nxt[:1]
        if HANGUL_RE.match(prev_end) and HANGUL_RE.match(nxt_start):
            result += nxt
        else:
            result += " " + nxt
    return result


def flush_paragraph(buf: list[str], out: list[str], is_bullet: bool = False) -> None:
    if not buf:
        return
    joined = smart_join(buf).strip()
    out.append(f"- {joined}" if is_bullet else joined)
    buf.clear()


def emit_body_lines(lines: list[str], out: list[str]) -> None:
    """Render body-section lines: join wrapped lines, convert bullets."""
    para: list[str] = []
    is_bullet = False
    for ln in lines:
        s = ln.strip()
        if not s:
            flush_paragraph(para, out, is_bullet)
            is_bullet = False
            out.append("")
            continue
        h = looks_like_heading(s)
        if h:
            flush_paragraph(para, out, is_bullet)
            is_bullet = False
            level, title = h
            out.append("")
            out.append(f"{'#' * level} {title}")
            out.append("")
            continue
        bm = BULLET_RE.match(s)
        if bm:
            flush_paragraph(para, out, is_bullet)
            is_bullet = True
            para.append(bm.group(1).strip())
            continue
        para.append(s)
        # Sentence-end heuristic: break paragraph after Korean declarative
        # endings followed by period. PDF doesn't preserve paragraph breaks,
        # so this gives some structure without over-splitting. Also exits
        # bullet mode so the next plain paragraph doesn't get appended.
        if re.search(r"(다|음|요|오|함|임)\.$", s):
            flush_paragraph(para, out, is_bullet)
            is_bullet = False
            out.append("")
    flush_paragraph(para, out, is_bullet)


def emit_frontmatter_lines(lines: list[str], out: list[str]) -> None:
    """Render TOC / frontmatter — keep line breaks but use ``  `` for soft break."""
    for ln in lines:
        s = ln.strip()
        if not s:
            out.append("")
        else:
            out.append(s + "  ")


def extract(
    pdf_path: Path,
    skip_pages: int = 3,
    body_starts_at: int = 11,
    title: str = "CLDC 1.1 규격 (한국어)",
    subtitle: str = (
        "Connected Limited Device Configuration Specification Version 1.1 "
        "(Sun Microsystems, 2003년 3월). `vendor/cldc-1_1-fr-spec-ko/"
        "CLDCSpecification1.1.pdf` 한국어 원본을 텍스트 추출한 결과."
    ),
) -> str:
    out: list[str] = []
    out.append(f"# {title}")
    out.append("")
    out.append(f"> {subtitle}")
    out.append("")

    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for idx, page in enumerate(pdf.pages):
            if idx < skip_pages:
                continue
            raw = page.extract_text() or ""
            raw = clean_text(raw)
            lines = raw.split("\n")
            # Recognize PDF chapter headings split across three lines as
            # ``<num>\n장\n<title>`` and merge them into one before noise
            # filtering would drop the bare number.
            merged: list[str] = []
            i = 0
            while i < len(lines):
                s = lines[i].strip()
                if (re.fullmatch(r"\d+", s) and i + 2 < len(lines)
                        and lines[i + 1].strip() == "장"
                        and lines[i + 2].strip()):
                    merged.append(f"{s}장 {lines[i + 2].strip()}")
                    i += 3
                    continue
                merged.append(lines[i])
                i += 1
            cleaned: list[str] = []
            for ln in merged:
                if is_noise(ln):
                    continue
                cleaned.append(ln.rstrip())
            if not cleaned:
                continue
            out.append(f"<!-- page {idx + 1}/{total} -->")
            out.append("")
            if (idx + 1) >= body_starts_at:
                emit_body_lines(cleaned, out)
            else:
                emit_frontmatter_lines(cleaned, out)
            out.append("")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


def main(argv: list[str]) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Extract a Korean CLDC PDF to Markdown.")
    p.add_argument("pdf")
    p.add_argument("out")
    p.add_argument("--skip-pages", type=int, default=3)
    p.add_argument("--body-starts-at", type=int, default=11)
    p.add_argument("--title", default="CLDC 1.1 규격 (한국어)")
    p.add_argument("--subtitle", default=(
        "Connected Limited Device Configuration Specification Version 1.1 "
        "(Sun Microsystems, 2003년 3월). `vendor/cldc-1_1-fr-spec-ko/"
        "CLDCSpecification1.1.pdf` 한국어 원본을 텍스트 추출한 결과."
    ))
    args = p.parse_args(argv[1:])
    dst = Path(args.out)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(
        extract(
            Path(args.pdf),
            skip_pages=args.skip_pages,
            body_starts_at=args.body_starts_at,
            title=args.title,
            subtitle=args.subtitle,
        ),
        encoding="utf-8",
    )
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
