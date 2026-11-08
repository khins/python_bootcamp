# ============================================================
# FILE: 06_batch-errors-project.py
# TOPIC: Project: Report a Batch of Failures
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: report a batch of failures to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# batch_processor.py attempts each record and collects expected RecordError
# instances with causes and index notes. If any record fails, it raises a group
# rather than returning partial data. Successful parsing does not imply an atomic
# external operation: a real import with writes needs a transaction or an explicit
# partial-success policy. Empty input returns an empty list.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from batch_processor import process_batch, RecordError

def example():
    print(process_batch(["1", "2"]))  # => [1, 2]
    try:
        process_batch(["bad", "-1"])
    except* RecordError as errors:
        print(len(errors.exceptions))  # => 2 for this flat group


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why preserve the original cause and record index?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Write tests for empty input, all-valid input, and mixed invalid records.
# ANSWER / CODE: ______________________________________________

# 3. How would you change the API to return partial successes explicitly?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: batch_processor.py attempts each record and collects expected
# RecordError instances with causes and index notes.
# ============================================================
# END OF LESSON
# ============================================================
