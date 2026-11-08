# ============================================================
# FILE: 06_descriptor-project.py
# TOPIC: Project: Validated Data Objects
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: validated data objects to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# validated_album.py validates and normalizes text through a shared descriptor.
# Instances remain independent. Album is deliberately unhashable because its
# fields can change while equality depends on them. Failed validation happens
# before assignment, preserving the previous value. NotImplemented lets Python
# try reflected comparison rather than incorrectly claiming all unknown types
# are unequal through a custom implementation.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from validated_album import Album

def example():
    album = Album(" Signals ", "Rush")
    print(album.title)  # => Signals
    print(album == Album("Signals", "Rush"))  # => True
    try:
        hash(album)
    except TypeError:
        print("mutable value objects are not keys here")


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why normalize before storing?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add a separate validated year descriptor and test two albums independently.
# ANSWER / CODE: ______________________________________________

# 3. Why is __hash__ = None an intentional design decision?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: validated_album.py validates and normalizes text through a
# shared descriptor.
# ============================================================
# END OF LESSON
# ============================================================
