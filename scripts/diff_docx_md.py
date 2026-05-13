"""Find paragraphs present in docx outline but missing from md.

Heuristic: take each docx line, normalize (strip ws/punct), take a "fingerprint"
(first 30 chars of normalized text), and check whether md contains the same
fingerprint. Output orphans with context.

Usage: python diff_docx_md.py <docx_outline.txt> <md_file> > report.txt
"""
import sys, re

def normalize(s):
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[“”"\'`‘’()\[\]{}.,;:!?·•\-—–_/<>=*+]', '', s)
    return s

def fingerprints(text, n=20):
    return normalize(text)[:n]

def main(docx_txt, md_file):
    with open(docx_txt, encoding='utf-8') as f:
        docx_lines = [l.rstrip() for l in f]
    with open(md_file, encoding='utf-8') as f:
        md_text = f.read()
    md_norm = normalize(md_text)

    print('# Missing from md (present in docx)\n')
    skip_prefixes = ('[TABLE', '[IMG', '[Heading', '[Title')
    for i, line in enumerate(docx_lines, 1):
        ls = line.strip()
        if not ls:
            continue
        if ls.startswith(skip_prefixes):
            continue
        # skip TOC-style page numbers
        if re.match(r'^[\d.\s]+$', ls):
            continue
        fp = fingerprints(ls, 25)
        if len(fp) < 15:
            continue
        if fp not in md_norm:
            # print with surrounding context (prev + next)
            prev = docx_lines[i-2].strip() if i >= 2 else ''
            nxt = docx_lines[i].strip() if i < len(docx_lines) else ''
            print(f'L{i}: {ls[:180]}')
            print()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
