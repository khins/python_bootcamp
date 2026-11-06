# Bootcamp music catalog

A local teaching package. No network service or credentials are required.

From the repository root, using your virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -e "section 45/music-catalog"
.\.venv\Scripts\python.exe -m bootcamp_catalog --help
.\.venv\Scripts\bootcamp-catalog.exe --catalog "section 45/demo-catalog.json" list
.\.venv\Scripts\bootcamp-catalog.exe --catalog "section 45/demo-catalog.json" add "Signals" "Rush" 1982
.\.venv\Scripts\bootcamp-catalog.exe --catalog "section 45/demo-catalog.json" list
```

The add command creates/updates the explicitly selected catalog file. List does
not create a missing file. Duplicate title/artist pairs are rejected. Corrupt
existing data is reported, never silently replaced with an empty catalog.

Build with `python -m build "section 45/music-catalog"` from the repository root,
using the same environment's interpreter. Install the resulting wheel into a
separate environment to test distribution independently from the source tree.
This teaching JSON store is for one writer at a time, not concurrent writers.
