#!/usr/bin/env python3
"""Run all HTML cleanup steps sequentially."""
import subprocess
import sys

scripts = [
    'scripts/simplify_html.py',
    'scripts/remove_external_resources.py',
]

for script in scripts:
    print(f'Running {script}...')
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f'Error running {script}', file=sys.stderr)
        sys.exit(result.returncode)
print('Cleanup complete.')
