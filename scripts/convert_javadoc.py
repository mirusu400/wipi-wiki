#!/usr/bin/env python3
"""
Convert WIPI JavaDoc HTML (frame-based, classic Javadoc) to Markdown.

Usage:
    python convert_javadoc.py <javadoc_root_dir> <output_dir>

Example:
    python scripts/convert_javadoc.py vendor/WIPI_API_1_1_1 docs/java-api

The JavaDoc files are assumed to be a stock 1.4-era javadoc layout:
  - package-list      (list of package names, one per line)
  - <pkg>/package-summary.html  (class index per package)
  - <pkg>/<Class>.html          (class detail pages)

Output:
  - <out>/index.md                            (overview)
  - <out>/<pkg>.md                            (package summary)
  - <out>/<pkg>/<Class>.md                    (class detail)
"""
from __future__ import annotations
import sys
import re
import os
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag


# -------------------- HTML helpers --------------------

def strip_nav(soup: BeautifulSoup) -> None:
    """Remove navigation chrome that javadoc puts on every page."""
    # Top/bottom nav bars
    for sel in (
        {"name": "navbar_top"}, {"name": "navbar_top_firstrow"},
        {"name": "navbar_bottom"}, {"name": "navbar_bottom_firstrow"},
        {"name": "skip-navbar_top"}, {"name": "skip-navbar_bottom"},
    ):
        for a in soup.find_all("a", attrs=sel):
            # walk up to the table that contains the navbar
            tbl = a.find_parent("table")
            if tbl:
                tbl.decompose()
            else:
                a.decompose()
    # "PREV CLASS  NEXT CLASS" lines and footer hr
    for hr in soup.find_all("hr"):
        # Remove trailing decoration hrs
        nxt = hr.next_sibling
        # Heuristic: hrs near nav links
        prev_text = (hr.previous_sibling.get_text() if hasattr(hr.previous_sibling, "get_text")
                     else (str(hr.previous_sibling) or ""))
        if "PREV" in prev_text.upper() or "NEXT" in prev_text.upper():
            hr.decompose()


def text_of(el) -> str:
    if el is None:
        return ""
    return el.get_text(" ", strip=True)


def collapse_ws(s: str) -> str:
    # Preserve fenced code blocks
    chunks = re.split(r"(```.*?```)", s, flags=re.DOTALL)
    out = []
    for i, ch in enumerate(chunks):
        if i % 2 == 1:
            # code block — keep as-is, just trim and collapse internal blank-line runs
            inner = ch[3:-3]
            if "\n" in inner:
                first, rest = inner.split("\n", 1)
                rest = rest.rstrip()
                rest = re.sub(r"\A\n+", "", rest)
                # Inside the code block: at most ONE consecutive blank line
                rest = re.sub(r"\n{2,}", "\n", rest)
                out.append("```" + first + "\n" + rest + "\n```")
            else:
                out.append("```" + inner + "```")
        else:
            t = re.sub(r"[ \t]+", " ", ch)
            t = re.sub(r"\n{3,}", "\n\n", t)
            out.append(t)
    s = "".join(out)
    return s.strip()


