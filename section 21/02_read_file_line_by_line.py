# Read a File Line by Line — Study Summary
# Instructor summary:
# - A text file object is iterable: a for loop yields one line at a time.
# - Each line is a string, so ordinary string methods work on it.
# - Iterating directly avoids loading the entire file into one large string.
# - Keep the loop inside a with block so the file stays open while being read
#   and closes automatically when the block exits.
# - open() defaults to text read mode, so the "r" argument can be omitted.
# - Lines usually retain their newline character. print() adds another newline
#   by default, which can produce extra blank lines in the output.
#
# Clarifications and corrections:
# - open() is a built-in function, not a method.
# - Line iteration is memory-efficient for many text tasks, but not universally
#   the fastest approach. A single extremely long line can still use much memory.
# - The last line may have no terminating newline and is still yielded.
# - strip() removes leading AND trailing whitespace, not just a newline.
# - rstrip() removes trailing whitespace, including spaces and tabs.
# - print(line, end="") avoids an extra newline while preserving the string's
#   existing whitespace. Use this when displaying the text as read.
# - rstrip("\n") removes only trailing newline characters, preserving spaces.
# - In default text mode, common file line endings are translated to "\n".
# - Relative paths use the current working directory. The path below explicitly
#   locates cupcakes.txt beside this script, as in the previous lesson.

from pathlib import Path


SAMPLE_PATH = Path(__file__).resolve().parent / "cupcakes.txt"


# --- 1. Prepare the sample file ---
# Create a UTF-8 cupcakes.txt beside this script if it does not already exist.
# For the exact example outputs below, use these two lines, with a newline
# after the final line:
# Vanilla cupcake
# Chocolate cupcake
#
# The demo reads whatever text is already in that file; it does not overwrite it.


# --- 2. Iterate over the open file ---
def display_lines(path):
    with open(path, encoding="utf-8") as file_object:
        for line in file_object:
            print(line, end="")


# Each iteration supplies one string. The loop does not need read() first.
# The with block closes the file after the loop, including if an exception exits it.
# For the sample, display_lines(SAMPLE_PATH) displays:
# Vanilla cupcake
# Chocolate cupcake


if __name__ == "__main__":
    try:
        display_lines(SAMPLE_PATH)
    except FileNotFoundError:
        print(f"Create a UTF-8 sample file here: {SAMPLE_PATH}")


# --- 3. See why print(line) adds gaps ---
# Uncomment after preparing the sample file:
# with open(SAMPLE_PATH, encoding="utf-8") as file_object:
#     for line in file_object:
#         print(repr(line))
#
# Expected:
# 'Vanilla cupcake\n'
# 'Chocolate cupcake\n'
#
# repr() displays the newline as \n so you can see it.
# print(line) would output the line's own newline PLUS print's default newline.
# print(line, end="") adds no extra newline and avoids that doubled spacing.


# --- 4. Compare whitespace handling ---
example_line = "  Vanilla cupcake  \n"
# Uncomment to compare the results:
# print(repr(example_line.strip()))  # 'Vanilla cupcake'
# print(repr(example_line.rstrip()))  # '  Vanilla cupcake'
# print(repr(example_line.rstrip("\n")))  # '  Vanilla cupcake  '
# print(repr(example_line))  # '  Vanilla cupcake  \n'
#
# These methods return new strings; example_line itself is unchanged.
# Choose a method based on which whitespace you intend to remove.
# For example, stripping indentation would change the appearance of indented text.


# --- 5. Print one line at a time with a new output newline ---
# with open(SAMPLE_PATH, encoding="utf-8") as file_object:
#     for line in file_object:
#         print(line.rstrip("\n"))
#
# This removes an existing newline, then print() adds one back.
# Unlike print(line, end=""), it also adds a newline after a final line that
# originally had none. It preserves leading and trailing spaces in the text.
# Using print(line.strip()) instead would remove those spaces too.


# --- 6. Count lines without collecting the whole file ---
def count_lines(path):
    count = 0
    with open(path, encoding="utf-8") as file_object:
        for line in file_object:
            count += 1
    return count


# print(count_lines(SAMPLE_PATH))  # 2 for the sample in section 1
# An empty file gives 0 iterations and returns 0.
# A blank line still counts: it is typically the string "\n".
# A final nonempty line without a newline also counts.
# A file containing "Vanilla\n" has one line, not an extra empty second line.


# --- 7. Iteration uses the current file position ---
# with open(SAMPLE_PATH, encoding="utf-8") as file_object:
#     for line in file_object:
#         print(line, end="")
#     print(repr(file_object.read()))  # '' — the loop reached the end
#
# A second loop over the same exhausted file object would have no iterations.
# Reopening the file starts a new stream at the beginning.
# Do not iterate after leaving the with block: the file has already been closed.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Use the sample from section 1 for exercises that refer to SAMPLE_PATH.
# Keep intentional-error examples commented out.

# Exercise 1 — Identify the loop variable
# Predict both printed types. What does line contain in each iteration?
# with open(SAMPLE_PATH, encoding="utf-8") as file_object:
#     for line in file_object:
#         print(type(line))
# ANSWER:


# Exercise 2 — Explain the extra spacing
# Why does this code produce an extra blank line after each sample line?
# Rewrite only the print call to preserve the text without adding extra newlines.
# with open(SAMPLE_PATH, encoding="utf-8") as file_object:
#     for line in file_object:
#         print(line)
# ANSWER:


# Exercise 3 — Choose the right string method
# Predict all three outputs, including spaces inside the quotes.
# text = "  Rush  \n"
# print(repr(text.strip()))
# print(repr(text.rstrip()))
# print(repr(text.rstrip("\n")))
# Which option removes the newline while preserving both surrounding spaces?
# ANSWER:


# Exercise 4 — Blank lines still count
# Suppose a file contains exactly "Rush\n\nYes".
# How many iterations does a for loop over that file perform?
# Write the repr() of each yielded string in order.
# Explain whether the lack of a final newline prevents "Yes" from being read.
# ANSWER:


# Exercise 5 — An exhausted stream
# Predict the last printed value. Why is no text returned by read() here?
# with open(SAMPLE_PATH, encoding="utf-8") as file_object:
#     for line in file_object:
#         pass
#     print(repr(file_object.read()))
# ANSWER:


# Exercise 6 — Write your own numbered display
# 1. Create a small UTF-8 favorite_albums.txt beside this script with three
#    album titles, one per line.
# 2. Build its path using SAMPLE_PATH.parent / "favorite_albums.txt".
# 3. Open it with a with block and iterate directly over the file.
# 4. Print each title preceded by its line number, starting at 1.
#    Example: 1: Hemispheres
# 5. Avoid extra blank lines. Preserve any spaces in the title itself.
# 6. After the with block, print the total number of lines processed.
#    Make sure an empty file would report 0.
# Write your code below:


# Optional challenge — Count nonempty lines containing a word
# Work through this one together when you are ready.
# Define count_matching_lines(path, word).
# Assume word is a nonempty string. Open the UTF-8 file using a with block
# and process it one line at a time, without read() or collecting all lines.
# Return the number of nonempty lines containing word as a case-insensitive
# substring. Use strip() to identify whitespace-only lines and lower() to
# compare text. Count each matching line once, even if word appears twice.
# For a file containing "Rush\n\nRUSH and Rush\nYes\n   \n":
# count_matching_lines(path, "rush") returns 2.
# An empty file returns 0. Leave the file unchanged and return after closing it.
# Let FileNotFoundError propagate if the file does not exist.
# Explain what each iteration supplies and why you do not need an inner loop.
# Write your code below:
