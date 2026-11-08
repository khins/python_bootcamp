# ============================================================
# FILE: 05_concurrent-failures-and-boundaries.py
# TOPIC: Concurrent Failures and Application Boundaries
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply concurrent failures and application boundaries to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# TaskGroup can report several failures that occurred before cancellation settled.
# Do not assume exactly one failure or a stable order. A boundary can translate
# known domain failures into a summary while letting unexpected errors remain
# visible. Catching every Exception and pretending success hides defects. Preserve
# cancellation so supervising tasks can stop work and release resources.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio

async def fail(label):
    raise ValueError(label)

async def run():
    try:
        async with asyncio.TaskGroup() as group:
            group.create_task(fail("first"))
            group.create_task(fail("second"))
    except* ValueError as errors:
        print("concurrent failures reported")  # Count/order not a general guarantee.

def example():
    asyncio.run(run())


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why should a caller not rely on failure ordering?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add cleanup in a sibling task and verify it runs on cancellation.
# ANSWER / CODE: ______________________________________________

# 3. Which errors should a public boundary translate, and which should stay visible?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: TaskGroup can report several failures that occurred before
# cancellation settled.
# ============================================================
# END OF LESSON
# ============================================================
