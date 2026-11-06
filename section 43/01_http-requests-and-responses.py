# ============================================================
# FILE: 01_http-requests-and-responses.py
# TOPIC: HTTP Request and Response Anatomy
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Identify method, URL, status, headers, and body.
# 2. Separate HTTP success from valid application data.

# SECTION 1 - UNDERSTAND THE IDEA
# A request has a method, URL, headers, and sometimes a body. A response has a
# status, headers, and body. 2xx indicates HTTP success, 4xx a client-side
# request problem, and 5xx a server failure. A 200 body can still be malformed
# for your schema; a 204 response may have no body to parse. Offline examples
# below represent responses as ordinary dictionaries, not real HTTP objects.

# SECTION 2 - WORKED EXAMPLES
def example_response():
    response = {"status": 200, "headers": {"Content-Type": "application/json"},
                "body": {"albums": [{"title": "Signals"}]}}
    print(response["status"])  # => 200
    print(response["body"]["albums"][0]["title"])  # => Signals
    print(200 <= response["status"] < 300)  # => True

# example_response()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Describe a GET request for a catalog page.
# ANSWER / CODE: ______________________________________________
# 2. Explain how 404 differs from a malformed JSON body.
# ANSWER / CODE: ______________________________________________
# 3. Decide what to return for a documented 204 response.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Validate both the transport outcome and the response data.

# ============================================================
# END OF LESSON
# ============================================================
