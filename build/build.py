"""Rebuild index.html (offline, libraries inlined) from build/template.html.

    cd build && npm ci && python3 build.py
"""
import os
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
x = open(os.path.join(here, 'node_modules/xlsx/dist/xlsx.full.min.js'), encoding='utf-8').read()
e = open(os.path.join(here, 'node_modules/exceljs/dist/exceljs.min.js'), encoding='utf-8').read()
assert '</script' not in x.lower() and '</script' not in e.lower()
out = (t.replace('<!--LIB_XLSX-->', '<script>' + x + '</script>', 1)
        .replace('<!--LIB_EXCELJS-->', '<script>' + e + '</script>', 1))
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(out)
print('wrote index.html,', len(out), 'bytes')
