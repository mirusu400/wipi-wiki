#!/usr/bin/env python3
"""Inject Starlight frontmatter (title) into every .md under src/content/docs.

- Skips files that already have YAML frontmatter.
- Pulls title from first H1; falls back to filename stem.
- Removes the H1 line from the body to avoid duplicate headings under Starlight.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("src/content/docs")


def yaml_escape(s: str) -> str:
    # Always wrap in double quotes; escape backslash + double-quote.
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def fallback_title(path: Path) -> str:
    stem = path.stem
    if stem == "index":
        return path.parent.name or "Home"
    return stem


def process(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        return "skipped (has frontmatter)"

    lines = text.splitlines(keepends=False)
    title: str | None = None
    drop_idx: int | None = None
    for i, line in enumerate(lines[:50]):  # scan top of file only
        m = H1_RE.match(line)
        if m:
            title = m.group(1).strip()
            drop_idx = i
            break

    if title is None:
        title = fallback_title(path)
        new_lines = lines
    else:
        # Drop H1 line and at most one trailing blank line.
        new_lines = lines[:drop_idx] + lines[drop_idx + 1:]
        if new_lines and drop_idx < len(new_lines) and new_lines[drop_idx].strip() == "":
            new_lines.pop(drop_idx)

    fm = f"---\ntitle: {yaml_escape(title)}\n---\n\n"
    body = "\n".join(new_lines).lstrip("\n")
    path.write_text(fm + body + ("\n" if not body.endswith("\n") else ""), encoding="utf-8")
    return f"injected: {title}"


def main() -> int:
    if not ROOT.exists():
        print(f"not found: {ROOT}", file=sys.stderr)
        return 1
    n = 0
    skipped = 0
    for md in sorted(ROOT.rglob("*.md")):
        result = process(md)
        if result.startswith("skipped"):
            skipped += 1
        else:
            n += 1
    print(f"injected {n}, skipped {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
