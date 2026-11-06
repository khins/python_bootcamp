"""Business rules: no printing, CLI parsing, or filesystem access."""
def validate_record(record):
    if not isinstance(record, dict):
        raise ValueError("record must be an object")
    title, artist, year = record.get("title"), record.get("artist"), record.get("year")
    if any(not isinstance(value, str) or not value.strip() for value in (title, artist)):
        raise ValueError("title and artist are required")
    if type(year) is not int or not 1800 <= year <= 2100:
        raise ValueError("year must be an integer from 1800 to 2100")
    return {"title": title.strip(), "artist": artist.strip(), "year": year}

def validate_catalog(records):
    if not isinstance(records, list):
        raise ValueError("catalog must be a list")
    result, seen = [], set()
    for record in records:
        item = validate_record(record)
        key = (item["title"].casefold(), item["artist"].casefold())
        if key in seen:
            raise ValueError("duplicate album")
        seen.add(key)
        result.append(item)
    return result

def add_record(records, title, artist, year):
    return validate_catalog([*records, {"title": title, "artist": artist, "year": year}])

def labels(records):
    return [f"{r['title']} by {r['artist']} ({r['year']})" for r in validate_catalog(records)]
