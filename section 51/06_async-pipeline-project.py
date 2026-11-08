# ============================================================
# FILE: 06_async-pipeline-project.py
# TOPIC: Project: Bounded Async Pipeline
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: bounded async pipeline to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# async_pipeline.py uses a bounded queue, a fixed number of workers, and TaskGroup.
# It preserves input order by indexing results, despite concurrent execution.
# On failure, TaskGroup cancels sibling workers and the producer, preventing a
# producer blocked on a full queue from hanging forever. This version fails the
# batch rather than silently discarding failed items. The result list still uses
# memory proportional to output; bounded concurrency is not bounded total memory.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio
from async_pipeline import pipeline

async def demonstrate():
    print(await pipeline(["a", "b", "c"]))  # => ['A', 'B', 'C']
    print(await pipeline([]))  # => []
    try:
        await pipeline(["a", "bad", "c"])
    except* ValueError as errors:
        print("failure reported")

def example():
    asyncio.run(demonstrate())


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why use fixed workers as well as a bounded queue?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Put a timeout around pipeline and verify cancellation completes.
# ANSWER / CODE: ______________________________________________

# 3. Design a collect-errors alternative and explain how its contract differs.
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: async_pipeline.py uses a bounded queue, a fixed number of
# workers, and TaskGroup.
# ============================================================
# END OF LESSON
# ============================================================
