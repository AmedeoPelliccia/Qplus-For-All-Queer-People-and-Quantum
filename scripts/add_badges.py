#!/usr/bin/env python3
"""
add_badges.py — Replace TBD / DRAFT / To Be Completed with shields.io badges
in all markdown files across the 040, 041, 042 subsections.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TARGET_DIRS = [
    REPO_ROOT / "Q+ATLANTIDE/000-099_ATLAS/040-049_Avionica-Informacion-y-APU/040_Multisystem",
    REPO_ROOT / "Q+ATLANTIDE/000-099_ATLAS/040-049_Avionica-Informacion-y-APU/041_Water-Ballast",
    REPO_ROOT / "Q+ATLANTIDE/000-099_ATLAS/040-049_Avionica-Informacion-y-APU/042_Integrated-Modular-Avionics",
]

BADGE_TBD   = '<img src="https://img.shields.io/badge/TBD-red" alt="TBD">'
BADGE_DRAFT = '<img src="https://img.shields.io/badge/DRAFT-yellow" alt="DRAFT">'
BADGE_TBC   = '<img src="https://img.shields.io/badge/To_Be_Completed-orange" alt="To Be Completed">'


def split_frontmatter(text):
    """
    Returns (frontmatter_text, body_text).
    frontmatter_text includes the opening and closing --- delimiters.
    """
    if not text.startswith("---"):
        return ("", text)
    # find second ---
    second = text.find("\n---", 3)
    if second == -1:
        return ("", text)
    end = second + 4  # past the closing ---
    # consume trailing newline
    if end < len(text) and text[end] == "\n":
        end += 1
    return (text[:end], text[end:])


def split_into_segments(body):
    """
    Split body into segments: regular text and fenced code blocks.
    Returns list of (is_code_block, text) tuples.
    """
    segments = []
    pattern = re.compile(r"(```[^\n]*\n.*?```)", re.DOTALL)
    last = 0
    for m in pattern.finditer(body):
        before = body[last:m.start()]
        if before:
            segments.append((False, before))
        segments.append((True, m.group(0)))
        last = m.end()
    tail = body[last:]
    if tail:
        segments.append((False, tail))
    return segments


def process_table_line(line):
    """
    Process a markdown table line (contains |).
    Replace cells that are exactly 'TBD' with badge.
    Also replace DRAFT cells and To Be Completed cells.
    """
    # Split by |
    parts = line.split("|")
    new_parts = []
    for i, part in enumerate(parts):
        stripped = part.strip()
        if stripped == "TBD":
            # preserve surrounding whitespace structure
            new_parts.append(part.replace("TBD", BADGE_TBD, 1))
        elif stripped == "DRAFT":
            new_parts.append(part.replace("DRAFT", BADGE_DRAFT, 1))
        elif stripped == "To Be Completed":
            new_parts.append(part.replace("To Be Completed", BADGE_TBC, 1))
        else:
            new_parts.append(part)
    return "|".join(new_parts)


def process_prose_line(line):
    """
    Process a non-table prose line.
    Replace TBD, DRAFT, To Be Completed with badges,
    but NOT inside link destinations ](...)  or inside backtick code spans.
    """
    # First replace 'To Be Completed' (longest match first)
    line = re.sub(r"\bTo Be Completed\b", BADGE_TBC, line)

    # Replace DRAFT with badge — but skip if inside link parens or backtick
    # We use a lookahead/lookbehind approach: don't replace inside ](...)
    # Strategy: tokenise around link syntax and backtick spans, replace only in text parts

    def replace_word(line, word, badge):
        result = []
        i = 0
        # Regex to find the word but skip inside ](...) and `...`
        # We'll scan character by character tracking context
        pattern_word = re.compile(r'\b' + re.escape(word) + r'\b')
        # Find all candidate positions
        for m in pattern_word.finditer(line):
            start, end = m.start(), m.end()
            # Check if inside a link destination ](...)
            # Look backwards for ]( and forwards for )
            before = line[:start]
            inside_link = bool(re.search(r'\]\([^)]*$', before))
            # Check if inside backtick span
            # Count backticks before start (odd = inside code span)
            backtick_count = before.count('`')
            inside_code = (backtick_count % 2 == 1)
            if not inside_link and not inside_code:
                result.append((start, end))
        # Apply replacements in reverse to preserve indices
        line_list = list(line)
        for start, end in reversed(result):
            line_list[start:end] = list(badge)
        return "".join(line_list)

    line = replace_word(line, "DRAFT", BADGE_DRAFT)
    line = replace_word(line, "TBD", BADGE_TBD)
    return line


def process_body(body):
    segments = split_into_segments(body)
    out = []
    for is_code, text in segments:
        if is_code:
            out.append(text)
        else:
            lines = text.split("\n")
            new_lines = []
            for line in lines:
                if "|" in line and not line.strip().startswith("```"):
                    new_lines.append(process_table_line(line))
                else:
                    new_lines.append(process_prose_line(line))
            out.append("\n".join(new_lines))
    return "".join(out)


def process_file(path):
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    new_body = process_body(body)
    if new_body != body:
        path.write_text(fm + new_body, encoding="utf-8")
        print(f"  UPDATED: {path.name}")
    else:
        print(f"  unchanged: {path.name}")


def main():
    total = 0
    for d in TARGET_DIRS:
        if not d.exists():
            print(f"WARNING: directory not found: {d}", file=sys.stderr)
            continue
        md_files = [f for f in sorted(d.glob("*.md")) if f.name != "README.md"]
        print(f"\n=== {d.name} ({len(md_files)} files) ===")
        for f in md_files:
            process_file(f)
            total += 1
    print(f"\nDone. Processed {total} file(s).")


if __name__ == "__main__":
    main()
