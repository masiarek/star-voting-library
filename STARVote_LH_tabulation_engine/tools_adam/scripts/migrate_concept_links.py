#!/usr/bin/env python3
"""Move concept folders and repair every reference to them, repo-wide.

Usage:  migrate_links.py --move OLD=NEW [--move OLD=NEW ...] [--apply]

Without --apply it is a dry run: it prints what would change and touches nothing.

Two passes, in this order (the order matters):

  1. LINK PASS — for every Markdown/HTML link in every text file, resolve the
     target against the *source file's* directory to a repo-relative path. If
     that path lands inside a moved folder, remap it and recompute the relative
     path from the source's own (possibly also moved) new location. This is the
     only correct way to handle `../../07_Concepts/X/y.md` style links, whose
     correct rewrite depends on where the *linking* file sits.

  2. LITERAL PASS — plain-replace any remaining literal `OLD/` strings. These
     are prose and source-code mentions written as repo-relative paths
     ("see 06_Other/RCV_IRV/concepts/foo.md"), plus published site URLs. Safe only
     because pass 1 already rewrote real links into new relative paths that no
     longer contain the old prefix.
"""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent  # overridden by --repo
TEXT_EXT = {".md", ".py", ".yaml", ".yml", ".json", ".txt", ".css", ".html"}
SKIP_DIRS = {".git", "site", ".venv", "__pycache__", ".claude", "node_modules"}

# Frozen BetterVoting exports are NOT repo files — they are the immutable record
# of what BV permanently stores, and BV descriptions can never be edited. Rewriting
# a path inside one makes it assert something BV never said, and (worse) hides the
# fact that the live description now names a folder that no longer exists. The
# 2026-08-02 reorganization did exactly that to 22 of them, because ".json" is in
# TEXT_EXT: the frozen copies read "01_STAR/05_Practice/" while BV still says
# "01_STAR/exercises/". Never migrate these.
SKIP_FILE_SUFFIXES = ("_bv_export.json",)

# [text](target)  and  [text]: target  and  src="target" / href="target"
MD_LINK = re.compile(r"(\[[^\]]*\]\()([^)\s]+?)((?:\s+\"[^\"]*\")?\))")
MD_REFDEF = re.compile(r"^(\s*\[[^\]]+\]:\s+)(\S+)", re.M)
HTML_ATTR = re.compile(r"((?:src|href)=[\"'])([^\"'#?]+)([\"'])")


def iter_text_files(repo: Path):
    for dirpath, dirnames, filenames in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.name.endswith(SKIP_FILE_SUFFIXES):
                continue
            if p.suffix.lower() in TEXT_EXT:
                yield p


def remap_path(rel: str, moves: list[tuple[str, str]]) -> str | None:
    """If repo-relative `rel` lands inside a moved folder, return its new path."""
    rel = posixpath.normpath(rel)
    for old, new in moves:
        if rel == old:
            return new
        if rel.startswith(old + "/"):
            return new + rel[len(old):]
    return None


def new_location_of(path_rel: str, moves: list[tuple[str, str]]) -> str:
    return remap_path(path_rel, moves) or path_rel


def rewrite_link(target: str, src_rel: str, moves: list[tuple[str, str]]) -> str | None:
    """Return the rewritten link target, or None if unchanged."""
    if not target or target.startswith(("http://", "https://", "#", "mailto:", "//")):
        return None
    frag = ""
    if "#" in target:
        target, frag = target.split("#", 1)
        frag = "#" + frag
    if not target:
        return None
    trailing_slash = target.endswith("/")

    src_dir = posixpath.dirname(src_rel)
    if posixpath.isabs(target):
        return None
    resolved = posixpath.normpath(posixpath.join(src_dir, target))
    if resolved.startswith(".."):
        return None  # points outside the repo; leave alone

    dest_new = remap_path(resolved, moves)
    src_new = new_location_of(src_rel, moves)
    if dest_new is None and src_new == src_rel:
        return None  # neither end moved

    dest_final = dest_new if dest_new is not None else resolved
    src_dir_new = posixpath.dirname(src_new)
    out = posixpath.relpath(dest_final, src_dir_new or ".")
    if trailing_slash and not out.endswith("/"):
        out += "/"
    if out == target and not frag:
        return None
    return out + frag


