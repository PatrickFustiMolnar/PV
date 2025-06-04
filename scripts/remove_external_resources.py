#!/usr/bin/env python3
"""Cleanup tool to remove external resources from HTML files.

Searches for common CDN or analytics URLs and strips them out. Remote
images are swapped with local copies when available.

Run from the repository root:
    python3 scripts/remove_external_resources.py
"""
import os
import re

REMOVE_PATTERNS = [
    re.compile(r'https?://[^"\']*google-analytics[^"\']*'),
    re.compile(r'https?://fonts\.googleapis\.com[^"\']*'),
    re.compile(r'https?://cdn\.snigelweb\.com[^"\']*'),
    re.compile(r'https?://www\.googletagservices\.com[^"\']*'),
    re.compile(r'https?://oss\.maxcdn\.com[^"\']*'),
]

REPLACEMENTS = {
    r'https://www\.w3schools\.com/images/w3schools_logo_436_2\.png': 'images/w3schools_logo.png',
    r'https://www\.w3schools\.com/images/colorpicker2000\.png': 'images/colorpicker.png',
}

for root, _, files in os.walk('.'):
    for fname in files:
        if fname.endswith('.html'):
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
            original = text
            for pattern in REMOVE_PATTERNS:
                text = pattern.sub('', text)
            for pattern, repl in REPLACEMENTS.items():
                text = re.sub(pattern, repl, text)
            if text != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print('Updated', path)
