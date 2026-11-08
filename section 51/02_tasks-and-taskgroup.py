# ============================================================
# FILE: 02_tasks-and-taskgroup.py
# TOPIC: Tasks and Structured Concurrency
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply tasks and structured concurrency to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# create_task schedules a coroutine on the running loop. Keep ownership of tasks:
# await their results and handle errors. Python 3.11 TaskGroup scopes related tasks
# and waits for them at exit. A non-cancellation failure cancels remaining siblings
# and is raised as an exception group. Results are safe to read after successful
# exit; completion order can differ from the order tasks were created.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio

async def double(value):
    await asyncio.sleep(0.001)
    return value * 2

async def run_group():
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(double(n)) for n in [1, 2, 3]]
    return [task.result() for task in tasks]

def example():
    print(asyncio.run(run_group()))  # => [2, 4, 6]


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Who waits for the tasks?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Make one task fail and inspect the ExceptionGroup outside the group.
# ANSWER / CODE: ______________________________________________

# 3. What happens to unfinished siblings after a normal task failure?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: create_task schedules a coroutine on the running loop.
# ============================================================
# END OF LESSON
# ============================================================
