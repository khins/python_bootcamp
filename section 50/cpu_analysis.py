"""Worked CPU-analysis project. Safe to import; run explicitly for timings."""
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

def analyze(limit):
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    return sum(value * value for value in range(limit))

def compare(limits, workers=2):
    limits = list(limits)
    if workers < 1:
        raise ValueError("workers must be positive")
    started = perf_counter()
    sequential = [analyze(limit) for limit in limits]
    sequential_seconds = perf_counter() - started
    started = perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as pool:
        parallel = list(pool.map(analyze, limits))
    parallel_seconds = perf_counter() - started
    if parallel != sequential:
        raise AssertionError("sequential and parallel answers differ")
    return sequential, sequential_seconds, parallel_seconds

if __name__ == "__main__":
    values, serial_time, process_time = compare([100_000] * 8)
    print("Results agree:", len(values))
    print(f"Sequential: {serial_time:.4f}s; processes: {process_time:.4f}s")
