# ============================================================
# FILE: 04_semaphores-and-bounded-work.py
# TOPIC: Limiting Concurrent Work
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply limiting concurrent work to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# A Semaphore limits how many tasks enter a protected operation simultaneously.
# It does not by itself limit the number of tasks you create or the size of input
# held in memory. For very large streams, use a bounded queue and a fixed worker
# set. Async with releases the permit on success, exception, or cancellation.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio

async def bounded_fetch(value, semaphore):
    async with semaphore:
        await asyncio.sleep(0.001)
        return value.upper()

async def fetch_all():
    semaphore = asyncio.Semaphore(2)
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(bounded_fetch(v, semaphore)) for v in ["a", "b", "c"]]
    return [task.result() for task in tasks]

def example():
    print(asyncio.run(fetch_all()))  # => ['A', 'B', 'C']


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Does a semaphore limit task creation?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Track active operations and verify the peak is at most two.
# ANSWER / CODE: ______________________________________________

# 3. What can happen if you construct millions of pending tasks?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: A Semaphore limits how many tasks enter a protected operation
# simultaneously.
# ============================================================
# END OF LESSON
# ============================================================
