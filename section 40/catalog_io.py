"""Validated JSON/CSV interchange; used by the section 40 worked project."""
import csv
import json

def validate(rows):
    if not isinstance(rows, list):
        raise ValueError("catalog must be a list")
    clean = []
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError(f"row {index}: expected an object")
        title, artist, year = row.get("title"), row.get("artist"), row.get("year")
        if any(not isinstance(v, str) or not v.strip() for v in (title, artist)):
            raise ValueError(f"row {index}: title and artist are required")
        if type(year) is not int or not 1800 <= year <= 2100:
            raise ValueError(f"row {index}: invalid year")
        clean.append({"title": title.strip(), "artist": artist.strip(), "year": year})
    return clean

def load_json(path):
    with open(path, encoding="utf-8") as source:
        return validate(json.load(source))

def save_json(path, rows):
    clean = validate(rows)  # Validate BEFORE opening/truncating the destination.
    with open(path, "w", encoding="utf-8") as destination:
        json.dump(clean, destination, ensure_ascii=False, indent=2, allow_nan=False)

def save_csv(path, rows):
    clean = validate(rows)
    with open(path, "w", encoding="utf-8", newline="") as destination:
        writer = csv.DictWriter(destination, fieldnames=["title", "artist", "year"])
        writer.writeheader()
        writer.writerows(clean)

def load_csv(path):
    with open(path, encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != ["title", "artist", "year"]:
            raise ValueError("expected title,artist,year header")
        rows = []
        for index, row in enumerate(reader, 1):
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f"row {index}: wrong number of columns")
            try:
                row["year"] = int(row["year"])
            except ValueError as error:
                raise ValueError(f"row {index}: invalid year") from error
            rows.append(row)
    return validate(rows)