def inline_to_md(el) -> str:
    """Convert an inline-ish element to markdown. Keeps <code>, <b>, <i>, <a>, <br>."""
    if el is None:
        return ""
    if isinstance(el, NavigableString):
        return str(el)
    parts: list[str] = []
    for child in el.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
            continue
        name = child.name.lower()
        if name == "br":
            parts.append("  \n")
        elif name in ("code", "tt"):
            txt = child.get_text()
            # If the code spans multiple lines (contains <br> inside, or newlines),
            # render as a fenced block rather than inline `...`
            has_br = bool(child.find("br"))
            if has_br or "\n" in txt.strip():
                # Replace <br> with newlines, decode nbsps
                inner = child.decode_contents()
                inner = re.sub(r"<br\s*/?>", "\n", inner, flags=re.I)
                # strip remaining tags
                inner = BeautifulSoup(inner, "lxml").get_text()
                inner = inner.replace("\u00a0", " ").rstrip()
                parts.append("\n\n```java\n" + inner + "\n```\n\n")
            else:
                parts.append("`" + txt + "`")
        elif name in ("b", "strong"):
            parts.append("**" + inline_to_md(child).strip() + "**")
        elif name in ("i", "em"):
            parts.append("*" + inline_to_md(child).strip() + "*")
        elif name == "a":
            href = child.get("href") or ""
            txt = inline_to_md(child).strip()
            # Strip internal javadoc cross-refs to plain text — we'll rebuild links
            # within MkDocs based on our own structure if needed.
            if href.startswith("#"):
                parts.append(txt or href)
            elif ".html" in href and not href.startswith(("http://", "https://")):
                parts.append(f"`{txt}`")  # keep readable but unlinked for now
            else:
                if href:
                    parts.append(f"[{txt}]({href})")
                else:
                    parts.append(txt)
        elif name == "p":
            parts.append("\n\n" + inline_to_md(child).strip() + "\n\n")
        elif name == "font":
            parts.append(inline_to_md(child))
        else:
            parts.append(inline_to_md(child))
    return "".join(parts)


# -------------------- Page conversion --------------------

