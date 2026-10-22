# ============================================================
# FILE: 03_fetch-html-with-requests.py
# TOPIC: Fetching HTML with Requests
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Make a request with timeouts and status checks.
# 2. Distinguish response bytes, text, and final URL.

# SECTION 1 — AN EXPLICIT LIVE REQUEST
# This example accesses https://example.com only when you uncomment its call.
# Network availability and remote page contents are not guaranteed.

def example_live_request():
    import requests

    response = requests.get(
        "https://example.com",
        headers={"User-Agent": "PythonBootcampLearning/1.0"},
        timeout=(3.05, 10),
    )
    response.raise_for_status()
    print(response.status_code)  # Normally 200; external state may change.
    print(response.url)          # Final URL after redirects.
    print(response.headers.get("Content-Type", "unknown"))
    print(response.text[:80])    # Decoded text; content can change.


# example_live_request()
# timeout=(connect_timeout, read_timeout) sets connection/read waits.
# It is not a deadline for the entire download.
# raise_for_status raises for HTTP 4xx/5xx, not for every unusual response.
# A 200 response can still contain a login page or unexpected content.
# response.content is bytes; response.text is decoded using an encoding.
# Use the final response URL as the base when resolving relative links.

# SECTION 2 — LOCAL PRACTICE FIRST
# Inspect the downloaded Content-Type before treating a response as HTML.
# An API's application/json response should normally be handled as JSON.
# Do not assume every URL returns the page structure you expect.
# REFERENCE: https://requests.readthedocs.io/en/latest/user/quickstart/

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. What are the two timeout values controlling?
# ANSWER / CODE: ______________________________________________
# 2. How do response.content and response.text differ?
# ANSWER / CODE: ______________________________________________
# 3. Why can a successful status still produce no album records?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Check the response before attempting to extract page data.

# ============================================================
# END OF LESSON
# ============================================================

