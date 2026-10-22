# ============================================================
# FILE: 01_how-web-scraping-works.py
# TOPIC: The Web Scraping Pipeline
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Separate fetching, parsing, and extraction.
# 2. Prepare scraping dependencies.

# SECTION 1 — FROM PAGE TO RECORDS
# Fetch: obtain HTML bytes/text from a server or a saved file.
# Parse: turn HTML into a tree of elements.
# Extract: locate relevant elements and read text/attributes.
# Clean: normalize and validate the values.
# Save: export structured records.
# Requests retrieves HTTP responses. Beautiful Soup parses HTML.
# Neither Requests nor Beautiful Soup executes page JavaScript.
# Prefer a documented API when it supplies the data you need.

def example_pipeline():
    stages = ["fetch", "parse", "extract", "clean", "save"]
    print(" -> ".join(stages))
    # => fetch -> parse -> extract -> clean -> save


# example_pipeline()

# SECTION 2 — SETUP
# From the repository root, after section 33:
# .\.venv\Scripts\python.exe -m pip install -r "section 34/requirements.txt"
# Examples import third-party libraries inside functions so lesson files
# can be opened/run without immediately requiring installed dependencies.
# Uncomment one example call at a time. Only the explicitly labeled live
# example in lesson 03 makes a network request. Other examples use fixtures.
# The fixtures folder contains synthetic pages, not scraped personal data.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain which stage uses Requests and which uses Beautiful Soup.
# ANSWER / CODE: ______________________________________________
# 2. Install the dependencies using your environment's interpreter.
# ANSWER / CODE: ______________________________________________
# 3. Why might a browser show data absent from downloaded HTML?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Treat scraping as several small, testable transformations.

# ============================================================
# END OF LESSON
# ============================================================

