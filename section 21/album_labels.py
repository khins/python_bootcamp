# Optional challenge — Append album labels and return a count
# Write your code below:
# Work through this one together when you are ready.
# Define append_album_log(path, albums).
from pathlib import Path

APPEND_PATH = Path(__file__).resolve().parent / "album_labels.txt"

def append_album_log(path, albums) -> int:
    count = 0
    # Open the file once in UTF-8 append mode using a with block.
    with open(path, "a", encoding="utf-8") as file_object:
        for artist in albums:
            count += 1 
            file_object.write(f'{artist["title"]} by {artist["artist"]} ({artist["year"]})\n')

    return count

# albums is a list of dictionaries with "title", "artist", and "year" keys.
# Assume title and artist are strings without embedded newlines; year is an integer.
# Assume the destination is empty, missing, or already ends with a newline,
# and its parent directory exists.
# Add one line per album in this format, ending each line with a newline:
# example: Hemispheres by Rush (1978)
# Return the number of albums appended after closing the file.
albums = [
    {
        "title": "Moving Pictures",
        "artist": "Rush",
        "year": 1981,
    },
    {
        "title": "Fragile",
        "artist": "Yes",
        "year": 1971,
    },
    {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
    },
    {
        "title": "Led Zeppelin IV",
        "artist": "Led Zeppelin",
        "year": 1971,
    },
    {
        "title": "Master of Reality",
        "artist": "Black Sabbath",
        "year": 1971,
    },
]

print(f'number of albums appended: {append_album_log(APPEND_PATH, albums)}')
print(f'number of albums appended: {append_album_log(APPEND_PATH, [])}')
# Preserve existing file text, input order, and the original dictionaries.
# An empty list returns 0 and writes no text, but still creates a missing file.
# Explain how this differs from the previous lesson's write_album_report()
# and why running the same append call twice creates duplicate lines.
# Lines are duplicated because the file does not first truncate
