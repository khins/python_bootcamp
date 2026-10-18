# Optional challenge — Write an album report
# Write your code below:
# Work through this one together when you are ready.
# Define write_album_report(path, albums).
def write_album_report(path, albums) -> int:
    count = 0
    # Open the destination once in UTF-8 write mode using a with block.
    # Write one line per dictionary in this format:
    # Hemispheres by Rush (1978)
    # End every written line with a newline. Return the number of albums written
    # after the file is closed. Preserve the original list and dictionaries.
    # An empty list must create or truncate the destination to an empty file and return 0.
    # Use a loop, dictionary lookups, and an f-string. Test with a dedicated demo file.
    with open(path, "w", encoding="utf-8") as file_object:
        for album in albums:
            count += 1
            file_object.write(f'{album["title"]} by {album["artist"]} ({album["year"]})\n')

    return count

from pathlib import Path
OUTPUT_PATH = Path(__file__).resolve().parent / "album_report.txt"

# albums is a list of dictionaries with "title", "artist", and "year" keys.
# Assume titles and artists are strings without embedded newlines; years are integers.
artists_pool = [
    {"title": "2112", "artist": "Rush", "year": 1976},
    {"title": "Close to the Edge", "artist": "Yes", "year": 1972},
    {"title": "Alone Together", "artist": "Dave Mason", "year": 1970},
    {"title": "Carolina Dreams", "artist": "Marshall Tucker Band", "year": 1977},
    {"title": "The Pleasure Principle", "artist": "Gary Numan", "year": 1979},
]
print(f'The number of albums processed: {write_album_report(OUTPUT_PATH, artists_pool)}')

# Explain why the open() call belongs outside the loop and how the return value
# differs from the number returned by an individual write() call.
