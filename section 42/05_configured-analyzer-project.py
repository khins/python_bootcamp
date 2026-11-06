# ============================================================
# FILE: 05_configured-analyzer-project.py
# TOPIC: Project: Configurable Analyzer with Logs
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Combine validated settings and diagnostics.
# 2. Keep business results independent of log destination.

# SECTION 1 - UNDERSTAND THE IDEA
# This extends the listening analyzer with minimum-duration filtering and a
# configurable log level. Inputs are synthetic trusted rows; configuration is
# validated before processing. The application creates its logger and hands it
# to the worker rather than hiding global configuration inside the worker.

# SECTION 2 - WORKED EXAMPLES
import logging
import tomllib
from collections import Counter
from io import StringIO

def analyze(rows, minimum, logger):
    counts = Counter()
    for row in rows:
        if row["seconds"] >= minimum:
            counts[row["artist"]] += 1
        else:
            logger.debug("Skipped a short listen")
    logger.info("Summarized %d artist(s)", len(counts))
    return dict(counts)

def example_configured_project():
    config = tomllib.loads('minimum_seconds = 30\nlog_level = "INFO"')
    minimum = config["minimum_seconds"]
    if type(minimum) is not int or minimum < 0:
        raise ValueError("minimum_seconds must be a nonnegative integer")
    level = config["log_level"]
    if level not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
        raise ValueError("invalid log level")
    output = StringIO()
    logger = logging.Logger("analyzer", level=level)
    handler = logging.StreamHandler(output)
    logger.addHandler(handler)
    try:
        rows = [{"artist": "Rush", "seconds": 40}, {"artist": "Yes", "seconds": 10}]
        print(analyze(rows, minimum, logger))  # => {'Rush': 1}
        print(output.getvalue().strip())      # => Summarized 1 artist(s)
    finally:
        logger.removeHandler(handler)
        handler.close()

# example_configured_project()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add environment overrides with explicit precedence.
# ANSWER / CODE: ______________________________________________
# 2. Use a temporary log file and verify no duplicate handlers across runs.
# ANSWER / CODE: ______________________________________________
# 3. Reject a negative minimum and demonstrate a useful error message.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Configuration selects behavior; logs explain what the application did.

# ============================================================
# END OF LESSON
# ============================================================
