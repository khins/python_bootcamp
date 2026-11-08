# ============================================================
# FILE: 03_exception-notes.py
# TOPIC: Adding Context with add_note
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply adding context with add_note to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Python 3.11 exceptions support add_note(str). Notes enrich a traceback without
# changing the exception type or replacing its cause. They are useful when a
# caller knows an item index or operation that the lower layer cannot know.
# Avoid recording passwords, tokens, or complete private records in notes.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
def parse_record(index, text):
    try:
        return int(text)
    except ValueError as error:
        error.add_note(f"record index: {index}")
        raise

def example():
    try:
        parse_record(2, "invalid")
    except ValueError as error:
        print(error.__notes__)  # => ['record index: 2']


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does adding a note change the exception class?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add an operation name in a second caller and inspect both notes.
# ANSWER / CODE: ______________________________________________

# 3. Why use bare raise after adding a note?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Python 3.11 exceptions support add_note(str).
# ============================================================
# END OF LESSON
# ============================================================
