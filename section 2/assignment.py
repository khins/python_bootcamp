# Use the print function to output the text "I am a developer!"
# Remember -- case sensitivity matters in Python.
# All characters and casings must match the ones in the string above.
print("I am a developer!")

# Use the print function to output the string "a ** b ** c"
# Make sure to use the proper keyword argument to separate the values.
# Don't cheat by manually copying and pasting the string.
print("a","b","c", sep=" ** ")


# Help me out! When I print the two lines below, they are
# separated by a line break. What's peanut butter without
# jelly? NOTHING! Fix the code to ensure the second
# line picks up where the first line concludes. Your
# solution should have 2 print function calls.

print("Peanut butter and ", end="")
print("jelly")

'''
Your assignment practices `print()`, `sep`, and `end`. One small fix: your second exercise produces `a**b**c`, but the requested output is `a ** b ** c`. Hint: spaces count as characters in your separator.

Try these additional exercises:

1. **Date formatting:** Print `2026-09-05` by passing three strings to one `print()` call. Use `sep` to add the hyphens.

2. **Stay on one line:** Use three separate `print()` calls to produce:
   ```text
   Learning Python is fun!
   ```
   Hint: consider how each call should end, including spaces.

3. **Combine both options:** Use one call to print three words separated by ` | ` and end the output with `!`:
   ```text
   code | test | learn!
   ```

4. **Return a greeting:** Define a function named `welcome` that accepts a name and returns a welcome message. Call it for two different names and print each result.

5. **Predict, then run:** What will this display?
   ```python
   print("A", "B", sep="-", end=">")
   print("C", "D", sep="+")
   ```

'''

# 1 Date Formatting 
print("2026","09","05", sep="-")

# 2 print Learning Python is fun!
print("Learning", end="")
print(" Python", end="")
print(" is fun!")

# 3 print code | test | learn!
print("code", "test", "learn", sep=" | ", end="!")

#4 
def welcome(name):
    return f'Welcome {name} to python programming'

# add a blank space for separtion
print("\n")
print(welcome('Nancy'))
print(welcome('Lou'))


# 5 
# Prediction is A and B will have a hyphen separating the letters and will end the string with >
# then C and D will be on the same line with a + between them
print("A", "B", sep="-", end=">")
print("C", "D", sep="+")