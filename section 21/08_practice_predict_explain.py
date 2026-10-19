# Exercise 1 — Preserve the existing text
# Assume the file initially contains "Rush\n".
# Predict its contents after this call. What would change if the function used
# "w" instead of "a"?
# append_text(APPEND_PATH, "Yes\n")
# ANSWER:
from pathlib import Path

APPEND_PATH = Path(__file__).resolve().parent / "append_demo.txt"
def append_text(path, artist):
# Step 1: Create the starting file WITHOUT a newline.
    with open(APPEND_PATH, "w", encoding="utf-8") as file_object:
        file_object.write(artist)

    # Step 2: Append Yes with a newline before and after.
    # with open(APPEND_PATH, "a", encoding="utf-8") as file_object:
    #     file_object.write("\nYes\n")

    # Step 3: Verify the actual contents.
    with open(APPEND_PATH, "r", encoding="utf-8") as file_object:
        print(repr(file_object.read()))
        # pass

# append_text(APPEND_PATH, "Yes\n")

# Exercise 2 — No automatic separator
# Assume the file initially contains "Rush" with no final newline.
# Predict its contents after append_text(APPEND_PATH, "Yes\n").
# Change the appended string so Yes begins on a new line for this starting file.
# append_text(APPEND_PATH, "Yes\n")
# print(append_text(APPEND_PATH, "Yes\n"))
# print(append_text(APPEND_PATH, "Yes\n"))

# Exercise 5 — Missing file and empty input
# Assume the parent directory exists but the file does not.
# What happens when 
append_text(APPEND_PATH, [])
# What happens if the same call runs on a file containing "Rush\n"?
# Explain how append mode differs from write mode in the second case.
# ANSWER:
# Rush