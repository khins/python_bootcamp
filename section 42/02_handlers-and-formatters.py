# ============================================================
# FILE: 02_handlers-and-formatters.py
# TOPIC: Route and Format Log Records
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Set logger and handler thresholds.
# 2. Avoid duplicate handlers.

# SECTION 1 - UNDERSTAND THE IDEA
# Loggers create records; handlers deliver them; formatters turn them into text.
# Both logger and handler thresholds matter. Propagation can send a record to
# ancestor handlers too, producing duplicates if you attach handlers at both
# levels. Configure once at startup; do not add a handler on every operation.

# SECTION 2 - WORKED EXAMPLES
import logging
from io import StringIO

def example_handlers():
    output = StringIO()
    logger = logging.Logger("catalog", level=logging.DEBUG)
    handler = logging.StreamHandler(output)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(logging.Formatter("%(name)s | %(levelname)s | %(message)s"))
    logger.addHandler(handler)
    try:
        logger.info("not delivered")
        logger.error("Import failed")
        print(output.getvalue().strip())  # => catalog | ERROR | Import failed
    finally:
        logger.removeHandler(handler)
        handler.close()

# example_handlers()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add a FileHandler inside a temporary directory.
# ANSWER / CODE: ______________________________________________
# 2. Explain why lowering only a handler level may not show DEBUG records.
# ANSWER / CODE: ______________________________________________
# 3. Find how repeated setup can duplicate each message.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Configure delivery once and trace thresholds at both levels.

# ============================================================
# END OF LESSON
# ============================================================
