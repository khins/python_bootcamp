# Exercise 6 — Build a small listening log
# Write your code below:
# 1. Choose a new dedicated file named listening_log_demo.txt beside this script.
# 2. Append three song titles using append mode and a with block.
from pathlib import Path

APPEND_PATH = Path(__file__).resolve().parent / "listening_log_demo.txt"

artists = [
    "Rush",
    "Yes",
    "Dave Mason",
]
# 3. Give each title a trailing newline; assume the file is empty, missing,
#    or already ends in a newline.
with open(APPEND_PATH, "a", encoding="utf-8") as file_object:
    for artist in artists:
        file_object.write(artist + "\n")

with open(APPEND_PATH, "r", encoding="utf-8") as file_object:
    for line in file_object:
        print(line, end="")

# 4. Reopen it for reading after the append block and print its contents.
# 5. Explain what happens if you run only the append-and-read code a second time.
# the contents of the log text file double because it is appending content instead of truncation
