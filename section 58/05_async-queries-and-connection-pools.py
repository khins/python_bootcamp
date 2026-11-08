# ============================================================
# FILE: 05_async-queries-and-connection-pools.py
# TOPIC: Async Queries and Connection Pools
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply async queries and connection pools to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# Await asynchronous connection and cursor operations. A pool reuses a bounded
# number of connections; each request borrows one only for its database work.
# An AsyncConnectionPool is opened and closed in application lifespan, not per
# query. Explicit open=False avoids opening during construction. pool.connection()
# commits or rolls back then returns the connection. Avoid awaiting slow unrelated
# network work while holding a scarce connection. One shared connection serializes
# queries and shares transaction state; many tasks do not imply parallel queries.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
import asyncio
from unittest.mock import AsyncMock, MagicMock

async def read_titles(pool):
    async with pool.connection() as connection:
        cursor = await connection.execute("SELECT title FROM albums ORDER BY id")
        return await cursor.fetchall()

def example():
    cursor = MagicMock()
    cursor.fetchall = AsyncMock(return_value=[("Signals",)])
    connection = MagicMock()
    connection.execute = AsyncMock(return_value=cursor)
    pool = MagicMock()
    pool.connection.return_value.__aenter__.return_value = connection
    print(asyncio.run(read_titles(pool)))  # => [('Signals',)]
    pool.connection.return_value.__aexit__.assert_awaited_once()


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Why open one pool per application rather than per query?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Simulate execute raising and verify the async context exits.
# ANSWER / CODE: ______________________________________________

# 3. Why does a single shared connection not provide independent transactions?
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: Await asynchronous connection and cursor operations.
# ============================================================
# END OF LESSON
# ============================================================
