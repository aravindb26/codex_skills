#!/usr/bin/env python3
# Advanced file reader for audit agent
# Usage: read_file.py <file> [--start N] [--lines N] [--grep PATTERN] [--list]

import sys
import os
import argparse
import re

def read_file_slice(path, start=None, lines=None):
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            all_lines = f.readlines()
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}")
        return
    except PermissionError:
        print(f"ERROR: Permission denied: {path}")
        return
    except Exception as e:
        print(f"ERROR: Could not read file: {e}")
        return

    total = len(all_lines)
    if start is None:
        start = 1  # 1-indexed for human-friendly usage
    if start > total:
        print(f"ERROR: Start line {start} exceeds total lines ({total}).")
        return

    if lines is None:
        lines = total - start + 1

    end = min(start + lines - 1, total)
    selected = all_lines[start-1:end]

    print(f"--- {path} (lines {start}-{end} of {total}) ---")
    for line in selected:
        print(line, end='')
    print("\n--- end of slice ---")

def grep_file(path, pattern):
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            for idx, line in enumerate(f, 1):
                if re.search(pattern, line):
                    print(f"{idx}: {line}", end='')
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}")
    except PermissionError:
        print(f"ERROR: Permission denied: {path}")
    except Exception as e:
        print(f"ERROR: {e}")

def list_dir(directory):
    try:
        items = os.listdir(directory)
        print(f"Contents of {directory}:")
        for item in sorted(items):
            full = os.path.join(directory, item)
            tag = "DIR" if os.path.isdir(full) else "FILE"
            print(f"  [{tag}] {item}")
    except Exception as e:
        print(f"ERROR listing directory: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read files for audit agent")
    parser.add_argument("target", help="File path or directory (with --list)")
    parser.add_argument("--start", type=int, help="Start line (1-indexed)")
    parser.add_argument("--lines", type=int, help="Number of lines to read")
    parser.add_argument("--grep", help="Regex pattern to search for")
    parser.add_argument("--list", action="store_true", help="List directory contents instead of reading")

    args = parser.parse_args()

    if args.list:
        list_dir(args.target)
    elif args.grep:
        grep_file(args.target, args.grep)
    else:
        read_file_slice(args.target, args.start, args.lines)