def process(repo: Path, moves: list[tuple[str, str]], apply: bool, exclude: set[str] | None = None):
    link_edits = 0
    literal_edits = 0
    files_changed: dict[Path, tuple[int, int]] = {}

    for path in iter_text_files(repo):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        src_rel = path.relative_to(repo).as_posix()
        if exclude and src_rel in exclude:
            continue
        original = text
        n_link = 0

        def sub_md(m):
            nonlocal n_link
            new = rewrite_link(m.group(2), src_rel, moves)
            if new is None:
                return m.group(0)
            n_link += 1
            return m.group(1) + new + m.group(3)

        def sub_ref(m):
            nonlocal n_link
            new = rewrite_link(m.group(2), src_rel, moves)
            if new is None:
                return m.group(0)
            n_link += 1
            return m.group(1) + new

        def sub_html(m):
            nonlocal n_link
            new = rewrite_link(m.group(2), src_rel, moves)
            if new is None:
                return m.group(0)
            n_link += 1
            return m.group(1) + new + m.group(3)

        if path.suffix.lower() in {".md", ".html"}:
            text = MD_LINK.sub(sub_md, text)
            text = MD_REFDEF.sub(sub_ref, text)
            text = HTML_ATTR.sub(sub_html, text)

        # Pass 2: literal repo-relative mentions left in prose / code.
        #
        # PUBLISHED URLs ARE EXEMPT. A https://masiarek.github.io/... link that
        # already went out — above all inside a permanent BetterVoting election
        # description, which can never be edited after publication — must keep
        # naming the URL that was actually published. Repointing the source
        # would make it a false record of a live page we cannot change. The
        # mkdocs redirect is what keeps those old URLs resolving. So mask them
        # out of the literal pass and restore them untouched.
        masked: list[str] = []

        def _mask(m):
            masked.append(m.group(0))
            return f"\x00URL{len(masked) - 1}\x00"

        text = re.sub(r"https?://masiarek\.github\.io/[^\s\"'()\]]*", _mask, text)

        n_lit = 0
        for old, new in moves:
            if old in text:
                n_lit += text.count(old)
                text = text.replace(old, new)

        if masked:
            text = re.sub(r"\x00URL(\d+)\x00", lambda m: masked[int(m.group(1))], text)

        if text != original:
            files_changed[path] = (n_link, n_lit)
            link_edits += n_link
            literal_edits += n_lit
            if apply:
                path.write_text(text, encoding="utf-8")

    return files_changed, link_edits, literal_edits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--move", action="append", required=True,
                    help="OLD=NEW, repo-relative directory paths")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--exclude", action="append", default=[],
                    help="repo-relative file to leave completely untouched. Use for "
                         "mkdocs.yml when renaming a folder: its redirect_maps SOURCE "
                         "keys are historical URLs that must keep naming the old path, "
                         "and rewriting them would point every redirect at a URL that "
                         "never existed. Hand-edit such files instead.")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    moves = []
    for spec in args.move:
        old, _, new = spec.partition("=")
        moves.append((old.strip("/"), new.strip("/")))
    # Longest prefix first so nested moves resolve correctly.
    moves.sort(key=lambda t: len(t[0]), reverse=True)

    files, nl, nlit = process(repo, moves, args.apply, {e.strip('/') for e in args.exclude})
    verb = "REWROTE" if args.apply else "would rewrite"
    if not args.quiet:
        for p in sorted(files):
            a, b = files[p]
            print(f"  {p.relative_to(repo)}  links:{a} literals:{b}")
    print(f"\n{verb} {len(files)} files — {nl} link targets, {nlit} literal path mentions")
    if not args.apply:
        print("(dry run — pass --apply to write)")


if __name__ == "__main__":
    main()
