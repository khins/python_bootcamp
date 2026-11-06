# ============================================================
# FILE: 03_contextmanager.py
# TOPIC: Generator-based Context Managers
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Yield exactly once.
# 2. Place cleanup in finally.

# SECTION 1 - UNDERSTAND THE IDEA
# contextmanager adapts a generator into the context-manager protocol. Setup
# happens before yield; yield supplies the as value; finally performs cleanup.
# An error from the body is thrown back at yield. Catching it without re-raising
# suppresses it, so logging an error should normally be followed by raise.

# SECTION 2 - WORKED EXAMPLES
from contextlib import contextmanager
from io import StringIO

@contextmanager
def text_resource(text):
    stream = StringIO(text)
    try:
        yield stream
    finally:
        stream.close()

def example_generator_manager():
    with text_resource("Yes") as stream:
        print(stream.read())  # => Yes
    print(stream.closed)      # => True

# example_generator_manager()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add setup and cleanup messages and predict their order.
# ANSWER / CODE: ______________________________________________
# 2. Test cleanup when the body raises RuntimeError.
# ANSWER / CODE: ______________________________________________
# 3. Explain why yielding twice violates this protocol.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A single yield divides resource setup from cleanup.

# REFERENCES
# https://docs.python.org/3.13/library/contextlib.html

# ============================================================
# END OF LESSON
# ============================================================
