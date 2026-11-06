# ============================================================
# FILE: 02_requests-parameters-and-timeouts.py
# TOPIC: Use Requests Deliberately
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Prepare encoded query parameters.
# 2. Bound connect and read waits.

# SECTION 1 - UNDERSTAND THE IDEA
# Requests is third-party; setup appears in learning-guide.txt. params encodes
# query strings, headers supplies request metadata, raise_for_status raises on
# HTTP errors, and json parses the body. A (connect, read) timeout is not a total
# end-to-end deadline. The preparation example sends no network traffic. The
# live helper is opt-in and requires a URL you choose; no endpoint is assumed.

# SECTION 2 - WORKED EXAMPLES
def example_prepared_request():
    import requests
    request = requests.Request("GET", "https://example.invalid/albums",
                               params={"artist": "Rush", "page": 1},
                               headers={"Accept": "application/json"}).prepare()
    print("artist=Rush" in request.url)  # => True
    print(request.headers["Accept"])    # => application/json

def fetch_json_live(url):
    import requests
    with requests.Session() as session:
        with session.get(url, timeout=(3.05, 10)) as response:
            response.raise_for_status()
            return response.json()

# example_prepared_request()
# fetch_json_live is deliberately not called by any example.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Prepare an artist containing spaces and inspect the URL.
# ANSWER / CODE: ______________________________________________
# 2. Handle a timeout separately from invalid JSON.
# ANSWER / CODE: ______________________________________________
# 3. Explain why parsing JSON before checking status can hide the real failure.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use explicit timeouts and status checks before consuming an API body.

# REFERENCES
# https://requests.readthedocs.io/en/latest/user/quickstart/

# ============================================================
# END OF LESSON
# ============================================================
