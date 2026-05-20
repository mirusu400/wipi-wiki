#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt for the WIPI Wiki Astro Starlight site.

Usage:
    python3 scripts/build_llms_txt.py <site_dir> [--site-url URL]

Walks src/content/docs/ for all Markdown content and writes:

  <site_dir>/llms.txt       — index of pages (title, URL, 1-line summary)
  <site_dir>/llms-full.txt  — every doc concatenated with a header separator

Also mirrors src/content/docs/**/*.md into <site_dir> so URLs in llms.txt
that point at raw `.md` files resolve. Run AFTER `astro build` so this
overwrites the public/ placeholders.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "src" / "content" / "docs"
ASTRO_CONFIG = REPO_ROOT / "astro.config.mjs"

SITE_NAME = "WIPI Wiki"
SITE_DESCRIPTION = "WIPI 1.2.1 모바일 표준 플랫폼 API 레퍼런스"


def detect_site_url() -> str:
    """Parse astro.config.mjs for site + base. Fall back to known prod URL."""
    try:
        text = ASTRO_CONFIG.read_text(encoding="utf-8")
    except OSError:
        return "https://mirusu400.github.io/wipi-wiki"
    site_m = re.search(r"site:\s*['\"]([^'\"]+)['\"]", text)
    base_m = re.search(r"base:\s*['\"]([^'\"]+)['\"]", text)
    site = site_m.group(1).rstrip("/") if site_m else "https://mirusu400.github.io"
    base = base_m.group(1).strip("/") if base_m else ""
    return f"{site}/{base}".rstrip("/") if base else site


def md_to_url(meta_url: str, rel: Path) -> str:
    return f"{meta_url}/{rel.as_posix()}"


def copy_md_into_site(site_dir: Path) -> int:
    count = 0
    for src in DOCS_DIR.rglob("*.md"):
        rel = src.relative_to(DOCS_DIR)
        dst = site_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        count += 1
    return count


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def strip_frontmatter(md: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(md)
    if not m:
        return {}, md
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip("'\"")
    return fm, md[m.end():]


def extract_title_and_summary(md: str, fallback: str) -> tuple[str, str]:
    fm, body = strip_frontmatter(md)
    title = fm.get("title") or fallback
    summary = fm.get("description", "")
    if not summary:
        for line in body.splitlines():
            s = line.strip()
            if title == fallback:
                m = re.match(r"^#\s+(.+?)\s*$", s)
                if m:
                    title = m.group(1)
                    continue
            if title != fallback and s and not s.startswith("#") and not s.startswith("|") and not s.startswith("-"):
                summary = re.sub(r"\s+", " ", s)[:160]
                break
    return title, summary


def iter_md_files() -> list[Path]:
    return sorted(p for p in DOCS_DIR.rglob("*.md"))


def build_index(site_url: str) -> str:
    lines: list[str] = []
    lines.append(f"# {SITE_NAME}")
    lines.append("")
    lines.append(f"> {SITE_DESCRIPTION}")
    lines.append("")
    lines.append(
        "WIPI 1.2.1 (한국 무선 인터넷 표준 플랫폼, 2005년 KWISF 제정) 규격서를 "
        "검색 가능한 Markdown 으로 재구성한 개발자 레퍼런스. 원본은 939페이지 한국어 PDF + "
        "JavaDoc HTML. 모든 페이지가 순수 Markdown 이라 LLM 이 직접 grep / fetch 가능."
    )
    lines.append("")
    lines.append("## LLM / Claude Code 사용 가이드")
    lines.append("")
    lines.append("### 네임스페이스로 어디를 볼지 결정")
    lines.append("")
    lines.append("- `MC_xxx` — C API (응용 → 플랫폼). 12개 카테고리")
    lines.append("- `MH_xxx` — HAL API (플랫폼 → 단말 기본SW). 15개 카테고리")
    lines.append("- `org.kwis.*` — Java API. 11개 패키지, 135개 클래스")
    lines.append("")
    lines.append("### 빠른 조회 패턴")
    lines.append("")
    lines.append("```")
    lines.append("# raw md fetch (HTML chrome 없음, 토큰 절약)")
    lines.append(f"curl {site_url}/c-api/kernel.md")
    lines.append(f"curl {site_url}/hal/system.md")
    lines.append(f"curl {site_url}/java-api/org/kwis/msp/io/File.md")
    lines.append("")
    lines.append("# 전체 덤프")
    lines.append(f"curl {site_url}/llms-full.txt")
    lines.append("```")
    lines.append("")
    lines.append("> 인덱스 링크는 모두 `.md` raw 파일. Starlight HTML 페이지(`/c-api/kernel/`)가 아니라 "
                 "`/c-api/kernel.md` 를 가리킨다.")
    lines.append("")
    lines.append("---")
    lines.append("")

    sections: dict[str, list[tuple[str, str, str]]] = {}
    for path in iter_md_files():
        rel = path.relative_to(DOCS_DIR)
        top = rel.parts[0] if len(rel.parts) > 1 else "Home"
        title, summary = extract_title_and_summary(
            path.read_text(encoding="utf-8"), fallback=rel.stem
        )
        url = md_to_url(site_url, rel)
        sections.setdefault(top, []).append((title, url, summary))

    section_order = ["Home", "overview", "hal", "c-api", "java-api", "cldc", "midp", "appendix"]
    ordered_keys = [k for k in section_order if k in sections] + [
        k for k in sections if k not in section_order
    ]
    for key in ordered_keys:
        lines.append(f"## {key}")
        lines.append("")
        for title, url, summary in sections[key]:
            if summary:
                lines.append(f"- [{title}]({url}): {summary}")
            else:
                lines.append(f"- [{title}]({url})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_full() -> str:
    parts: list[str] = []
    for path in iter_md_files():
        rel = path.relative_to(DOCS_DIR)
        parts.append(f"\n\n<!-- ===== {rel.as_posix()} ===== -->\n")
        parts.append(path.read_text(encoding="utf-8").rstrip())
        parts.append("\n")
    return "".join(parts).lstrip() + "\n"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("site_dir", type=Path)
    ap.add_argument("--site-url", default=None)
    args = ap.parse_args(argv[1:])

    if not DOCS_DIR.is_dir():
        print(f"docs dir not found: {DOCS_DIR}", file=sys.stderr)
        return 2

    site_dir = args.site_dir
    site_dir.mkdir(parents=True, exist_ok=True)
    site_url = (args.site_url or detect_site_url()).rstrip("/")

    (site_dir / "llms.txt").write_text(build_index(site_url), encoding="utf-8")
    (site_dir / "llms-full.txt").write_text(build_full(), encoding="utf-8")
    copied = copy_md_into_site(site_dir)
    print(f"wrote {site_dir/'llms.txt'}")
    print(f"wrote {site_dir/'llms-full.txt'}")
    print(f"copied {copied} raw .md files into {site_dir}")
    print(f"site_url: {site_url}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
