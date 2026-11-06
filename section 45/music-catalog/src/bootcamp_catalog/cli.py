"""CLI translates arguments/errors; the core and storage do the actual work."""
import argparse
from pathlib import Path
import sys
from .core import add_record, labels
from .storage import load, save

def main(argv=None):
    parser = argparse.ArgumentParser(description="Manage a local teaching music catalog")
    parser.add_argument("--catalog", type=Path, default=Path("catalog.json"))
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    add = commands.add_parser("add")
    add.add_argument("title")
    add.add_argument("artist")
    add.add_argument("year", type=int)
    args = parser.parse_args(argv)
    try:
        records = load(args.catalog)
        if args.command == "add":
            records = add_record(records, args.title, args.artist, args.year)
            save(args.catalog, records)
            print("Added 1 album")
        else:
            for label in labels(records):
                print(label)
        return 0
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
