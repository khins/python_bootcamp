# ============================================================
# FILE: 04_environment-and-config-files.py
# TOPIC: Load and Validate Configuration
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Read TOML and environment strings.
# 2. Define precedence explicitly.

# SECTION 1 - UNDERSTAND THE IDEA
# Python 3.11 supplies tomllib for reading TOML. Environment variables are text,
# so bool("false") is True and is not a valid boolean parser. Use documented
# values and reject invalid ones. This example uses environment > file > default
# precedence and accepts a mapping so tests need not mutate real environment state.

# SECTION 2 - WORKED EXAMPLES
import tomllib

def settings(file_text, environment):
    values = tomllib.loads(file_text)
    raw = environment.get("CATALOG_VERBOSE", str(values.get("verbose", False)))
    normalized = raw.casefold()
    if normalized not in {"true", "false"}:
        raise ValueError("CATALOG_VERBOSE must be true or false")
    return {"verbose": normalized == "true"}

def example_configuration():
    print(settings("verbose = true", {}))  # => {'verbose': True}
    print(settings("verbose = true", {"CATALOG_VERBOSE": "false"}))
    # => {'verbose': False}

# example_configuration()
# Real entry points can pass os.environ; keep secrets out of committed TOML.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add a positive integer batch_size setting.
# ANSWER / CODE: ______________________________________________
# 2. Test malformed TOML separately from invalid settings.
# ANSWER / CODE: ______________________________________________
# 3. Write down precedence before combining CLI, environment, and file settings.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Parse configuration strings and validate them before use.

# ============================================================
# END OF LESSON
# ============================================================
