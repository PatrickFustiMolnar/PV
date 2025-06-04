#!/usr/bin/env python3
"""Extract plain text from all HTML files.

Parses each HTML document using BeautifulSoup and writes a `.txt` file with the
extracted text next to the original HTML file.

Run from repository root:
    python3 scripts/extract_text.py
"""
import os
try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit("BeautifulSoup (bs4) is required. Install with `pip install bs4`.")

for root, _, files in os.walk('.'):
    for fname in files:
        if fname.endswith('.html'):
            html_path = os.path.join(root, fname)
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                soup = BeautifulSoup(f, 'html.parser')
            text = soup.get_text(separator='\n').strip()
            txt_path = html_path[:-5] + '.txt'
            with open(txt_path, 'w', encoding='utf-8') as out:
                out.write(text)
            print('Extracted', txt_path)