def convert_class_page(html: str, pkg: str, class_name: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    strip_nav(soup)
    out: list[str] = []

    # Header
    h2 = soup.find("h2")
    if h2:
        # h2 text is like "org.kwis.msp.lcduiClass  Graphics" — split apart
        title = text_of(h2)
        # The package name is concatenated to "Class XXX" or "Interface XXX"
        m = re.match(r"^(.*?)(Class|Interface|Enum)\s+(.+)$", title)
        if m:
            out.append(f"# {m.group(2)} {m.group(3)}")
            out.append(f"\n`package {pkg}`\n")
        else:
            out.append(f"# {title}")
            out.append(f"\n`package {pkg}`\n")
    else:
        out.append(f"# {class_name}")
        out.append(f"\n`package {pkg}`\n")

    # Inheritance tree (PRE element near the top, before field/method summary)
    pre = soup.find("pre")
    if pre and "extends" not in pre.get_text() and "Object" in pre.get_text():
        # Just show the inheritance hierarchy
        out.append("\n```\n" + pre.get_text() + "\n```\n")
    elif pre:
        out.append("\n```\n" + pre.get_text() + "\n```\n")

    # Class declaration block — usually a <pre> right before the description
    # Already captured above

    # Class description: paragraphs between class declaration and summary anchors
    # Locate the field_summary or method_summary or constructor_summary anchor and
    # take everything between class signature and it.
    summary_anchor = (
        soup.find("a", attrs={"name": "field_summary"})
        or soup.find("a", attrs={"name": "constructor_summary"})
        or soup.find("a", attrs={"name": "method_summary"})
        or soup.find("a", attrs={"name": "inner_class_summary"})
    )

    desc_parts: list[str] = []
    if pre is not None:
        node = pre.next_sibling
        # Move forward collecting paragraphs/h3 until we hit the summary anchor
        while node is not None:
            if isinstance(node, Tag):
                if node.find("a", attrs={"name": True}):
                    a_inside = node.find("a", attrs={"name": True})
                    if a_inside["name"] in ("field_summary", "constructor_summary",
                                            "method_summary", "inner_class_summary"):
                        break
                if node.name == "h3":
                    desc_parts.append(f"\n### {text_of(node)}\n")
                elif node.name in ("p", "div"):
                    desc_parts.append(inline_to_md(node).strip())
                elif node.name == "hr":
                    pass
                elif node.name == "table":
                    # might be a sub-table inside description (rare) — keep text
                    desc_parts.append(text_of(node))
                elif node.name in ("dl", "ul", "ol"):
                    desc_parts.append(_list_to_md(node))
            elif isinstance(node, NavigableString):
                txt = str(node).strip()
                if txt:
                    desc_parts.append(txt)
            node = node.next_sibling
    if desc_parts:
        out.append("\n## 설명\n")
        out.append(collapse_ws("\n\n".join(desc_parts)))

    # Field summary
    fs = soup.find("a", attrs={"name": "field_summary"})
    if fs:
        out.append("\n## 필드 요약\n")
        out.append(_summary_table_to_md(fs))

    # Constructor summary
    cs = soup.find("a", attrs={"name": "constructor_summary"})
    if cs:
        out.append("\n## 생성자 요약\n")
        out.append(_summary_table_to_md(cs))

    # Method summary
    ms = soup.find("a", attrs={"name": "method_summary"})
    if ms:
        out.append("\n## 메서드 요약\n")
        out.append(_summary_table_to_md(ms))

    # Field detail
    fd = soup.find("a", attrs={"name": "field_detail"})
    if fd:
        out.append("\n## 필드 상세\n")
        out.append(_detail_to_md(fd))

    # Constructor detail
    cd = soup.find("a", attrs={"name": "constructor_detail"})
    if cd:
        out.append("\n## 생성자 상세\n")
        out.append(_detail_to_md(cd))

    # Method detail
    md = soup.find("a", attrs={"name": "method_detail"})
    if md:
        out.append("\n## 메서드 상세\n")
        out.append(_detail_to_md(md))

    return collapse_ws("\n".join(out)) + "\n"


def _list_to_md(el: Tag) -> str:
    parts: list[str] = []
    if el.name == "dl":
        # WIPI's javadoc nests Parameters:/Returns: blocks inside multiple
        # wrapping <dd>s and an inner <dl>. We walk ALL descendant dt/dd in
        # document order, deduped, using plain text for dt and inline-md for dd.
        all_pairs = el.find_all(["dt", "dd"])
        # Filter out "wrapper" dd's that only contain more dt/dd (no own text).
        own_text_pairs = []
        for p in all_pairs:
            # If this element has ANY descendant dt/dd, it's a wrapper — skip
            if p.find(["dt", "dd"], recursive=True):
                continue
            own_text_pairs.append(p)
        # Find prelude text: dl's direct text descendants that are NOT inside
        # any dt/dd. Walk dl's content as a string with all dt/dd removed.
        clone = BeautifulSoup(str(el), "lxml")
        outer = clone.find("dl")
        if outer:
            for inner in outer.find_all(["dt", "dd"]):
                inner.decompose()
            prelude = outer.get_text(" ", strip=True)
        else:
            prelude = ""
        prelude = re.sub(r"\s+", " ", prelude).strip()
        if prelude:
            parts.append(prelude)
        for p in own_text_pairs:
            if p.name == "dt":
                term = p.get_text(" ", strip=True).rstrip(":").strip()
                parts.append(f"\n**{term}:**")
            else:
                val = inline_to_md(p).strip()
                if val:
                    parts.append(f"- {val}")
        if not parts:
            return text_of(el)
        return "\n".join(parts)
    elif el.name in ("ul", "ol"):
        bullet = "-" if el.name == "ul" else "1."
        for li in el.find_all("li", recursive=False):
            parts.append(f"{bullet} {inline_to_md(li).strip()}")
        return "\n".join(parts)
    return text_of(el)


def _summary_table_to_md(anchor: Tag) -> str:
    """Summary table → flat markdown list. Each row becomes:
        - `<modifiers> name(args)` — description
    The full signature (with newlines) and modifiers are flattened to one line."""
    table = anchor.find_next("table")
    if not table:
        return ""
    rows = table.find_all("tr")
    out_rows = []
    for tr in rows[1:]:
        tds = tr.find_all("td", recursive=False)
        if len(tds) == 2:
            mod = text_of(tds[0])
            body = tds[1]
            code = body.find("code")
            if code is None:
                out_rows.append(f"- {text_of(body)}")
                continue
            sig_text = code.get_text(" ", strip=False)
            sig_text = re.sub(r"\s+", " ", sig_text).strip()
            desc_parts = []
            for sib in code.next_siblings:
                if isinstance(sib, NavigableString):
                    s = str(sib).strip()
                    if s:
                        desc_parts.append(s)
                elif isinstance(sib, Tag):
                    if sib.name == "br":
                        continue
                    desc_parts.append(inline_to_md(sib).strip())
            desc = re.sub(r"\s+", " ", " ".join(desc_parts)).strip()
            sig_line = f"{mod} {sig_text}".strip() if mod else sig_text
            if desc:
                out_rows.append(f"- `{sig_line}` — {desc}")
            else:
                out_rows.append(f"- `{sig_line}`")
        elif len(tds) == 1:
            out_rows.append(f"- {text_of(tds[0])}")
    return "\n".join(out_rows) + "\n"


def _detail_to_md(anchor: Tag) -> str:
    """Convert a detail block. The anchor is usually inside a <p> or similar
    wrapper, so we walk the parent's next siblings forward, not the anchor's
    direct siblings."""
    out: list[str] = []
    # Start from the element AFTER the wrapper that contains the anchor.
    start = anchor.parent if anchor.parent and anchor.parent.name != "body" else anchor
    node = start.next_sibling

    # Names of "stop" anchors — encountering one means we've moved into the
    # next major section (shouldn't happen for *_detail at end of doc, but safe).
    stop_names = {"navbar_bottom", "navbar_bottom_firstrow",
                  "skip-navbar_bottom"}

    while node is not None:
        if isinstance(node, Tag):
            # Stop if we entered the bottom navbar
            inner_a = node.find("a", attrs={"name": True}) if hasattr(node, "find") else None
            if inner_a and inner_a.get("name") in stop_names:
                break
            if node.name == "h3":
                out.append(f"\n### {text_of(node)}\n")
            elif node.name == "pre":
                out.append("\n```java\n" + node.get_text().strip() + "\n```\n")
            elif node.name in ("p", "div"):
                txt = inline_to_md(node).strip()
                if txt:
                    out.append(txt)
            elif node.name == "dl":
                out.append(_list_to_md(node))
            elif node.name in ("ul", "ol"):
                out.append(_list_to_md(node))
            elif node.name == "hr":
                pass
            elif node.name == "table":
                # Defensive: another summary table — stop
                cap = node.find("td")
                if cap and "Summary" in text_of(cap):
                    break
        node = node.next_sibling

    return "\n\n".join(p for p in out if p.strip()) + "\n"


AROMASOFT_FOOTER = re.compile(
    r"\n*\*\*\*AromaSoft Corp\. Proprietary and Confidential\*\*\*\s*\n+"
    r"\*\(C\)opyright \d{4} AromaSoft Corp\. All right reserved\.\s*\n"
    r"Contact : \[contact@aromasoft\.com\]\(mailto:contact@aromasoft\.com\)\*"
)


def strip_interior_footers(md: str) -> str:
    """Remove AromaSoft copyright footer blocks that appear mid-document.

    The source JavaDoc repeats the same footer on every class section. We keep
    only the trailing occurrence so each Markdown page ends with one footer.
    """
    matches = list(AROMASOFT_FOOTER.finditer(md))
    if len(matches) <= 1:
        return md
    parts: list[str] = []
    cursor = 0
    for m in matches[:-1]:
        parts.append(md[cursor:m.start()])
        cursor = m.end()
        while cursor < len(md) and md[cursor] == "\n":
            cursor += 1
    parts.append(md[cursor:])
    return re.sub(r"\n{3,}", "\n\n", "".join(parts))


def convert_package_summary(html: str, pkg: str) -> tuple[str, list[str]]:
    """Returns (markdown, list_of_class_names_found)."""
    soup = BeautifulSoup(html, "lxml")
    strip_nav(soup)
    out: list[str] = []
    out.append(f"# package {pkg}\n")

    # Package description — usually a paragraph below the H2 heading
    h2 = soup.find("h2")
    if h2:
        # Walk siblings collecting text until first table
        node = h2.next_sibling
        while node is not None and not (isinstance(node, Tag) and node.name == "table"):
            if isinstance(node, Tag) and node.name in ("p", "div"):
                txt = inline_to_md(node).strip()
                if txt:
                    out.append(txt)
            node = node.next_sibling

    # Tables of Interface Summary, Class Summary, etc.
    classes: list[str] = []
    for table in soup.find_all("table"):
        cap_cell = table.find("td")
        if not cap_cell:
            continue
        cap_text = text_of(cap_cell)
        section_titles = ("Interface Summary", "Class Summary", "Exception Summary",
                          "Error Summary", "Annotation Types Summary")
        title = next((t for t in section_titles if t in cap_text), None)
        if not title:
            continue
        out.append(f"\n## {title}\n")
        rows = table.find_all("tr")
        for tr in rows[1:]:
            tds = tr.find_all("td", recursive=False)
            if len(tds) >= 2:
                link = tds[0].find("a")
                name = text_of(link) if link else text_of(tds[0])
                desc = text_of(tds[1])
                if name:
                    classes.append(name)
                    out.append(f"- [{name}]({name}.md) — {desc}")

    return collapse_ws("\n".join(out)) + "\n", classes


# -------------------- Main pipeline --------------------

def main(src: str, dst: str) -> None:
    src_path = Path(src)
    dst_path = Path(dst)
    dst_path.mkdir(parents=True, exist_ok=True)

    def read_html(path: Path) -> str:
        data = path.read_bytes()
        m = re.search(rb"charset\s*=\s*['\"]?([\w-]+)", data[:2048], re.IGNORECASE)
        enc = m.group(1).decode("ascii").lower() if m else "utf-8"
        if enc in ("euc-kr", "euckr", "ks_c_5601-1987"):
            enc = "cp949"
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            return data.decode("cp949", errors="replace")

    pkg_list = (src_path / "package-list").read_text().strip().splitlines()
    pkg_list = [p.strip() for p in pkg_list if p.strip()]
    print(f"[javadoc] {len(pkg_list)} packages")

    index_lines = ["# Java API Reference\n",
                   "WIPI 1.2.1 JavaDoc을 Markdown으로 재구성한 레퍼런스입니다. "
                   "원본 JavaDoc은 [nikita36078/J2ME_Docs](https://github.com/nikita36078/J2ME_Docs) "
                   "에서 가져왔습니다.\n",
                   "## 패키지 목록\n"]

    total_classes = 0
    for pkg in pkg_list:
        pkg_path = src_path / pkg.replace(".", "/")
        summary_html = pkg_path / "package-summary.html"
        if not summary_html.exists():
            print(f"[javadoc] skip {pkg} — no package-summary.html")
            continue

        # Convert package summary
        md, classes = convert_package_summary(read_html(summary_html), pkg)

        # Filter to classes whose HTML actually exists (e.g. MIDP listings
        # include CLDC-inherited classes that aren't redocumented here).
        present_classes = [c for c in classes if (pkg_path / f"{c}.html").exists()]
        missing = set(classes) - set(present_classes)
        if missing:
            # Drop link lines pointing at missing classes so strict build passes.
            kept_lines: list[str] = []
            for line in md.splitlines():
                m = re.match(r"^- \[([^\]]+)\]\(([^)]+)\.md\)", line)
                if m and m.group(1) in missing:
                    continue
                kept_lines.append(line)
            md = "\n".join(kept_lines)

        # Write package-level index
        pkg_index = dst_path / pkg.replace(".", "/") / "index.md"
        pkg_index.parent.mkdir(parents=True, exist_ok=True)
        pkg_index.write_text(md, encoding="utf-8")
        index_lines.append(f"- [`{pkg}`]({pkg.replace('.', '/')}/index.md) "
                           f"({len(present_classes)} classes)")

        # Convert each present class
        for class_name in present_classes:
            class_html = pkg_path / f"{class_name}.html"
            md_class = convert_class_page(read_html(class_html),
                                          pkg, class_name)
            md_class = strip_interior_footers(md_class)
            out_file = dst_path / pkg.replace(".", "/") / f"{class_name}.md"
            out_file.write_text(md_class, encoding="utf-8")
            total_classes += 1

    (dst_path / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"[javadoc] wrote {total_classes} classes across {len(pkg_list)} packages")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
