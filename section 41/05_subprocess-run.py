# ============================================================
# FILE: 05_subprocess-run.py
# TOPIC: Run a Child Process
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Pass an argument list without a shell.
# 2. Handle failure and timeouts.

# SECTION 1 - UNDERSTAND THE IDEA
# subprocess.run waits for a child and returns a CompletedProcess. A list of
# arguments avoids shell parsing. sys.executable selects the current Python.
# check=True raises CalledProcessError on a nonzero status; timeout bounds the
# wait. capture_output stores output in memory, so do not capture unbounded logs.

# SECTION 2 - WORKED EXAMPLES
import subprocess
import sys

def example_child():
    result = subprocess.run([sys.executable, "-c", "print(6 * 7)"],
                            capture_output=True, text=True, check=True, timeout=5)
    print(result.stdout.strip(), result.returncode)  # => 42 0
    try:
        subprocess.run([sys.executable, "-c", "raise SystemExit(3)"],
                       check=True, capture_output=True, timeout=5)
    except subprocess.CalledProcessError as error:
        print(error.returncode)  # => 3

# example_child()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Capture both stdout and stderr from a small child script.
# ANSWER / CODE: ______________________________________________
# 2. Handle TimeoutExpired separately from a nonzero exit.
# ANSWER / CODE: ______________________________________________
# 3. Explain why untrusted input should not be interpolated into a shell command.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use explicit arguments, status checking, and bounded waits.

# ============================================================
# END OF LESSON
# ============================================================
