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
import shutil
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
    """Return URL pointing at the raw `.md` file (not the rendered HTML page).

    LLMs that follow links from llms.txt should fetch the plain Markdown, not
    the MkDocs HTML page (which is wrapped in nav chrome + JS). The build step
    copies every `docs/**/*.md` into `site/` at the same relative path so these
    URLs resolve.
    """
    return f"{meta_url}/{rel.as_posix()}"


def copy_md_into_site(site_dir: Path) -> int:
    """Mirror docs/**/*.md into site/ so the URLs in llms.txt are reachable."""
    count = 0
    for src in DOCS_DIR.rglob("*.md"):
        rel = src.relative_to(DOCS_DIR)
        dst = site_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        count += 1
    return count


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
    url = meta["url"]
    lines: list[str] = []
    lines.append(f"# {meta['name']}")
    lines.append("")
    if meta["description"]:
        lines.append(f"> {meta['description']}")
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
    lines.append("- `MC_xxx` — C API (응용 → 플랫폼). 12개 카테고리: 커널/그래픽/DB/파일시스템/네트워크/매체/시리얼/전화/MISC/유틸/UI/표준C")
    lines.append("- `MH_xxx` — HAL API (플랫폼 → 단말 기본SW). 15개 카테고리: 타입/플랫폼/시스템/콜/단말/네트워크/시리얼/매체/시간/유틸/파일/입력/폰트/프레임버퍼/가상키")
    lines.append("- `org.kwis.*` — Java API. 11개 패키지, 135개 클래스. JavaDoc 원본을 MD 로 변환")
    lines.append("")
    lines.append("### 빠른 조회 패턴")
    lines.append("")
    lines.append("```")
    lines.append("# 1) 단일 페이지 raw md fetch (HTML 안 받음, 토큰 절약)")
    lines.append(f"curl {url}/c-api/kernel.md")
    lines.append(f"curl {url}/hal/system.md")
    lines.append(f"curl {url}/java-api/org/kwis/msp/io/File.md")
    lines.append("")
    lines.append("# 2) 카테고리 인덱스 (목차 + 챕터 링크)")
    lines.append(f"curl {url}/c-api/index.md")
    lines.append(f"curl {url}/hal/index.md")
    lines.append(f"curl {url}/java-api/index.md")
    lines.append("")
    lines.append("# 3) 전체 덤프 한 번에 (오프라인/큰 컨텍스트)")
    lines.append(f"curl {url}/llms-full.txt")
    lines.append("")
    lines.append("# 4) repo 클론한 경우: 로컬 grep")
    lines.append("grep -rn 'MC_grpDrawLine' docs/c-api/")
    lines.append("```")
    lines.append("")
    lines.append("> **중요**: 아래 인덱스의 모든 링크는 `.md` raw 파일을 가리킨다 "
                 "(`/c-api/kernel/` HTML 페이지가 아니라 `/c-api/kernel.md`). "
                 "LLM 은 raw md 를 fetch 해서 HTML chrome / JS 토큰을 낭비하지 말 것.")
    lines.append("")
    lines.append("### 페이지 구조")
    lines.append("")
    lines.append("PDF 추출 페이지 (c-api/, hal/, overview/, appendix/) 는 일관된 형식:")
    lines.append("")
    lines.append("- `### 함수명` — API 엔트리 헤딩")
    lines.append("- `**프로토타입**` 다음 ```c 펜스 — 시그니처")
    lines.append("- `**설명**` — 동작 설명")
    lines.append("- `**매개 변수**` — `- \\`param\\` — 설명` 형태 불릿")
    lines.append("- `**반환 값**` — 리턴 값 의미")
    lines.append("- `**참고 항목**`, `**예제**`, `**부작용**`, `**에러 코드**` — 상황별")
    lines.append("")
    lines.append("Java API (java-api/) 는 JavaDoc 변환:")
    lines.append("")
    lines.append("- 클래스 페이지: 상속 트리 + 필드/생성자/메서드 요약 + 상세")
    lines.append("- Parameters / Returns 블록 그대로 유지")
    lines.append("")
    lines.append("### URL 형태")
    lines.append("")
    lines.append(f"- raw md (LLM 권장): `{url}/c-api/kernel.md`")
    lines.append(f"- HTML 페이지 (사람 권장): `{url}/c-api/kernel/`")
    lines.append("- repo 경로: `docs/c-api/kernel.md` (사이트 path 그대로)")
    lines.append("")
    lines.append("### 알려진 한계")
    lines.append("")
    lines.append("- PDF 추출본은 일부 표/그림이 누락 (텍스트만). 표 원본은 PDF 직접 참고")
    lines.append("- Java API 의 일부 다중 파라미터 메서드는 첫 파라미터 누락 가능 (변환기 nested `<dd>` 이슈)")
    lines.append("- 사이트 검색 (MkDocs 기본) 은 CJK 토크나이징 약함. 정확한 식별자 검색은 본 llms.txt + grep 권장")
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
    copied = copy_md_into_site(site_dir)
    print(f"wrote {site_dir/'llms.txt'}")
    print(f"wrote {site_dir/'llms-full.txt'}")
    print(f"copied {copied} raw .md files into {site_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
