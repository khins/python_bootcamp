# Append to a File — Study Summary
# Instructor summary:
# - Open a text file with mode "a" to append new text to its end.
# - Append mode preserves existing contents instead of erasing them.
# - Use the same write() method as in write mode; the open mode changes
#   whether existing content is preserved or truncated.
# - If the file does not exist, append mode creates it.
# - write() does not automatically insert a space or newline.
# - Running the same append code again adds the text again.
# - Use a with block to close the file automatically after writing.
#
# Clarifications and connections:
# - "w" truncates an existing file when it opens; "a" does not.
# - A text file object has write(), not a list-style append() method.
# - Append mode writes at the end; it does not guarantee a new line starts there.
# - If existing text lacks a final newline, new text joins that final line
#   unless you explicitly supply a separator.
# - A leading "\n" separates text from an unterminated last line, but adds
#   a blank line if the file already ends with a newline.
# - A trailing "\n" prepares the end of the appended text for the next line.
# - Creating a missing file still requires its parent directory to exist.
# - Text write() takes a string and returns the number of characters written.
# - Mode "a" alone is for writing, not reading. Reopen with "r" to inspect it.
# - Use a consistent encoding, such as UTF-8, for reading and writing.

from pathlib import Path


APPEND_PATH = Path(__file__).resolve().parent / "append_demo.txt"
# This explicitly locates the practice file beside the script. A plain relative
# filename would instead be resolved from the current working directory.
# All calls that modify files are commented out; running this lesson as supplied
# does not create or change the practice file.


# --- 1. Append using the same write() method ---
def append_text(path, text):
    with open(path, "a", encoding="utf-8") as file_object:
        characters_written = file_object.write(text)
    return characters_written


# To try this, uncomment the call:
# append_text(APPEND_PATH, "Third line is the best line.\n")
#
# If the file is missing, it is created with that text as its first line.
# If it already contains text, the string is added directly to its end.
# No other separator is inserted. The existing text remains unchanged.


# --- 2. Prepare a known starting point for experiments ---
# Run this setup only when you want to reset the dedicated practice file:
# with open(APPEND_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("Hello file!\nYou're my favorite file.")
#
# The setup deliberately uses "w" to replace previous practice content.
# Notice that its final line does NOT end with "\n".
# Append once:
# append_text(APPEND_PATH, "Third line is the best line.")
#
# File contents now look like:
# Hello file!
# You're my favorite file.Third line is the best line.
#
# Append mode preserves text but does not decide where your lines should break.


# --- 3. Add a leading newline when the existing last line needs one ---
# After resetting the file with section 2's setup, try this alternative:
# append_text(APPEND_PATH, "\nThird line is the best line.\n")
#
# Expected file contents:
# Hello file!
# You're my favorite file.
# Third line is the best line.
#
# Do not blindly prefix every append with "\n": if the file already ends in
# a newline, that prefix creates an extra blank line. In an empty file it
# creates a blank first line. Choose separators to match your file's format.


# --- 4. Keep a consistent trailing-newline format ---
# Reset the practice file so every initial line ends with a newline:
# with open(APPEND_PATH, "w", encoding="utf-8") as file_object:
#     file_object.write("Hello file!\nYou're my favorite file.\n")
#
# append_text(APPEND_PATH, "Third line is the best line.\n")
# append_text(APPEND_PATH, "Fourth line follows.\n")
#
# Expected file contents:
# Hello file!
# You're my favorite file.
# Third line is the best line.
# Fourth line follows.
#
# Each append can start with its text immediately because the previous content
# already ends with a newline. This also works when starting with an empty file.


# --- 5. Repeated calls add repeated content ---
# Starting with an empty practice file, run:
# append_text(APPEND_PATH, "Rush\n")
# append_text(APPEND_PATH, "Rush\n")
#
# File contents: "Rush\nRush\n"
# Append mode does not check for duplicates or replace earlier matching text.
# Rerunning just these calls adds two more lines each time.


# --- 6. Read back after closing the append stream ---
# After any append example above:
# with open(APPEND_PATH, "r", encoding="utf-8") as file_object:
#     content = file_object.read()
# print(content, end="")
#
# The append block has closed and flushed buffered output before reading.
# To inspect a write count, use this separate example:
# print(append_text(APPEND_PATH, "Yes\n"))  # 4
# That call adds "Yes\n" and returns four characters written, not total file size.


# --- 7. Append a collection of lines ---
def append_artists(path, artists):
    with open(path, "a", encoding="utf-8") as file_object:
        for artist in artists:
            file_object.write(artist + "\n")


# Assume artist names are strings without embedded newlines, and the destination
# is empty, missing, or already ends in a newline.
# append_artists(APPEND_PATH, ["Rush", "Yes", "Genesis"])
#
# The file is opened once and each artist is added in list order.
# An empty list writes no text, but opening in "a" still creates a missing file.
# If the file already exists, an empty list leaves its contents unchanged.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before trying each exercise.
# Treat each exercise independently with the stated starting contents.
# Use only a dedicated practice file. Show exact text using \n for newlines.

# Exercise 1 — Preserve the existing text
# Assume the file initially contains "Rush\n".
# Predict its contents after this call. What would change if the function used
# "w" instead of "a"?
# append_text(APPEND_PATH, "Yes\n")
# ANSWER:


# Exercise 2 — No automatic separator
# Assume the file initially contains "Rush" with no final newline.
# Predict its contents after append_text(APPEND_PATH, "Yes\n").
# Change the appended string so Yes begins on a new line for this starting file.
# ANSWER:


# Exercise 3 — Too many newlines
# Assume the file initially contains "Rush\n".
# Predict its contents after append_text(APPEND_PATH, "\nYes\n").
# Explain why an extra blank line appears and how to avoid it in this case.
# ANSWER:


# Exercise 4 — Repeat the operation
# Assume the file is initially empty.
# Predict its final contents and both printed values.
# print(append_text(APPEND_PATH, "Yes\n"))
# print(append_text(APPEND_PATH, "Yes\n"))
# ANSWER:


# Exercise 5 — Missing file and empty input
# Assume the parent directory exists but the file does not.
# What happens when append_artists(APPEND_PATH, []) runs?
# What happens if the same call runs on a file containing "Rush\n"?
# Explain how append mode differs from write mode in the second case.
# ANSWER:


# Exercise 6 — Build a small listening log
# 1. Choose a new dedicated file named listening_log_demo.txt beside this script.
# 2. Append three song titles using append mode and a with block.
# 3. Give each title a trailing newline; assume the file is empty, missing,
#    or already ends in a newline.
# 4. Reopen it for reading after the append block and print its contents.
# 5. Explain what happens if you run only the append-and-read code a second time.
# Write your code below:


# Optional challenge — Append album labels and return a count
# Work through this one together when you are ready.
# Define append_album_log(path, albums).
# albums is a list of dictionaries with "title", "artist", and "year" keys.
# Assume title and artist are strings without embedded newlines; year is an integer.
# Assume the destination is empty, missing, or already ends with a newline,
# and its parent directory exists.
# Open the file once in UTF-8 append mode using a with block.
# Add one line per album in this format, ending each line with a newline:
# Hemispheres by Rush (1978)
# Return the number of albums appended after closing the file.
# Preserve existing file text, input order, and the original dictionaries.
# An empty list returns 0 and writes no text, but still creates a missing file.
# Explain how this differs from the previous lesson's write_album_report()
# and why running the same append call twice creates duplicate lines.
# Write your code below:
