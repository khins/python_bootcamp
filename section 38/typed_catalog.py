"""Small fully annotated catalog core for the section 38 checker exercise."""
from collections.abc import Iterable
from typing import TypedDict

class Listen(TypedDict):
    artist: str
    seconds: int

def summarize(records: Iterable[Listen]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for row in records:
        if type(row["seconds"]) is not int or row["seconds"] < 0:
            raise ValueError("seconds must be a nonnegative integer")
        if not row["artist"].strip():
            raise ValueError("artist is required")
        artist = row["artist"].strip()
        totals[artist] = totals.get(artist, 0) + row["seconds"]
    return totals

def example_project() -> None:
    rows: list[Listen] = [{"artist": "Rush", "seconds": 200}]
    print(summarize(rows))  # => {'Rush': 200}

# example_project()
