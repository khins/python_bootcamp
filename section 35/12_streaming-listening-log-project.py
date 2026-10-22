# ============================================================
# FILE: 12_streaming-listening-log-project.py
# TOPIC: Project: Stream a Listening Log
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Compose generator stages.
# 2. Aggregate a stream without storing every record.
# 3. Verify empty and malformed input behavior.

from io import StringIO


# SECTION 1 — PARSE ONE LINE AT A TIME
# Input format: artist|song|seconds
# Blank lines and comment lines are ignored.
# Malformed records raise ValueError with the source line number.
# This simple format forbids | inside fields; real CSV needs the csv module.

def parse_listens(lines):
    for line_number, raw in enumerate(lines, start=1):
        text = raw.strip()
        if not text or text.startswith("#"):
            continue
        parts = [part.strip() for part in text.split("|")]
        if len(parts) != 3:
            raise ValueError(f"Line {line_number}: expected three fields")
        artist, song, seconds_text = parts
        if not artist or not song:
            raise ValueError(f"Line {line_number}: missing artist or song")
        try:
            seconds = int(seconds_text)
        except ValueError:
            raise ValueError(f"Line {line_number}: seconds must be an integer") from None
        if seconds < 0:
            raise ValueError(f"Line {line_number}: seconds must be nonnegative")
        yield {"artist": artist, "song": song, "seconds": seconds}


# SECTION 2 — FILTER, THEN AGGREGATE
def long_listens(records, minimum_seconds):
    for record in records:
        if record["seconds"] >= minimum_seconds:
            yield record


def total_seconds_by_artist(records):
    totals = {}
    for record in records:
        artist = record["artist"]
        totals[artist] = totals.get(artist, 0) + record["seconds"]
    return totals


# Parsing and filtering stream records. Aggregation retains one entry
# per distinct artist, so memory is not constant if artist count grows.


# SECTION 3 — AN OFFLINE WORKED EXAMPLE
def example_pipeline():
    sample = """# Synthetic listening history
Rush|Tom Sawyer|270

Joni Mitchell|Blue|180
Rush|Limelight|260
Miles Davis|So What|540
"""
    with StringIO(sample) as source:
        records = parse_listens(source)
        selected = long_listens(records, minimum_seconds=240)
        totals = total_seconds_by_artist(selected)
    print(totals)  # => {'Rush': 530, 'Miles Davis': 540}


# example_pipeline()
# StringIO behaves like a text file but keeps this small fixture in memory.
# For a large real file, replace StringIO(sample) with:
# open(your_path, encoding="utf-8")
# Consume the pipeline inside the with block while the file is still open.
# Do not replace file iteration with read().splitlines() for streaming.


# SECTION 4 — VERIFY EDGE CASES
def example_edge_cases():
    print(total_seconds_by_artist(parse_listens([])))  # => {}
    print(list(parse_listens(["# comment", ""])))      # => []
    records = parse_listens(["Rush|Signals|unknown"])
    try:
        next(records)
    except ValueError as error:
        print(error)  # => Line 1: seconds must be an integer


# example_edge_cases()
# CHALLENGE
# Add tests for missing titles, negative seconds, and the exact threshold.
# Add a stage that selects one artist before aggregation.
# Explain which stages are lazy and which consume their complete input.
# Decide whether malformed rows should abort or be reported and skipped;
# implement and test your chosen policy without silently hiding errors.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Why must aggregation finish before the file's with block ends?
# ANSWER / CODE: ______________________________________________
# 2. Which values are retained in memory as the input grows?
# ANSWER / CODE: ______________________________________________
# 3. Write a fresh pipeline to compute both total seconds and record counts.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Stream intermediate records and retain only the summary you need.

# ============================================================
# END OF LESSON
# ============================================================

