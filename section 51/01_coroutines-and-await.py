# ============================================================
# FILE: 01_coroutines-and-await.py
# TOPIC: Coroutines and async/await
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply coroutines and async/await to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Calling an async def function creates a coroutine object; it does not execute
# its body immediately. await runs it and can suspend the current task. asyncio.run
# creates and closes an event loop for a synchronous entry point. Do not call it
# inside an already running event loop; in a notebook await the coroutine instead.
# asyncio.sleep yields control; time.sleep blocks the loop's thread.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio

async def greeting(name):
    await asyncio.sleep(0)
    return f"Hello, {name}"

def example():
    print(asyncio.run(greeting("Ada")))  # => Hello, Ada


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does calling greeting execute it to completion?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Await two greetings sequentially and return a list.
# ANSWER / CODE: ______________________________________________

# 3. Why does an async keyword not make CPU-heavy work parallel?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Calling an async def function creates a coroutine object; it
# does not execute its body immediately.
# ============================================================
# END OF LESSON
# ============================================================
