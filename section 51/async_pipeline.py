"""Bounded worker pipeline with simulated I/O and structured cancellation."""
import asyncio

async def fake_fetch(value):
    await asyncio.sleep(0.001)
    if value == "bad":
        raise ValueError("invalid synthetic item")
    return value.upper()

async def pipeline(values, concurrency=2, fetch=fake_fetch):
    if concurrency < 1:
        raise ValueError("concurrency must be positive")
    queue = asyncio.Queue(maxsize=concurrency)
    results = {}
    sentinel = object()

    async def produce():
        for index, value in enumerate(values):
            await queue.put((index, value))
        for _ in range(concurrency):
            await queue.put(sentinel)

    async def consume():
        while True:
            item = await queue.get()
            try:
                if item is sentinel:
                    return
                index, value = item
                results[index] = await fetch(value)
            finally:
                queue.task_done()

    async with asyncio.TaskGroup() as group:
        group.create_task(produce())
        for _ in range(concurrency):
            group.create_task(consume())
    return [results[index] for index in sorted(results)]

if __name__ == "__main__":
    print(asyncio.run(pipeline(["signals", "blue", "kind of blue"])))
