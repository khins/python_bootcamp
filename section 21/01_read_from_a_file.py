# Read from a File — Study Summary
# Instructor summary:
# - open(path, "r") opens a file for reading and returns a file object.
# - "r" is the default mode; reading text is the default rather than binary mode.
# - Use with open(...) as file_object: to close the file automatically when
#   the block exits, including when an exception leaves the block.
# - file_object.read() returns the remaining text as one string.
# - Store that string in a variable to use it after the file has closed.
# - Reading an entire file at once is suitable for small files; large files
#   can be processed incrementally instead.
# - Opening a nonexistent file in read mode raises FileNotFoundError.
# - input() can supply a filename chosen by the user.
#
# Clarifications and corrections:
# - Relative paths are resolved from the CURRENT WORKING DIRECTORY, not
#   automatically from the directory containing the Python script.
# - An IDE runner can read files; its working directory affects relative paths.
#   Interactive input also requires a runner or terminal that supports input().
# - open() accepts more options than filename and mode. encoding="utf-8"
#   explicitly selects UTF-8 for these text examples.
# - Read mode does not create missing files or change their contents.
# - with still uses open(); it replaces the need to manually arrange close().
# - Closing a read-only file releases resources. Leaving it open does not
#   itself rewrite or corrupt the source file.
# - with closes an opened file during normal exit and exception unwinding;
#   it does not suppress the exception or protect against abrupt process termination.
# - Text read from a file remains available after closing the file object.

from pathlib import Path


# --- 1. Prepare a small UTF-8 text file ---
# Create cupcakes.txt beside this lesson and save these two lines:
# Vanilla cupcake
# Chocolate cupcake
#
# For the exact repr() outputs below, include a newline after the second line.
# The examples only read the file. They do not create or overwrite it.

# This path locates the sample beside the script, regardless of the terminal's
# current working directory. __file__ is the path of this Python file.
SAMPLE_PATH = Path(__file__).resolve().parent / "cupcakes.txt"


# --- 2. Read with automatic cleanup ---
def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file_object:
        content = file_object.read()
    return content


# The return happens after the with block closes the file.
# The returned content is a string, not an open file object.
# Opening without an explicit "r" would also use text read mode.


def main():
    try:
        with open(SAMPLE_PATH, "r", encoding="utf-8") as cupcakes_file:
            print("The file has been opened.")
            content = cupcakes_file.read()
            print(cupcakes_file.closed)  # False

        print("The file has been closed.")
        print(cupcakes_file.closed)  # True
        print(content, end="")
    except FileNotFoundError:
        print(f"Create a UTF-8 text file here before running the demo: {SAMPLE_PATH}")


if __name__ == "__main__":
    main()

# With the sample from section 1, the output is:
# The file has been opened.
# False
# The file has been closed.
# True
# Vanilla cupcake
# Chocolate cupcake
#
# end="" avoids adding an extra newline after the file's existing final newline.
# If the sample is missing, the demo prints its expected location instead.
# Other errors, such as an invalid UTF-8 encoding, are not caught by this handler.


# --- 3. Understand what read() returns ---
# After creating the sample, uncomment this example:
content = read_text_file(SAMPLE_PATH)
print(type(content))  # <class 'str'>
print(repr(content))  # 'Vanilla cupcake\nChocolate cupcake\n'
#
# repr() makes newline characters visible as \n in the displayed representation.
# The saved string is usable even though read_text_file() has closed the file.
# An empty file produces an empty string: "".


# --- 4. Reading advances the file position ---
with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
    first_read = file_object.read()
    second_read = file_object.read()
#
print(repr(first_read))  # 'Vanilla cupcake\nChocolate cupcake\n'
print(repr(second_read))  # ''
#
# The first read reaches the end. A second read does not automatically restart.
# Opening the file again creates a new stream positioned at the beginning.


# --- 5. Read a limited amount of text ---
with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
    print(file_object.read(7))  # Vanilla
    print(repr(file_object.read(1)))  # ' '
#
# In text mode, read(n) reads at most n characters, starting at the current position.
# Another option for large text files is to iterate over lines:
# with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
#     for line in file_object:
#         print(line, end="")
# This processes one line at a time instead of collecting the whole file in a string.


# --- 6. Ask the user for a path ---
# Run this optional example in a terminal that supports input():
# file_name = input("What file would you like to open? ")
# with open(file_name, "r", encoding="utf-8") as file_object:
#     print(file_object.read(), end="")
#
# A relative filename here is resolved from the current working directory.
# An absolute path specifies the location directly. Enter the path without
# surrounding quotation marks, even if its directory names contain spaces.
# To inspect the working directory:
# print(Path.cwd())
#
# Leave this intentional error commented out, assuming the path does not exist:
# read_text_file(SAMPLE_PATH.parent / "missing_example.txt")  # FileNotFoundError


