# ============================================================
# FILE: 03_cancellation-and-timeouts.py
# TOPIC: Cancellation and Timeouts
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply cancellation and timeouts to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Cancellation is cooperative: CancelledError is injected at a suspension point.
# Use finally for cleanup and normally re-raise cancellation after cleanup.
# CancelledError is a BaseException subclass, not an Exception subclass.
# asyncio.timeout bounds a block and turns its cancellation into TimeoutError
# outside the context. Timeouts cannot interrupt CPU loops that never yield.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio

async def slow_operation():
    try:
        await asyncio.sleep(10)
    finally:
        print("cleanup")

async def run_timed():
    try:
        async with asyncio.timeout(0.01):
            await slow_operation()
    except TimeoutError:
        print("timed out")

def example():
    asyncio.run(run_timed())  # => cleanup, then timed out


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Where should TimeoutError be caught?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Cancel a task explicitly, await it, and confirm cleanup ran.
# ANSWER / CODE: ______________________________________________

# 3. Why is swallowing cancellation dangerous for TaskGroup?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Cancellation is cooperative: CancelledError is injected at a
# suspension point.
# ============================================================
# END OF LESSON
# ============================================================
