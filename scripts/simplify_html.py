#!/usr/bin/env python3
"""Simplify HTML files by removing HTTrack comments and remote references.

Run from repository root:
    python3 scripts/simplify_html.py
"""
import os
import re

HTTRACK_COMMENT_RE = re.compile(r'<!--\s*Mirrored from.*?-->', re.DOTALL)
REMOTE_PATTERNS = [
    re.compile(r'https?://[^"\']*google-analytics[^"\']*'),
    re.compile(r'https?://[^"\']*googletagmanager[^"\']*'),
    re.compile(r'https?://translate\.google\.com[^"\']*'),
    re.compile(r'https?://www\.google\.com[^"\']*'),
    re.compile(r'https?://fonts\.googleapis\.com[^"\']*'),
]

for root, _, files in os.walk('.'):
    for fname in files:
        if fname.endswith('.html'):
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
            original = text
            text = HTTRACK_COMMENT_RE.sub('', text)
            for pattern in REMOTE_PATTERNS:
                text = pattern.sub('', text)
            if text != original:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print('Simplified', path)
