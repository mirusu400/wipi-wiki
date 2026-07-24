#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt for the WIPI Wiki Astro Starlight site.

Usage:
    python3 scripts/build_llms_txt.py <site_dir> [--site-url URL]

Walks src/content/docs/ for all Markdown content and writes:

  <site_dir>/llms.txt            — index of all pages across all versions
  <site_dir>/llms-full.txt       — every doc concatenated
  <site_dir>/llms-v20-full.txt   — v2.0 docs only
  <site_dir>/llms-v22-full.txt   — v2.2.0 docs only

Also mirrors src/content/docs/**/*.md into <site_dir> so URLs in llms.txt
that point at raw `.md` files resolve. Run AFTER `astro build`.
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
SITE_DESCRIPTION = (
    "WIPI 모바일 표준 플랫폼 API 레퍼런스 — v1.2.1 / v2.0 / v2.2.0"
)

VERSIONS = {
    "v1.2.1": {
        "prefix": "",
        "desc": "WIPI 1.2.1 (2005) — 939페이지 PDF + JavaDoc HTML 기반",
        "sections": ["overview", "hal", "c-api", "java-api", "cldc", "midp", "appendix"],
    },
    "v2.0": {
        "prefix": "v20",
        "desc": "WIPI 2.0 (TTAS.KO-06.0036/R3, 2004) — 편별 PDF 6개, 총 1,291페이지",
        "sections": ["v20/overview", "v20/hal", "v20/c-api", "v20/java-api",
                      "v20/optional", "v20/appendix"],
    },
    "v2.2.0": {
        "prefix": "v22",
        "desc": "WIPI 2.2.0 (TTAK.KO-06.0036/R6, 2008) — 단일 PDF, 1,356페이지",
        "sections": ["v22/overview", "v22/hal", "v22/c-api", "v22/java-api",
                      "v22/optional", "v22/appendix"],
    },
}


def detect_site_url() -> str:
    try:
        text = ASTRO_CONFIG.read_text(encoding="utf-8")
    except OSError:
        return "https://mirusu400.github.io/wipi-wiki"
    site_m = re.search(r"site:\s*['\"]([^'\"]+)['\"]", text)
    base_m = re.search(r"base:\s*['\"]([^'\"]+)['\"]", text)
    site = site_m.group(1).rstrip("/") if site_m else "https://mirusu400.github.io"
    base = base_m.group(1).strip("/") if base_m else ""
    return f"{site}/{base}".rstrip("/") if base else site


def md_to_url(site_url: str, rel: Path) -> str:
    return f"{site_url}/{rel.as_posix()}"


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


def get_version(rel: Path) -> str:
    top = rel.parts[0] if len(rel.parts) > 1 else ""
    if top == "v20":
        return "v2.0"
    elif top == "v22":
        return "v2.2.0"
    return "v1.2.1"


def get_section_key(rel: Path) -> str:
    parts = rel.parts
    if len(parts) <= 1:
        return "Home"
    if parts[0] in ("v20", "v22"):
        return "/".join(parts[:2]) if len(parts) > 2 else parts[0]
    return parts[0]


def iter_md_files() -> list[Path]:
    return sorted(p for p in DOCS_DIR.rglob("*.md"))


