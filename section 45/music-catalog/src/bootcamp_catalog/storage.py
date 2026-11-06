"""JSON persistence for a single-writer teaching application."""
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from .core import validate_catalog

def load(path):
    path = Path(path)
    try:
        with path.open(encoding="utf-8") as source:
            return validate_catalog(json.load(source))
    except FileNotFoundError:
        return []

def save(path, records):
    clean = validate_catalog(records)
    path = Path(path)
    temporary = None
    try:
        # Write beside the target, then replace after closing (also works on Windows).
        with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                prefix=".catalog-", suffix=".tmp", delete=False) as target:
            temporary = Path(target.name)
            json.dump(clean, target, ensure_ascii=False, indent=2)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
