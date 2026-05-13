"""Dump docx as plain markdown-ish outline including image positions, tables.

Usage: python docx_to_outline.py <input.docx> <out.txt>
"""
import sys, os, zipfile, re
from xml.etree import ElementTree as ET

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
}

def text_of(el):
    parts = []
    for t in el.iter('{%s}t' % NS['w']):
        parts.append(t.text or '')
    # also handle line breaks
    return ''.join(parts)

def style_of(p):
    pPr = p.find('w:pPr', NS)
    if pPr is None:
        return ''
    pStyle = pPr.find('w:pStyle', NS)
    if pStyle is None:
        return ''
    return pStyle.get('{%s}val' % NS['w'], '')

def has_image(p, rels):
    # blip references
    for blip in p.iter('{%s}blip' % NS['a']):
        embed = blip.get('{%s}embed' % NS['r'])
        if embed and embed in rels:
            return rels[embed]
    return None

def load_rels(z):
    rels = {}
    try:
        with z.open('word/_rels/document.xml.rels') as f:
            tree = ET.parse(f)
        for rel in tree.getroot():
            rid = rel.get('Id')
            target = rel.get('Target')
            rels[rid] = target
    except KeyError:
        pass
    return rels

def cell_text(tc):
    paras = []
    for p in tc.findall('w:p', NS):
        paras.append(text_of(p))
    return ' '.join(p for p in paras if p)

def process_table(tbl, out):
    rows = []
    for tr in tbl.findall('w:tr', NS):
        cells = [cell_text(tc) for tc in tr.findall('w:tc', NS)]
        rows.append(cells)
    if not rows:
        return
    out.append('[TABLE start]')
    for r in rows:
        out.append(' | '.join(c.replace('\n', ' ').strip() for c in r))
    out.append('[TABLE end]')

def main(inp, outp):
    z = zipfile.ZipFile(inp)
    rels = load_rels(z)
    with z.open('word/document.xml') as f:
        tree = ET.parse(f)
    body = tree.getroot().find('w:body', NS)
    out = []
    for child in body:
        tag = child.tag.split('}')[1]
        if tag == 'p':
            s = style_of(child)
            txt = text_of(child).strip()
            img = has_image(child, rels)
            line = ''
            if s.startswith('Heading') or s.startswith('Title'):
                line = '[%s] %s' % (s, txt)
            elif txt:
                line = txt
            if img:
                line = (line + ' ' if line else '') + '[IMG %s]' % img
            if line:
                out.append(line)
        elif tag == 'tbl':
            process_table(child, out)
    with open(outp, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print('Wrote', outp, len(out), 'lines')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
