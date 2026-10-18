# Exercise 6 — Write and verify your own file
# Write your code below:
# 1. Build a path beside this script named favorite_artists_demo.txt.
from pathlib import Path


OUTPUT_PATH = Path(__file__).resolve().parent / "favorite_artists_demo.txt"
# 2. Create a list of at least three artist-name strings.
artists = [
    "Rush",
    "Yes",
    "Dave Mason",
]
# 3. Open the file once with a with block in UTF-8 write mode.
# 4. Loop over the names and write each one followed by a newline.
# 5. After closing it, reopen the file for reading and print its contents.
with open(OUTPUT_PATH, "a", encoding="utf-8") as file_object:
    for artist in artists:
        file_object.write(f'{artist}\n')
with open(OUTPUT_PATH, "r", encoding="utf-8") as file_object:
    for line in file_object:
        print(line.rstrip("\n"))

# 6. Explain what happens if you run your code twice with the same names.
# just writes the same content since first mode is w
# Running the script twice produces the same contents.
# Opening the file in "w" mode erases the previous data.
# The loop then writes the three artist names again.
# No duplicate entries are created.
