# ============================================================
# FILE: 01_log-levels.py
# TOPIC: Choose Useful Log Levels
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Distinguish DEBUG through CRITICAL.
# 2. Configure logs in the application entry point.

# SECTION 1 - UNDERSTAND THE IDEA
# DEBUG is diagnostic detail, INFO normal progress, WARNING a recoverable
# problem, ERROR an operation failure, and CRITICAL an application-threatening
# failure. A logger is named by component. Libraries generally obtain loggers
# without configuring global handlers; the application chooses destinations.

# SECTION 2 - WORKED EXAMPLES
import logging
from io import StringIO

def example_levels():
    output = StringIO()
    logger = logging.Logger("catalog-demo", level=logging.INFO)
    handler = logging.StreamHandler(output)
    handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
    logger.addHandler(handler)
    try:
        logger.debug("hidden detail")
        logger.info("Loaded %d albums", 3)
        logger.warning("Missing optional artwork")
        print(output.getvalue(), end="")
        # => INFO:Loaded 3 albums
        # => WARNING:Missing optional artwork
    finally:
        logger.removeHandler(handler)
        handler.close()

# example_levels()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Classify three messages from an importer by level.
# ANSWER / CODE: ______________________________________________
# 2. Explain lazy %s formatting in logging calls.
# ANSWER / CODE: ______________________________________________
# 3. Explain why importing a library should not configure the whole application.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Log levels let the caller select useful detail.

# ============================================================
# END OF LESSON
# ============================================================
