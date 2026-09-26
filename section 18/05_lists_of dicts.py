# Lists of dictionaries — Study Summary
# Instructor summary:
# - A list can contain dictionaries as its elements.
# - Each dictionary can describe one record, such as a concert attendee.
# - Use a list index to select a record, then a dictionary key to select a detail.
# - A for loop over the list gives you one complete dictionary at a time.
# - An inner loop over attendee.items() gives you that dictionary's key-value pairs.
# - The inner loop finishes for the current attendee before the outer loop advances.
# - Indentation shows which statements belong to each loop.
# - len() counts the elements at the level you give it, not every nested element.
# - A loop variable refers to the actual dictionary in the list; iteration does
#   not automatically create a copy.
#
# Correction to the transcript:
# - Python 3.7+ dictionaries preserve insertion order. The outer loop follows
#   list order, and each items() loop follows its dictionary's insertion order.


# --- 1. Build a list of attendee records ---
concert_attendees = [
    {"name": "Taylor", "section": 400, "price_paid": 99.99},
    {"name": "Christina", "section": 200, "price_paid": 149.99},
    {"name": "Jeremy", "section": 100, "price_paid": 0.00},
]
# The outer square brackets create a list.
# Each pair of curly braces creates one dictionary inside that list.
# Commas separate list elements and also separate entries within each dictionary.

print(type(concert_attendees))     # <class 'list'>
print(len(concert_attendees))      # 3 — attendee records
print(type(concert_attendees[0]))  # <class 'dict'>
print(len(concert_attendees[0]))   # 3 — keys in the first record


# --- 2. Select a record, then select its detail ---
print(concert_attendees[0]["name"])        # Taylor
print(concert_attendees[1]["section"])     # 200
print(concert_attendees[2]["price_paid"])  # 0.0
# [1] selects the second dictionary from the list.
# ["section"] selects a value from that dictionary.
# A float written as 0.00 normally prints as 0.0 without special formatting.


# --- 3. The outer loop supplies a complete dictionary ---
for attendee in concert_attendees:
    print(attendee["name"])
# Expected:
# Taylor
# Christina
# Jeremy
# attendee is a dictionary each time, not an index or an attendee's name.
# Use a key lookup when you need just one particular detail.


# --- 4. An inner loop visits every detail in the current record ---
for attendee in concert_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}.")
# Expected:
# The name is Taylor.
# The section is 400.
# The price_paid is 99.99.
# The name is Christina.
# The section is 200.
# The price_paid is 149.99.
# The name is Jeremy.
# The section is 100.
# The price_paid is 0.0.
# Outer loop: select one attendee dictionary.
# Inner loop: visit all three entries in that dictionary.
# Then repeat with the next attendee. This example prints nine lines.


# --- 5. Indentation controls when a statement runs ---
for attendee in concert_attendees:
    print("Attendee:")
    for key, value in attendee.items():
        print(f"{key}: {value}")
    print("End of record")
print("All records complete")
# For each of the three attendees, this prints:
# Attendee:
# ...that attendee's three key-value lines...
# End of record
# After all attendees, it prints All records complete once.
# "End of record" belongs to the outer loop, after the inner loop.
# "All records complete" is outside both loops.


# --- 6. Use selected fields without an inner loop ---
for attendee in concert_attendees:
    if attendee["price_paid"] == 0:
        print(f'{attendee["name"]} received a free ticket.')
# Expected: Jeremy received a free ticket.
# An inner loop is useful for visiting every entry; it is not required just
# because the list contains dictionaries.

# Leave these intentional errors commented out:
# print(concert_attendees["name"])  # TypeError — the outer object is a list
# print(concert_attendees[0]["seat"])  # KeyError — no "seat" key in this record
# print(concert_attendees[3])  # IndexError — this list has only indexes 0, 1, 2

# Empty dictionaries produce no inner iterations; empty lists produce no
# outer iterations. A record with more keys produces more inner iterations.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Use concert_attendees from section 1 where instructed.
# Keep intentional-error lines commented out.

# Exercise 1 — Follow the lookup path
# Predict all three outputs. Identify which brackets use an index and which
# use a dictionary key.
print(concert_attendees[1]["name"]) # Christina
print(concert_attendees[0]["price_paid"]) # 99.99
print(concert_attendees[2]["section"]) # 100
# ANSWER:
# # ANSWER:
# Outputs: Christina, 99.99, 100 (on separate lines).
# The first brackets use a list index to select an attendee dictionary.
# The second brackets use a dictionary key to select a value.


