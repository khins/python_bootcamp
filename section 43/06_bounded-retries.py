# ============================================================
# FILE: 06_bounded-retries.py
# TOPIC: Retry Transient Reads
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Bound attempts and waiting.
# 2. Distinguish transient from permanent errors.

# SECTION 1 - UNDERSTAND THE IDEA
# The helper in api_client.py retries selected transient statuses and built-in
# transport exceptions. It accepts a sleeper so demonstrations never actually
# wait. It handles both Retry-After forms and refuses an excessive delay.
# Production clients also need a total deadline, jitter, and service-specific
# rules. Requests exceptions require explicit translation to this contract.

# SECTION 2 - WORKED EXAMPLES
def example_retries():
    from api_client import request_page
    replies = iter([(503, None, {}), (429, None, {"Retry-After": "2"}),
                    (200, {"items": [], "next": None}, {})])
    waits = []
    payload = request_page(lambda page: next(replies), 1, sleeper=waits.append)
    print(waits)      # => [1.0, 2.0]
    print(payload)    # => {'items': [], 'next': None}

# example_retries()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Verify a 401 response is attempted only once.
# ANSWER / CODE: ______________________________________________
# 2. Verify three transient failures raise ApiError.
# ANSWER / CODE: ______________________________________________
# 3. Explain why retrying a payment POST is different from retrying a catalog GET.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Retries need an error policy, an attempt limit, and a wait budget.

# ============================================================
# END OF LESSON
# ============================================================
