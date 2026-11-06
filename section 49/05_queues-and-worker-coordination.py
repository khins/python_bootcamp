# ============================================================
# FILE: 05_queues-and-worker-coordination.py
# TOPIC: Coordinate Work with Queue
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use task_done and join correctly.
# 2. Stop a worker with a sentinel.

# SECTION 1 - UNDERSTAND THE IDEA
# queue.Queue provides synchronized handoff and an optional capacity bound.
# Every get must be matched by task_done, including a sentinel. join waits for
# unfinished tasks, not thread termination; join the worker thread separately.
# Production workers must report errors and still call task_done to avoid a
# blocked join. This example uses one worker so FIFO output is deterministic.

# SECTION 2 - WORKED EXAMPLES
from queue import Queue
from threading import Thread

def example_queue_worker():
    tasks = Queue(maxsize=2)
    results = []
    sentinel = object()
    def worker():
        while True:
            item = tasks.get()
            try:
                if item is sentinel:
                    return
                results.append(item.upper())
            finally:
                tasks.task_done()
    thread = Thread(target=worker)
    thread.start()
    for title in ["Signals", "Blue"]:
        tasks.put(title)
    tasks.put(sentinel)
    tasks.join()
    thread.join()
    print(results)  # => ['SIGNALS', 'BLUE']

# example_queue_worker()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Use one sentinel per worker when adding multiple consumers.
# ANSWER / CODE: ______________________________________________
# 2. Report a task exception without losing task_done.
# ANSWER / CODE: ______________________________________________
# 3. Explain queue capacity as backpressure on the producer.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Queue accounting and worker shutdown are separate responsibilities.

# ============================================================
# END OF LESSON
# ============================================================
