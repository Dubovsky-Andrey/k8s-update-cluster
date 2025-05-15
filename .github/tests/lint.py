#!/usr/bin/env python3
import os
import sys
import regex

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <directory-to-scan>")
    sys.exit(2)

start_dir = sys.argv[1]
if not os.path.isdir(start_dir):
    print(f"Error: '{start_dir}' is not a directory or does not exist.")
    sys.exit(2)

print("Scanning directory:", start_dir)

cyr_pattern      = regex.compile(r'\p{Cyrillic}')
emoji_pattern    = regex.compile(r'\p{Extended_Pictographic}')
emoticon_pattern = regex.compile(r'[:;=8][\-~^]?[)(DPp]')

errors = []
for root, dirs, files in os.walk(start_dir):
    for name in files:
        path = os.path.join(root, name)

        if cyr_pattern.search(name):
            errors.append(f"{path}  # filename contains Cyrillic")

        try:
            with open(path, encoding='utf-8', errors='ignore') as f:
                for num, line in enumerate(f, 1):
                    if (cyr_pattern.search(line)
                        or emoji_pattern.search(line)
                        or emoticon_pattern.search(line)):
                        errors.append(f"{path}:{num}:{line.strip()}")
        except OSError:
            continue

if errors:
    print("Found Cyrillic or emoji in:")
    print("\n".join(errors))
    sys.exit(1)
else:
    print("No Cyrillic or emoji found")
    sys.exit(0)
