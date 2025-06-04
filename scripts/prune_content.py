#!/usr/bin/env python3
"""Prune repository content to keep only lessons and exercises.

This script removes image files, deletes directories that do not appear to
contain lesson or exercise material, and ensures no directory contains more
than 100 files by moving overflow into numbered subfolders.

Run with `--dry-run` to preview actions without modifying files.

Example:
    python3 scripts/prune_content.py --dry-run
"""
import os
import argparse
import shutil

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.ico'}
KEEP_EXTS = {'.html', '.css', '.js'}

LESSON_KEYWORDS = {'lesson', 'lessons', 'exercise', 'exercises'}

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--dry-run', action='store_true', help='Show actions without writing changes')
args = parser.parse_args()

def is_lesson_dir(path):
    name = os.path.basename(path).lower()
    return any(key in name for key in LESSON_KEYWORDS)

for root, dirs, files in os.walk('.', topdown=False):
    # Remove unwanted files
    for fname in list(files):
        _, ext = os.path.splitext(fname)
        if ext.lower() in IMAGE_EXTS:
            path = os.path.join(root, fname)
            if args.dry_run:
                print('Would remove', path)
            else:
                os.remove(path)
                print('Removed', path)
        elif ext.lower() not in KEEP_EXTS:
            path = os.path.join(root, fname)
            if args.dry_run:
                print('Would remove', path)
            else:
                os.remove(path)
                print('Removed', path)

    # Delete directories without lesson keywords
    for d in list(dirs):
        path = os.path.join(root, d)
        if not is_lesson_dir(path):
            if args.dry_run:
                print('Would delete directory', path)
            else:
                shutil.rmtree(path, ignore_errors=True)
                print('Deleted directory', path)

    # After removals, enforce max 100 files per directory
    remaining = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
    if len(remaining) > 100:
        count = 0
        batch_index = 1
        batch_dir = os.path.join(root, f'batch_{batch_index}')
        if not args.dry_run:
            os.makedirs(batch_dir, exist_ok=True)
        for fname in remaining:
            count += 1
            if count > 100:
                target = os.path.join(batch_dir, fname)
                src = os.path.join(root, fname)
                if args.dry_run:
                    print('Would move', src, 'to', target)
                else:
                    shutil.move(src, target)
                if count - 100 >= 100:
                    batch_index += 1
                    batch_dir = os.path.join(root, f'batch_{batch_index}')
                    if not args.dry_run:
                        os.makedirs(batch_dir, exist_ok=True)
        if not args.dry_run:
            print('Moved files into', batch_dir, 'for directory', root)
