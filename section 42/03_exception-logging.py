# ============================================================
# FILE: 03_exception-logging.py
# TOPIC: Log Failures with Tracebacks
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use logger.exception in an exception handler.
# 2. Preserve a useful failure policy.

# SECTION 1 - UNDERSTAND THE IDEA
# logger.exception logs an ERROR with the current exception traceback. Use it
# inside except. Logging does not fix or propagate the failure: explicitly
# re-raise, return an error result, or continue according to your policy. Never
# log credentials or entire sensitive payloads just to get more context.

# SECTION 2 - WORKED EXAMPLES
import logging
from io import StringIO

def example_exception():
    output = StringIO()
    logger = logging.Logger("importer")
    handler = logging.StreamHandler(output)
    logger.addHandler(handler)
    try:
        try:
            int("unknown")
        except ValueError:
            logger.exception("Invalid duration in row %d", 2)
        print("ValueError" in output.getvalue())  # => True
        print("row 2" in output.getvalue())       # => True
    finally:
        logger.removeHandler(handler)
        handler.close()

# example_exception()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Log a file-open failure with a record identifier.
# ANSWER / CODE: ______________________________________________
# 2. Explain log-and-reraise versus log-and-continue.
# ANSWER / CODE: ______________________________________________
# 3. List data that should never appear in diagnostic logs.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A traceback explains a failure; application policy decides what happens next.

# ============================================================
# END OF LESSON
# ============================================================
