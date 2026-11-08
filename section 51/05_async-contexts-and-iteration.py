# ============================================================
# FILE: 05_async-contexts-and-iteration.py
# TOPIC: Asynchronous Context Managers and Iteration
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply asynchronous context managers and iteration to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# async with awaits entry and exit operations. async for awaits items from an
# asynchronous iterator. Neither syntax requires a network; the example is a
# local simulated session. asynccontextmanager wraps an async generator with one
# yield. Put cleanup in finally so early returns and errors still release it.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def session():
    print("open")
    try:
        yield "demo"
    finally:
        print("close")

async def names():
    for name in ["Ada", "Grace"]:
        await asyncio.sleep(0)
        yield name

async def consume():
    async with session():
        async for name in names():
            print(name)

def example():
    asyncio.run(consume())  # => open, Ada, Grace, close


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Which methods conceptually power async with?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Raise an error while consuming and verify close is printed.
# ANSWER / CODE: ______________________________________________

# 3. How does async for differ from an ordinary for loop?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: async with awaits entry and exit operations.
# ============================================================
# END OF LESSON
# ============================================================
