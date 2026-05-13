#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt for the WIPI Wiki site.

Usage:
    python3 scripts/build_llms_txt.py <site_dir>

Reads mkdocs.yml for site_name / site_description / site_url, walks docs/ for
all Markdown content, and writes:

  <site_dir>/llms.txt       — index of pages (title, URL, 1-line summary)
  <site_dir>/llms-full.txt  — every doc concatenated with a header separator

Follows the llmstxt.org convention.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"


def load_site_meta() -> dict:
    with MKDOCS_YML.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return {
        "name": data.get("site_name", "WIPI Wiki"),
        "description": data.get("site_description", ""),
        "url": data.get("site_url", "").rstrip("/"),
    }


def md_to_url(meta_url: str, rel: Path) -> str:
    parts = rel.with_suffix("").as_posix()
    if parts.endswith("/index"):
        parts = parts[: -len("index")]
    elif parts == "index":
        parts = ""
    return f"{meta_url}/{parts}".rstrip("/") + ("/" if not parts.endswith(".md") else "")


def extract_title_and_summary(md: str, fallback: str) -> tuple[str, str]:
    title = fallback
    summary = ""
    for line in md.splitlines():
        s = line.strip()
        if not title or title == fallback:
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


def build_index(meta: dict) -> str:
    lines: list[str] = []
    lines.append(f"# {meta['name']}")
    lines.append("")
    if meta["description"]:
        lines.append(f"> {meta['description']}")
        lines.append("")
    lines.append(
        "WIPI 1.2.1 (한국 무선 인터넷 표준 플랫폼) 규격을 검색 가능한 Markdown 으로 "
        "재구성한 개발자 레퍼런스. 모든 페이지는 순수 Markdown 으로 제공되어 LLM 이 "
        "직접 grep / fetch 할 수 있다."
    )
    lines.append("")

    sections: dict[str, list[tuple[str, str, str]]] = {}
    for path in iter_md_files():
        rel = path.relative_to(DOCS_DIR)
        top = rel.parts[0] if len(rel.parts) > 1 else "Home"
        title, summary = extract_title_and_summary(
            path.read_text(encoding="utf-8"), fallback=rel.stem
        )
        url = md_to_url(meta["url"], rel)
        sections.setdefault(top, []).append((title, url, summary))

    section_order = ["", "Home", "overview", "hal", "c-api", "java-api", "appendix"]
    seen: set[str] = set()
    ordered_keys = [k for k in section_order if k in sections] + [
        k for k in sections if k not in section_order
    ]
    for key in ordered_keys:
        if key in seen:
            continue
        seen.add(key)
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
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    site_dir = Path(argv[1])
    site_dir.mkdir(parents=True, exist_ok=True)
    meta = load_site_meta()

    (site_dir / "llms.txt").write_text(build_index(meta), encoding="utf-8")
    (site_dir / "llms-full.txt").write_text(build_full(), encoding="utf-8")
    print(f"wrote {site_dir/'llms.txt'}")
    print(f"wrote {site_dir/'llms-full.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
