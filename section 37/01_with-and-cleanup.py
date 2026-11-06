# ============================================================
# FILE: 01_with-and-cleanup.py
# TOPIC: How with Manages a Resource
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Trace resource lifetime.
# 2. Distinguish a closed file from saved content.

# SECTION 1 - UNDERSTAND THE IDEA
# with calls a context manager on entry and exit. Normal completion and errors
# in the body both trigger exit after successful entry. If entry itself fails,
# its exit method is not called: acquisition must clean up partial resources.
# A with statement does not make every value automatically into a context manager.

# SECTION 2 - WORKED EXAMPLES
from io import StringIO

def example_lifetime():
    with StringIO("Rush") as stream:
        text = stream.read()
        print(stream.closed)  # => False
    print(stream.closed)      # => True
    print(text)               # => Rush

def example_failure_cleanup():
    stream = StringIO("Rush")
    try:
        with stream:
            raise ValueError("bad record")
    except ValueError:
        print(stream.closed)  # => True

# example_lifetime()
# example_failure_cleanup()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Predict whether saved text can be read after closing the stream.
# ANSWER / CODE: ______________________________________________
# 2. Raise an exception inside a with block and verify closure.
# ANSWER / CODE: ______________________________________________
# 3. Explain what must happen if acquisition fails halfway through.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Resource lifetime is a control-flow concern, including error paths.

# ============================================================
# END OF LESSON
# ============================================================