def build_index(site_url: str) -> str:
    lines: list[str] = []
    lines.append(f"# {SITE_NAME}")
    lines.append("")
    lines.append(f"> {SITE_DESCRIPTION}")
    lines.append("")
    lines.append(
        "WIPI (Wireless Internet Platform for Interoperability)는 한국 모바일 표준 플랫폼 규격이다. "
        "이 위키는 v1.2.1, v2.0, v2.2.0 세 버전의 규격서를 검색 가능한 Markdown으로 재구성한 "
        "개발자 레퍼런스이다. 모든 페이지가 순수 Markdown이라 LLM이 직접 grep/fetch 가능."
    )
    lines.append("")
    lines.append("## 버전별 접근")
    lines.append("")
    lines.append("| 버전 | 규격서 | llms-full |")
    lines.append("|---|---|---|")
    lines.append(f"| v1.2.1 | [HAL]({site_url}/hal/system.md) [C API]({site_url}/c-api/kernel.md) [Java API]({site_url}/java-api/org/kwis/msf/core/Kernel.md) | `curl {site_url}/llms-full.txt` |")
    lines.append(f"| v2.0 | [HAL]({site_url}/v20/hal/system.md) [C API]({site_url}/v20/c-api/kernel.md) [Java API]({site_url}/v20/java-api/kernel.md) | `curl {site_url}/llms-v20-full.txt` |")
    lines.append(f"| v2.2.0 | [HAL]({site_url}/v22/hal/system.md) [C API]({site_url}/v22/c-api/kernel.md) [Java API]({site_url}/v22/java-api/kernel.md) | `curl {site_url}/llms-v22-full.txt` |")
    lines.append("")
    lines.append("## 네임스페이스 가이드")
    lines.append("")
    lines.append("- `MC_xxx` — C API (응용 -> 플랫폼)")
    lines.append("- `MH_xxx` — HAL API (플랫폼 -> 단말 기본SW)")
    lines.append("- `org.kwis.*` — Java API")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Group files by version, then by section
    all_files = iter_md_files()

    for ver_name, ver_info in VERSIONS.items():
        prefix = ver_info["prefix"]
        lines.append(f"## {ver_name}")
        lines.append("")
        lines.append(f"> {ver_info['desc']}")
        lines.append("")

        sections: dict[str, list[tuple[str, str, str]]] = {}
        for path in all_files:
            rel = path.relative_to(DOCS_DIR)
            if get_version(rel) != ver_name:
                continue
            sec_key = get_section_key(rel)
            title, summary = extract_title_and_summary(
                path.read_text(encoding="utf-8"), fallback=rel.stem
            )
            url = md_to_url(site_url, rel)
            sections.setdefault(sec_key, []).append((title, url, summary))

        for sec_key in ver_info["sections"]:
            if sec_key not in sections:
                continue
            display = sec_key.split("/")[-1] if "/" in sec_key else sec_key
            lines.append(f"### {display}")
            lines.append("")
            for title, url, summary in sections[sec_key]:
                if summary:
                    lines.append(f"- [{title}]({url}): {summary}")
                else:
                    lines.append(f"- [{title}]({url})")
            lines.append("")

        # Home/root files for this version
        home_key = prefix if prefix else "Home"
        if home_key in sections:
            for title, url, summary in sections[home_key]:
                if summary:
                    lines.append(f"- [{title}]({url}): {summary}")
                else:
                    lines.append(f"- [{title}]({url})")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_version_index(site_url: str, ver_name: str) -> str:
    """Build a standalone llms.txt for a single version."""
    ver_info = VERSIONS[ver_name]
    prefix = ver_info["prefix"]
    lines: list[str] = []
    lines.append(f"# WIPI Wiki — {ver_name}")
    lines.append("")
    lines.append(f"> {ver_info['desc']}")
    lines.append("")
    lines.append("## 네임스페이스 가이드")
    lines.append("")
    lines.append("- `MC_xxx` — C API (응용 -> 플랫폼)")
    lines.append("- `MH_xxx` — HAL API (플랫폼 -> 단말 기본SW)")
    lines.append("- `org.kwis.*` — Java API")
    lines.append("")
    pfx = f"/{prefix}" if prefix else ""
    lines.append("### 빠른 조회")
    lines.append("")
    lines.append("```")
    lines.append(f"curl {site_url}{pfx}/hal/system.md")
    lines.append(f"curl {site_url}{pfx}/c-api/kernel.md")
    full_name = f"llms-{prefix}-full.txt" if prefix else "llms-full.txt"
    lines.append(f"curl {site_url}/{full_name}")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")

    sections: dict[str, list[tuple[str, str, str]]] = {}
    for path in iter_md_files():
        rel = path.relative_to(DOCS_DIR)
        if get_version(rel) != ver_name:
            continue
        sec_key = get_section_key(rel)
        title, summary = extract_title_and_summary(
            path.read_text(encoding="utf-8"), fallback=rel.stem
        )
        url = md_to_url(site_url, rel)
        sections.setdefault(sec_key, []).append((title, url, summary))

    for sec_key in ver_info["sections"]:
        if sec_key not in sections:
            continue
        display = sec_key.split("/")[-1] if "/" in sec_key else sec_key
        lines.append(f"## {display}")
        lines.append("")
        for title, url, summary in sections[sec_key]:
            if summary:
                lines.append(f"- [{title}]({url}): {summary}")
            else:
                lines.append(f"- [{title}]({url})")
        lines.append("")

    home_key = prefix if prefix else "Home"
    if home_key in sections:
        for title, url, summary in sections[home_key]:
            if summary:
                lines.append(f"- [{title}]({url}): {summary}")
            else:
                lines.append(f"- [{title}]({url})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_full(version_filter: str | None = None) -> str:
    parts: list[str] = []
    for path in iter_md_files():
        rel = path.relative_to(DOCS_DIR)
        ver = get_version(rel)
        if version_filter and ver != version_filter:
            continue
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

    # Main index
    (site_dir / "llms.txt").write_text(build_index(site_url), encoding="utf-8")
    print(f"wrote {site_dir / 'llms.txt'}")

    # Full dumps
    (site_dir / "llms-full.txt").write_text(build_full(), encoding="utf-8")
    print(f"wrote {site_dir / 'llms-full.txt'}")

    for ver_name, ver_info in VERSIONS.items():
        prefix = ver_info["prefix"]
        if not prefix:
            continue  # v1.2.1 uses the main llms.txt / llms-full.txt
        (site_dir / f"llms-{prefix}.txt").write_text(
            build_version_index(site_url, ver_name), encoding="utf-8"
        )
        print(f"wrote {site_dir / f'llms-{prefix}.txt'}")
        (site_dir / f"llms-{prefix}-full.txt").write_text(
            build_full(ver_name), encoding="utf-8"
        )
        print(f"wrote {site_dir / f'llms-{prefix}-full.txt'}")

    copied = copy_md_into_site(site_dir)
    print(f"copied {copied} raw .md files into {site_dir}")
    print(f"site_url: {site_url}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
