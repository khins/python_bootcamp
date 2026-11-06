# ============================================================
# FILE: 07_bounded-downloader-project.py
# TOPIC: Project: Bounded Concurrent Downloader
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Bound both workers and pending futures.
# 2. Save results and retain individual failures.

# SECTION 1 - UNDERSTAND THE IDEA
# bounded_downloader.py keeps at most max_pending futures submitted at once and
# refills as tasks finish. Indexed filenames avoid trusting URL path text and
# allow duplicate URLs. Exclusive writes reject collisions. The default demo
# uses fake bytes; an optional HTTPS adapter is separate. Task bodies must bound
# their own I/O. Summary dictionaries grow with total tasks even though pending
# work is bounded; stream outcomes instead for huge task lists.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory

def fake_fetch(url):
    if url == "demo://missing":
        raise OSError("not found")
    return ("audio fixture for " + url).encode("utf-8")

def example_downloader_project():
    from bounded_downloader import download_all
    with TemporaryDirectory() as folder:
        successes, failures = download_all(
            ["demo://one", "demo://missing", "demo://two"], Path(folder),
            fake_fetch, workers=2, max_pending=2)
        print(sorted(successes), sorted(failures))  # => [0, 2] [1]
        print(successes[0]["path"].read_bytes().startswith(b"audio"))  # => True
        print(failures[1]["error"])  # => not found

# example_downloader_project()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build your own bounded collector and test empty input plus mixed failures.
# ANSWER / CODE: ______________________________________________
# 2. Verify existing output files are never overwritten.
# ANSWER / CODE: ______________________________________________
# 3. Instrument running and pending counts; explain why output order can vary.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Bound submission and I/O, then collect each outcome explicitly.

# ============================================================
# END OF LESSON
# ============================================================
