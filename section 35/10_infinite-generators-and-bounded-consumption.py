# ============================================================
# FILE: 10_infinite-generators-and-bounded-consumption.py
# TOPIC: Infinite Generators and Bounded Consumption
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Create an unbounded stream.
# 2. Consume a finite portion without hanging.

from itertools import islice


# SECTION 1 — A STREAM DOES NOT NEED A FINAL ITEM
def ticket_numbers(start=1):
    number = start
    while True:
        yield number
        number += 1


def example_bounded_stream():
    tickets = ticket_numbers(100)
    print(list(islice(tickets, 4)))  # => [100, 101, 102, 103]
    print(next(tickets))            # => 104


# example_bounded_stream()
# islice consumes selected positions without creating the entire input.
# It returns an iterator. Converting this bounded slice to a list is safe.
# Never call list(ticket_numbers()) or sum(ticket_numbers()): there is no
# natural exhaustion. Keep those expressions as comments.
# islice and other itertools tools receive more coverage in section 36.


# SECTION 2 — AN EXPLICIT STOP CONDITION
def example_stop_at_limit():
    stream = ticket_numbers()
    for ticket in stream:
        if ticket > 3:
            break
        print(ticket)
    # => 1
    # => 2
    # => 3
    print(next(stream))  # => 5, because ticket 4 triggered the break.


# example_stop_at_limit()
# break stops this consumer. It does not rewind or close the generator.
# Infinite generators are useful for counters and repeated work, but
# consumers must enforce limits or cancellation.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Generate even numbers forever, then collect only the first five.
# ANSWER / CODE: ______________________________________________
# 2. Explain why the value after the break example is 5 rather than 4.
# ANSWER / CODE: ______________________________________________
# 3. Use islice to skip two tickets and collect the following three.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: An unbounded producer requires a bounded consumer.

# ============================================================
# END OF LESSON
# ============================================================

