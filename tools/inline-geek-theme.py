#!/usr/bin/env python3
"""Push geek-theme.css into the inline <style> block of every page that uses it.

geek-theme.css is the single source of truth. The landing pages live in
separate git repos, so instead of <link>ing a shared stylesheet across
repo/host boundaries they each carry a verbatim inlined copy, fenced between:

    /* @geek-theme:start */
    ...generated, do not hand-edit...
    /* @geek-theme:end */

Page-specific rules go *after* the end marker and are never touched.

Usage:  python3 tools/inline-geek-theme.py [--check]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "geek-theme.css"

# This repo's page, plus the sibling repo checked out next to this one.
TARGETS = [
    ROOT / "projects" / "index.html",
    ROOT.parent / "claude-status-bar" / "index.html",
]

START = "/* @geek-theme:start */"
END = "/* @geek-theme:end */"
BLOCK = re.compile(
    re.escape(START) + r".*?" + re.escape(END), re.DOTALL
)


def payload() -> str:
    """geek-theme.css with its file-level header comment stripped."""
    css = SOURCE.read_text()
    header_end = css.index("*/") + 2
    return css[header_end:].strip("\n")


def main() -> int:
    check = "--check" in sys.argv
    body = payload()
    replacement = f"{START}\n{body}\n{END}"
    stale = []

    for target in TARGETS:
        if not target.exists():
            print(f"skip   {target} (not checked out)")
            continue
        html = target.read_text()
        if not BLOCK.search(html):
            print(f"ERROR  {target}: no @geek-theme markers found")
            return 1
        updated = BLOCK.sub(lambda _: replacement, html, count=1)
        if updated == html:
            print(f"ok     {target}")
            continue
        stale.append(target)
        if check:
            print(f"STALE  {target}")
        else:
            target.write_text(updated)
            print(f"wrote  {target}")

    if check and stale:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
