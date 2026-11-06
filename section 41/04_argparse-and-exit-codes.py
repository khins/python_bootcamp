# ============================================================
# FILE: 04_argparse-and-exit-codes.py
# TOPIC: Parse CLI Options
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Define positional and optional arguments.
# 2. Return process status deliberately.

# SECTION 1 - UNDERSTAND THE IDEA
# argparse converts command-line strings and supplies help/error messages.
# parse_args accepts a list for testing without touching sys.argv. main should
# return 0 on success and a nonzero value on failure. raise SystemExit(main())
# turns that value into the process exit code. argparse uses code 2 for usage errors.

# SECTION 2 - WORKED EXAMPLES
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Preview a catalog filter")
    parser.add_argument("artist")
    parser.add_argument("--minimum-year", type=int, default=1900)
    parser.add_argument("--verbose", action="store_true")
    return parser

def example_arguments():
    args = build_parser().parse_args(["Rush", "--minimum-year", "1980", "--verbose"])
    print(args.artist, args.minimum_year, args.verbose)  # => Rush 1980 True

# example_arguments()
# A real entry point ends with: if __name__ == "__main__": raise SystemExit(main())

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add an output Path argument.
# ANSWER / CODE: ______________________________________________
# 2. Test a noninteger year and inspect the usage error.
# ANSWER / CODE: ______________________________________________
# 3. Explain why printing an error alone does not set a failure exit code.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A CLI translates text arguments into validated application inputs.

# ============================================================
# END OF LESSON
# ============================================================
