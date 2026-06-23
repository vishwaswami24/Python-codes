"""File organizer for this repo (d:/Python).

Moves (or copies) files from the project root into existing category folders
based on simple keyword/extension rules.

Usage:
  python file_organizer.py --dry-run
  python file_organizer.py

Defaults:
  - source: d:/Python
  - destination root: d:/Python
  - action: move
"""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Rule:
    dest: str
    keywords: tuple[str, ...] = ()
    extensions: tuple[str, ...] = ()


# Default mapping (keyword-based + a few extension-based rules)
RULES: tuple[Rule, ...] = (
    # Electronics + FFT examples
    Rule(dest="electronics", keywords=("fft", "electronics"), extensions=(".py",)),

    # Demos: html + rainbow patterns etc.
    Rule(dest="demos", keywords=("demo", "rainbow"), extensions=(".html", ".py")),

    # Games/mini-games
    Rule(dest="games", keywords=("minion", "game", "spiderman"), extensions=(".py",)),

    # OOP examples
    Rule(dest="oop", keywords=("oop", "inheritance", "encapsulation", "abstraction", "polymorphism"), extensions=(".py",)),

    # Strings: explicit string-focused scripts
    Rule(dest="strings", keywords=("string", "palindrome", "anagram", "vowel", "consonent", "character", "tokenizer"), extensions=(".py",)),

    # Algorithms: things like graphs
    Rule(dest="algorithms", keywords=("graph", "tokenizer", "challenge"), extensions=(".py",)),

    # Math-ish buckets
    Rule(dest="math", keywords=(
        "prime", "factorial", "fibonacci", "armstrong", "palindrome", "digit sum", "digitsum", "n^n",
        "emi", "triangle", "n^n", "range", "summation", "table",
        "balance", "scale", "math module", "range function",
    ), extensions=(".py",)),

    # Files: anything related to file IO demos
    Rule(dest="files", keywords=("file", "open function"), extensions=(".py", ".txt", ".csv")),

    # Utils fallback for miscellaneous modules/utilities
    Rule(dest="utils", keywords=("utils", "os module", "random module", "date time module", "built in"), extensions=(".py",)),
)


DEFAULT_SOURCE = Path("d:/Python")
DEST_ROOT = Path("d:/Python")


def infer_prog1_name(p: Path) -> str | None:
    """Infer better filename for known/legacy scripts.

    Currently only covers a small subset (can be extended).
    """
    try:
        text = p.read_text(encoding="utf-8", errors="ignore").lower()
    except Exception:
        return None

    if p.stem.lower() == "prog1":
        # Based on utils/prog1.py content (options for +,-,*,/) 
        if "multiplication" in text and "division" in text and "subtration" in text:
            return "arithmetic_menu.py"
        if "addition" in text and "subtration" in text and "multiplication" in text and "division" in text:
            return "arithmetic_menu.py"
    return None


def normalize_filename(name: str) -> str:
    # Keep extension already handled elsewhere; normalize base name only.
    # Replace spaces with underscores and strip leading/trailing underscores.
    return name.strip().replace(" ", "_")



def _normalize_name(p: Path) -> str:
    return p.name.lower().replace("-", " ")


def _iter_source_files(source: Path) -> Iterable[Path]:
    for p in source.iterdir():
        if p.is_file() and p.name != "file_organizer.py":
            yield p


def pick_destination(p: Path, rules: Iterable[Rule]) -> str | None:
    name = _normalize_name(p)
    ext = p.suffix.lower()

    for rule in rules:
        if rule.extensions and ext not in rule.extensions:
            continue
        if rule.keywords:
            if any(k in name for k in rule.keywords):
                return rule.dest
        else:
            # extension-only rule
            if rule.extensions and ext in rule.extensions:
                return rule.dest

    # default fallback: keep README in place, otherwise utils
    if p.name.lower() == "readme.md":
        return None
    return "utils"


def ensure_dest_dir(dest_root: Path, dest: str) -> Path:
    d = dest_root / dest
    d.mkdir(parents=True, exist_ok=True)
    return d


def move_or_copy(src: Path, dest_dir: Path, dry_run: bool, action: str) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / src.name

    if target.exists():
        # Avoid clobbering: add suffix
        stem = src.stem
        suffix = src.suffix
        i = 1
        while True:
            candidate = dest_dir / f"{stem}__{i}{suffix}"
            if not candidate.exists():
                target = candidate
                break
            i += 1

    if dry_run:
        print(f"[DRY] {action.upper()}: {src} -> {target}")
        return

    if action == "copy":
        shutil.copy2(src, target)
    elif action == "move":
        shutil.move(str(src), str(target))
    else:
        raise ValueError(f"Unknown action: {action}")


def maybe_rename_in_dest_files(dest_root: Path) -> None:
    """Rename known legacy filenames inside category folders."""
    # Only rename in known category dirs we manage.
    category_dirs = [
        "utils", "math", "strings", "oop", "games", "algorithms", "electronics", "demos", "files",
    ]

    for cat in category_dirs:
        d = dest_root / cat
        if not d.exists():
            continue
        for p in d.iterdir():
            if not p.is_file():
                continue
            new_stem = infer_prog1_name(p)
            if not new_stem:
                continue
            # Keep same extension.
            new_name = normalize_filename(new_stem)
            if not new_name.lower().endswith(p.suffix.lower()):
                new_name = new_name + p.suffix


            target = p.with_name(new_name)
            if target.exists():
                continue
            shutil.move(str(p), str(target))
            print(f"Renamed: {p} -> {target}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rename", action="store_true", help="Rename files in destination folders using inference rules")

    parser.add_argument("--source", type=str, default=str(DEFAULT_SOURCE))
    parser.add_argument("--dest-root", type=str, default=str(DEST_ROOT))
    parser.add_argument("--action", type=str, default="move", choices=["move", "copy"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source = Path(args.source)
    dest_root = Path(args.dest_root)

    if not source.exists():
        raise SystemExit(f"Source not found: {source}")

    for p in _iter_source_files(source):
        dest = pick_destination(p, RULES)
        if dest is None:
            continue
        dest_dir = ensure_dest_dir(dest_root, dest)
        move_or_copy(p, dest_dir, dry_run=args.dry_run, action=args.action)


if __name__ == "__main__":
    main()

