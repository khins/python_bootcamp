# Write to a File — Study Summary
# Instructor summary:
# - Open a text file with mode "w" to write to it.
# - If the file does not exist, "w" creates it, provided its parent directory exists.
# - If the file already exists, opening it with "w" erases its existing contents.
# - Use a with block to close the file automatically when the block exits.
# - file_object.write(text) writes a string to the file.
# - write() does not add spaces or newlines automatically.
# - Use "\n" inside a string to write a newline between lines of text.
# - Consecutive write() calls continue from the current file position.
#
# Clarifications and connections:
# - Truncation happens when open(..., "w") succeeds, before any write() call.
#   Even an empty with block can therefore erase an existing file's contents.
# - Reopening with "w" truncates again; a second write() in the same open
#   stream does not truncate the file again.
# - "w" is lowercase. The default mode is "r", which does not permit writing.
# - Text write() requires a string and returns the number of characters written.
# - Writing to a file does not automatically display anything in the terminal.
# - Closing flushes buffered output. with also closes the file if an exception
#   leaves its block, but it does not undo text already written or truncation.
# - Use encoding="utf-8" consistently when writing and reading these examples.
# - Relative paths use the current working directory. The path below explicitly
#   chooses an output beside this script.
# - Append mode ("a") preserves existing text and adds to its end; the next
#   lesson covers that behavior.

from pathlib import Path


OUTPUT_PATH = Path(__file__).resolve().parent / "writing_demo.txt"


# --- 1. Define the instructor's two-line example ---
def write_greeting(path):
    with open(path, "w", encoding="utf-8") as file_object:
        file_object.write("Hello file!\n")
        file_object.write("You're my favorite file.\n")


# To try it, uncomment the call below. Each call replaces writing_demo.txt's
# contents, so use this dedicated practice file rather than a file you need.
# write_greeting(OUTPUT_PATH)
#
# Expected file contents:
# Hello file!
# You're my favorite file.
#
# The function returns None and prints nothing. Its result is the written file.
# Writing examples are opt-in: running this lesson as supplied does not write files.


# --- 2. Read back the saved text ---
# After calling write_greeting(), uncomment:
# with open(OUTPUT_PATH, "r", encoding="utf-8") as file_object:
#     content = file_object.read()
#
# print(repr(content))  # "Hello file!\nYou're my favorite file.\n"
#
# The write block has closed before the read block opens the same path.
# The default text-reading behavior normalizes standard line endings to "\n".


# --- 3. Consecutive writes do not insert separators ---
# This replaces the practice file with a different example:
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("Hello")
#     file_object.write("file")
#
# Exact text content: Hellofile
# There is no space or newline unless one is included in a string.
# To put the words on separate lines, use "Hello\n" for the first write.


# --- 4. Inspect the return value of write() ---
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     characters_written = file_object.write("Rush\n")
#
# print(characters_written)  # 5 — four letters plus one newline character
#
# This count is characters, not necessarily the number of bytes stored on disk.
# Text encoding and platform newline translation can affect the byte count.


# --- 5. Opening in write mode is what erases earlier contents ---
# Run these blocks in order using only the dedicated practice file:
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("First version\n")
#
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("Second version\n")
#
# Final file contents: "Second version\n"
# The first version is gone; the second open truncated the file.
#
# This would leave the practice file empty, even without calling write():
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     pass


# --- 6. Convert other values to strings before writing ---
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     year = 1978
#     file_object.write(str(year))
#     file_object.write("\n")
#     file_object.write(f"Album year: {year}\n")
#
# Expected file contents:
# 1978
# Album year: 1978
#
# Passing an integer directly to a text stream's write() raises TypeError:
# file_object.write(1978)  # Intentional error when open; keep commented out.
# A closed stream cannot be written to, even if the variable still exists.


# --- 7. Write several lines with a loop ---
def write_album_titles(path, titles):
    with open(path, "w", encoding="utf-8") as file_object:
        for title in titles:
            file_object.write(title + "\n")


# Assume each title is a string without embedded newlines.
# To try the function:
# write_album_titles(OUTPUT_PATH, ["Hemispheres", "Moving Pictures", "Tarkus"])
#
# Expected file contents:
# Hemispheres
# Moving Pictures
# Tarkus
#
# The file is opened once, outside the loop. Putting a separate "w" open inside
# each iteration would erase earlier titles, leaving only the last one.
# An empty titles list still opens and truncates the file, leaving it empty.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before trying each exercise.
# Use OUTPUT_PATH only as a dedicated practice file; each "w" open replaces it.
# Distinguish terminal output from file contents, and show newlines with \n
# when writing exact string predictions. Keep intentional errors commented out.

# Exercise 1 — Adjacent writes
# Predict the exact file contents. Does this code print anything in the terminal?
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("Rush")
#     file_object.write("Yes")
# ANSWER:


# Exercise 2 — Include newlines
# Predict the exact file contents and the value printed in the terminal.
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     count = file_object.write("Rush\n")
#     file_object.write("Yes\n")
# print(count)
# ANSWER:


# Exercise 3 — Reopen the same file
# Predict the final file contents. Explain what happens to "Old text".
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("Old text")
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("New text")
# ANSWER:


# Exercise 4 — No write call
# Assume OUTPUT_PATH already contains "Keep this text".
# What does it contain after this block? Which operation causes the change?
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     pass
# ANSWER:


# Exercise 5 — Diagnose the value type
# Explain why this write call raises TypeError and show two ways to convert
# the number into suitable text. What happens to old contents before the error?
# with open(OUTPUT_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write(1981)  # Intentional TypeError; keep commented out.
# ANSWER:


# Exercise 6 — Write and verify your own file
# 1. Build a path beside this script named favorite_artists_demo.txt.
# 2. Create a list of at least three artist-name strings.
# 3. Open the file once with a with block in UTF-8 write mode.
# 4. Loop over the names and write each one followed by a newline.
# 5. After closing it, reopen the file for reading and print its contents.
# 6. Explain what happens if you run your code twice with the same names.
# Write your code below:


# Optional challenge — Write an album report
# Work through this one together when you are ready.
# Define write_album_report(path, albums).
# albums is a list of dictionaries with "title", "artist", and "year" keys.
# Assume titles and artists are strings without embedded newlines; years are integers.
# Open the destination once in UTF-8 write mode using a with block.
# Write one line per dictionary in this format:
# Hemispheres by Rush (1978)
# End every written line with a newline. Return the number of albums written
# after the file is closed. Preserve the original list and dictionaries.
# An empty list must create or truncate the destination to an empty file and return 0.
# Use a loop, dictionary lookups, and an f-string. Test with a dedicated demo file.
# Explain why the open() call belongs outside the loop and how the return value
# differs from the number returned by an individual write() call.
# Write your code below:
