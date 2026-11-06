# ============================================================
# FILE: 05_authentication-and-rate-limits.py
# TOPIC: Credentials and Rate-limit Responses
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Keep credentials out of source and logs.
# 2. Interpret retry guidance deliberately.

# SECTION 1 - UNDERSTAND THE IDEA
# An API may require a bearer token in Authorization. Read credentials at the
# application boundary, use HTTPS, and do not print prepared authenticated
# requests. 401 usually concerns authentication; 403 access; 429 rate limiting.
# Retry-After can be seconds or an HTTP date. Respect API rules and cap attempts;
# if a requested wait exceeds your allowed budget, stop rather than retry early.

# SECTION 2 - WORKED EXAMPLES
def authentication_headers(environment):
    token = environment.get("MUSIC_API_TOKEN", "").strip()
    if not token:
        raise ValueError("MUSIC_API_TOKEN is required")
    return {"Authorization": f"Bearer {token}", "Accept": "application/json"}

def example_authentication():
    headers = authentication_headers({"MUSIC_API_TOKEN": "synthetic-demo-only"})
    print(sorted(headers))  # => ['Accept', 'Authorization']; token is not printed
    try:
        authentication_headers({})
    except ValueError as error:
        print(error)  # => MUSIC_API_TOKEN is required

# example_authentication()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Read a token from os.environ without displaying it.
# ANSWER / CODE: ______________________________________________
# 2. Explain why 401 should not be retried repeatedly with unchanged credentials.
# ANSWER / CODE: ______________________________________________
# 3. Describe behavior when Retry-After exceeds your time budget.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Credentials and rate-limit policies belong at the transport boundary.

# ============================================================
# END OF LESSON
# ============================================================