# --- 7. Closed files cannot be read again ---
with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
    content = file_object.read()

print(content, end="")  # Works: content is an ordinary string.
# print(file_object.read())  # Intentional ValueError; keep commented out.
#
# The variable file_object still exists after the block, but its stream is closed.
# with does not create a separate variable scope.


# --- 8. Practice: predict, explain, then run ---
# Use the sample from section 1, including its final newline, where instructed.
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error lines commented out.

# Exercise 1 — Follow the file's lifetime
# Predict both outputs. 
with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
    print(file_object.closed)
print(file_object.closed)
# ANSWER:
#  Chocolate cupcakeFalse
# True
# Explain what closes the file.
# the file closes when the with loop completes
# The file automatically closes when execution exits
# the with block because the context manager calls
# the file object's __exit__() method.

# Exercise 2 — Identify the returned object
# Predict both outputs and explain why content remains usable afterward.
content = read_text_file(SAMPLE_PATH)
print(type(content))
print(content.startswith("Vanilla"))
# ANSWER:
# <class 'str'>
# False
# explain why content remains usable afterward:
# because content is a variable that contains the result of the read_text_file
# The content variable references the string returned
# by read_text_file(). Even after the file is closed,
# the string remains available in memory.

# Exercise 3 — Two reads
# Predict both outputs. Explain why the second read differs from the first.
with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
    print(len(file_object.read()) > 0)
    print(repr(file_object.read()))
# ANSWER:
# True
# ''
# Explain why the second read differs from the first:
# repr says that it will Return the canonical string representation of the object.
# The first file_object.read() reads the entire file and moves the cursor to the end.
# The second file_object.read() starts at the current cursor position, which is already at the end of the file.
# Since there's nothing left to read, Python returns an empty string ("").
# repr() displays that empty string as ''.


# Exercise 4 — Diagnose the path
# A script is stored in section 21, but the terminal's current directory is
# the repository root. cupcakes.txt exists only inside section 21.
# Explain why open("cupcakes.txt", "r") fails in this situation.
# Show how using SAMPLE_PATH solves the problem.
# ANSWER:
from pathlib import Path

SAMPLE_PATH = Path(__file__).resolve().parent / "cupcakes.txt"

with open(SAMPLE_PATH, "r", encoding="utf-8") as file_object:
    print(file_object.read())
# Vanilla cupcake
# Chocolate cupcake

# Exercise 5 — Missing versus empty
# Explain the difference between reading an existing empty file and opening
# a nonexistent file in "r" mode. What value or exception results in each case?
# Does read mode create the nonexistent file?
# ANSWER:
# with open("cupcaked.txt", "r", encoding="utf-8") as file:
#     content = file.read()
# FileNotFoundError
# with open("cupcakes.txt", "w", encoding="utf-8") as file:
#     pass

with open(SAMPLE_PATH, "a", encoding="utf-8") as file:
    file.write("\nStrawberry cupcake")


# Exercise 6 — Write your own reader
# Write your code below:
# 1. Create a small UTF-8 text file named favorite_albums.txt beside this lesson.
#    Put at least three album titles in it, one per line.
FAV_PATH = SAMPLE_PATH.parent / "favorite_albums.txt"
with open(FAV_PATH, "w", encoding="utf-8") as file:
    file.write("Rush: Moving Pictures\n")
    file.write("Yes: Heaven and Earth\n")
    file.write("Eagles: Hotel Cali\n")
# 2. Build its path using SAMPLE_PATH.parent / "favorite_albums.txt".
# 3. Open it with a with block in read mode and save read()'s result to text.
# 4. After the block, print the saved text and its character count using len().
# 5. Explain whether newline characters count toward that length.
# practice reading the file you just created
with open(FAV_PATH, "r", encoding="utf-8") as file:
    text = file.read()

# Print text and its length here
print(text)
print(len(text))

album = "Rush\nYes"
print(len(album))

# Optional challenge — Return nonempty lines from a file
# Work through this one together when you are ready.
# Define read_nonempty_lines(path).
def read_nonempty_lines(path) -> list:
    results = []
    with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned = line.strip()
                if cleaned: # This works because an empty string ("") is falsy, while a nonempty string is truthy
                    results.append(cleaned)
                # print(repr(line))

    return results

print(read_nonempty_lines(FAV_PATH))
    

# Open a UTF-8 text file using a with block and iterate over its lines.
# Strip leading/trailing whitespace from each line with strip().
# Append only nonempty stripped strings to a NEW list and return it after closing.
# Preserve line order and leave the source file unchanged.
# A file containing "  Rush  \n\nYes\n   \nGenesis\n" should produce:
# ['Rush', 'Yes', 'Genesis']
# An empty file should produce []. Let FileNotFoundError propagate for a missing file.
# Explain what the loop variable holds and why the returned list works after close.
# Write your code below:
