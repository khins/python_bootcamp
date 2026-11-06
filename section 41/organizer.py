"""Teaching CLI: preview by default; --apply copies top-level files into groups.
Originals remain in place. Existing targets are rejected, never overwritten.
This is a single-user example, not a defense against hostile concurrent changes.
"""
import argparse
from pathlib import Path
import shutil
import sys

def plan(root):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("source must be a directory")
    actions = []
    for source in sorted(root.iterdir()):
        if source.is_symlink() or not source.is_file():
            continue
        group = "text" if source.suffix.lower() == ".txt" else "other"
        destination = root / "organized" / group / source.name
        if not destination.resolve().is_relative_to(root):
            raise ValueError("destination escapes source directory")
        actions.append((source, destination))
    return actions

def apply(actions):
    # Preflight the entire plan before starting. Failures during copying can
    # still leave earlier copies; this example is not a transaction.
    for source, target in actions:
        if target.exists() or target.is_symlink():
            raise FileExistsError(target)
    for source, target in actions:
        target.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation prevents overwriting even if a target just appeared.
        with source.open("rb") as incoming, target.open("xb") as outgoing:
            shutil.copyfileobj(incoming, outgoing)

def main(argv=None):
    parser = argparse.ArgumentParser(description="Preview or copy files into extension groups")
    parser.add_argument("source", type=Path)
    parser.add_argument("--apply", action="store_true", help="copy files; default only previews")
    args = parser.parse_args(argv)
    try:
        actions = plan(args.source)
        for source, target in actions:
            print(f"{source.name} -> {target.relative_to(args.source.resolve())}")
        if args.apply:
            apply(actions)
        print(f"{'Copied' if args.apply else 'Planned'} {len(actions)} file(s)")
        return 0
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