# Exercise 2 — Know the current object
# Predict all four outputs. Explain why the two lengths happen to match here.
print(type(concert_attendees))
print(type(concert_attendees[0]))
print(len(concert_attendees))
print(len(concert_attendees[0]))
# ANSWER:
# Outputs: <class 'list'>
# <class 'dict'>
# 3
# 3
# Explain why the two lengths happen to match here: the list has 3 dictionaries and each dict has 3 elements


# Exercise 3 — Trace both loops
# Predict every output line in order. How many times does the inner print run?
records = [
    {"name": "Kevin", "section": 100},
    {"name": "Alex", "section": 200},
]
for record in records:
    for key, value in record.items():
        print(key, value)
# ANSWER:
# Outputs
# name Kevin
# section 100
# name Alex
# section 200
# How many times does the inner print run?: runs twice for each element in the dict, ultimately 4 times


# Exercise 4 — Empty records and indentation
# Predict every output line. Why does "record finished" still print for {}?
records = [{"name": "Kevin"}, {}, {"name": "Alex"}]
for record in records:
    for key, value in record.items():
        print(value)
    print("record finished")
print("done")
# ANSWER:
# Outputs:
# Kevin
# record finished
# record finished
# Alex
# record finished
# done
# Why does "record finished" still print for {}?: because ther is no elements so the inner
# dict skips to next line of code 

# Exercise 5 — Diagnose the level
# The goal is to print each attendee's name.
# Identify the error in the first iteration and explain its cause.
# Write a corrected loop below. Keep the broken snippet commented out.
# for attendee in concert_attendees:
#     print(concert_attendees["name"])
# ANSWER:
# Outputs
# the first original loop causes a TypeError
index = 0 
for attendee in concert_attendees:
    print(concert_attendees[index]['name'])
    index += 1
# Taylor
# Christina
# Jeremy


# Exercise 6 — Build a list of album records
# 1. Create albums as a list containing three dictionaries.
# 2. Give each dictionary "title", "artist", and "year" keys.
#    Use strings for title and artist, and an integer for year.
#    Fictional sample data is fine.
# 3. Use a loop over albums and an inner items() loop to print every key and value.
# 4. Print a separator after each album, outside the inner loop.
# 5. After both loops, print the number of album records.
# 6. Explain what each of your three loop variables holds.
# Write your code below:
albums = [
    {
        "title": "Emerson, Lake & Palmer",
        "year": 1970,
        "artist": "Emerson, Lake & Palmer",
    },
    {
        "title": "Tarkus",
        "year": 1971,
        "artist": "Emerson, Lake & Palmer",
    },
    {
        "title": "Brain Salad Surgery",
        "year": 1973,
        "artist": "Emerson, Lake & Palmer",
    },
]
album_count = 0
for album in albums:
    for key, value in album.items():
        print(key, value)  
        album_count += 1
    print(f'album count {album_count}')
    print("---")

# Explain what each of your three loop variables holds: the 3 loops hold the key and value and album count
# No inner items() loop is needed because I know the keys I need.
# Each outer iteration gives me one attendee dictionary.
# I look up "price_paid" directly and append "name" when it qualifies.



# Optional challenge — Find attendees within a budget
# Work through this one together when you are ready.
# Define attendee_names_within_budget(attendees, budget).
# Each attendee dictionary has "name" and "price_paid" keys.
# Return a NEW list of names whose prices are less than or equal to budget.
# Use a loop, dictionary lookups, and append(). Preserve attendee order and
# leave the input list and its dictionaries unchanged.
def attendee_names_within_budget(attendees, budget):
    new_list = []
    for attendee in attendees:
        if attendee["price_paid"] <= budget:
            new_list.append(attendee["name"]) 
    return new_list

print(attendee_names_within_budget(concert_attendees, 100)) # => ['Taylor', 'Jeremy']
print(attendee_names_within_budget(concert_attendees, 0)) # => ['Jeremy']
print(attendee_names_within_budget([], 100)) #=> []
# Explain whether you need an inner items() loop for this task and why.
# Write your code below:
