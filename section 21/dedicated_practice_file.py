# Exercise 1 — Preserve the existing text
# Assume the file initially contains "Rush\n".
# Predict its contents after this call. What would change if the function used
# "w" instead of "a"?
# append_text(APPEND_PATH, "Yes\n")
from pathlib import Path

def append_text(path, text):
    with open(path, "a", encoding="utf-8") as file_object:
        file_object.write(text)

APPEND_PATH = Path(__file__).resolve().parent / "append_demo.txt"
append_text(APPEND_PATH, "Rush\n")
append_text(APPEND_PATH, "Yes\n")
# ANSWER:
# Rush
# Yes
# The mode of the file object would change to w
# With "a" mode, the file contains:
# Rush
# Yes