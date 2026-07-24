#!/usr/bin/env python3
"""
Auto-indent C code blocks in Markdown files.

Processes all ```c code blocks in v20/ and v22/ docs,
applying proper indentation based on brace depth.

Usage:
    python3 scripts/indent_c_blocks.py
"""
import os
import re
import sys

DOCS_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "src", "content", "docs")

TARGETS = ["v20", "v22"]


def indent_c_code(code: str) -> str:
    """Apply brace-based indentation to C code."""
    lines = code.split("\n")
    result = []
    depth = 0
    indent = "    "  # 4 spaces

    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            result.append("")
            continue

        # Closing brace (or }; or },) decreases depth BEFORE this line
        close_first = stripped.startswith("}") or stripped.startswith("};")
        if close_first:
            depth = max(0, depth - stripped.count("}"))

        # Apply indentation
        result.append(indent * depth + stripped)

        # Adjust depth based on braces in this line
        if not close_first:
            opens = stripped.count("{")
            closes = stripped.count("}")
            depth = max(0, depth + opens - closes)

    return "\n".join(result)


def process_file(filepath: str) -> int:
    """Process a single .md file, returns number of blocks fixed."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0

    def replace_block(m):
        nonlocal count
        code = m.group(1)
        indented = indent_c_code(code)
        if indented != code:
            count += 1
        return f"```c\n{indented}\n```"

    new_content = re.sub(
        r"```c\n(.*?)\n```",
        replace_block,
        content,
        flags=re.DOTALL,
    )

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return count


def main():
    total_files = 0
    total_blocks = 0

    for target in TARGETS:
        target_dir = os.path.join(DOCS_ROOT, target)
        if not os.path.isdir(target_dir):
            print(f"Skipping {target}: not found")
            continue

        for dirpath, _, filenames in os.walk(target_dir):
            for fn in sorted(filenames):
                if not fn.endswith(".md") or fn == "index.md":
                    continue
                filepath = os.path.join(dirpath, fn)
                n = process_file(filepath)
                if n > 0:
                    rel = os.path.relpath(filepath, DOCS_ROOT)
                    print(f"  {rel}: {n} blocks indented")
                    total_files += 1
                    total_blocks += n

    print(f"\nDone. {total_blocks} code blocks indented across {total_files} files.")


if __name__ == "__main__":
    main()
