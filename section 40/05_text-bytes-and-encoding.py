# ============================================================
# FILE: 05_text-bytes-and-encoding.py
# TOPIC: Encode Text and Decode Bytes
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use UTF-8 explicitly.
# 2. Distinguish character and byte counts.

# SECTION 1 - UNDERSTAND THE IDEA
# str stores Unicode text; bytes stores byte values. encode changes text into
# bytes; decode changes bytes into text using an agreed encoding. A character
# may use multiple UTF-8 bytes. Ignoring decoding errors can silently damage
# data; prefer strict decoding unless you intentionally choose another policy.

# SECTION 2 - WORKED EXAMPLES
def example_encoding():
    text = "Beyoncé"
    data = text.encode("utf-8")
    print(len(text), len(data))     # => 7 8
    print(data.decode("utf-8"))     # => Beyoncé
    try:
        bytes([255]).decode("utf-8")
    except UnicodeDecodeError:
        print("invalid UTF-8")     # => invalid UTF-8

# example_encoding()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Compare character and byte counts for an emoji.
# ANSWER / CODE: ______________________________________________
# 2. Write and read a UTF-8 file containing accented artist names.
# ANSWER / CODE: ______________________________________________
# 3. Explain why decoding UTF-8 bytes with the wrong encoding can corrupt text.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: An encoding is the agreement connecting text to bytes.

# ============================================================
# END OF LESSON
# ============================================================
