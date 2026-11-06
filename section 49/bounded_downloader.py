"""Bound submissions and collect download outcomes. The default demo is offline.
Completed bytes are written by the collector, not shared worker state.
"""
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from pathlib import Path

MAX_BYTES = 1_000_000

def download_all(urls, destination, fetch, *, workers=3, max_pending=6):
    if type(workers) is not int or workers < 1 or type(max_pending) is not int or max_pending < 1:
        raise ValueError("workers and max_pending must be positive integers")
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    indexed = enumerate(urls)
    successes, failures = {}, {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        pending = {}
        def submit_next():
            try:
                index, url = next(indexed)
            except StopIteration:
                return False
            pending[pool.submit(fetch, url)] = (index, url)
            return True
        for _ in range(max_pending):
            if not submit_next():
                break
        while pending:
            done, _ = wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                index, url = pending.pop(future)
                target = destination / f"download-{index:04d}.bin"
                created = False
                try:
                    data = future.result()
                    if not isinstance(data, bytes) or len(data) > MAX_BYTES:
                        raise ValueError("expected bytes within size limit")
                    with target.open("xb") as output:
                        created = True
                        output.write(data)
                    successes[index] = {"url": url, "path": target}
                except Exception as error:
                    # Per-item boundary: report task/storage failures and continue.
                    if created:
                        target.unlink(missing_ok=True)
                    failures[index] = {"url": url, "error": str(error)}
                submit_next()
    return successes, failures

def fetch_https_live(url):
    # Optional live adapter: no examples call this. Choose only trusted public
    # HTTPS URLs. timeout bounds waits, not a complete wall-clock deadline.
    # Disable redirects so this adapter does not silently switch destinations.
    from urllib.parse import urlsplit
    import requests
    if urlsplit(url).scheme != "https":
        raise ValueError("HTTPS is required")
    with requests.get(url, timeout=(3.05, 10), stream=True, allow_redirects=False) as response:
        if response.status_code != 200:
            raise ValueError(f"HTTP {response.status_code}")
        chunks, size = [], 0
        for chunk in response.iter_content(chunk_size=65536):
            size += len(chunk)
            if size > MAX_BYTES:
                raise ValueError("response exceeds byte limit")
            chunks.append(chunk)
        return b"".join(chunks)
