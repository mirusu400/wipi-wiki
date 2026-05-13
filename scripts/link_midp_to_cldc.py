#!/usr/bin/env python3
"""MIDP 패키지 인덱스의 plain-text 클래스 항목을 CLDC 트리로 cross-link.

MIDP javadoc 패키지 요약은 CLDC 에서 상속된 클래스를 다 나열하지만
MIDP javadoc 자체에는 해당 클래스 HTML 이 없다. 변환기는 그래서 plain bullet
(`` `ClassName` `` — desc) 로 남긴다. 이 스크립트는 CLDC 트리에 같은 이름의
md 가 있으면 상대경로 링크로 교체한다.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIDP_ROOT = ROOT / "docs" / "midp" / "java-api"
CLDC_ROOT = ROOT / "docs" / "cldc" / "java-api"

PLAIN_RE = re.compile(r"^(- )`([A-Za-z_][\w]*)`(\s+—\s+.*)?$")


def relink_index(index_md: Path) -> int:
    rel_pkg = index_md.parent.relative_to(MIDP_ROOT)
    cldc_pkg = CLDC_ROOT / rel_pkg
    if not cldc_pkg.is_dir():
        return 0

    lines = index_md.read_text(encoding="utf-8").splitlines()
    changed = 0
    out: list[str] = []
    for line in lines:
        m = PLAIN_RE.match(line)
        if not m:
            out.append(line)
            continue
        name = m.group(2)
        cldc_md = cldc_pkg / f"{name}.md"
        if not cldc_md.is_file():
            out.append(line)
            continue
        rel = os.path.relpath(cldc_md, index_md.parent)
        tail = m.group(3) or ""
        out.append(f"{m.group(1)}[{name}]({rel}){tail}")
        changed += 1

    if changed:
        index_md.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    total = 0
    touched = 0
    for index_md in MIDP_ROOT.rglob("index.md"):
        if index_md.parent == MIDP_ROOT:
            continue
        n = relink_index(index_md)
        if n:
            touched += 1
            total += n
            print(f"  {index_md.relative_to(ROOT)}: {n} link(s)")
    print(f"Re-linked {total} entries across {touched} index file(s).")


if __name__ == "__main__":
    main()
