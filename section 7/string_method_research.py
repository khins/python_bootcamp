# 1. Some methods need arguments
text = "Learning Python"
print(text.upper())  # LEARNING PYTHON

# 2. Methods return values
position = text.find("Python")
print(position)  # 9

# 3. Strings count positions starting at zero
'''
Both find() and index() return the starting position of the first match:
Character:  b  a  n  a  n  a
Index:      0  1  2  3  4  5
'''
fruit = "banana"

print(fruit.find("na"))   # 2
print(fruit.index("na"))  # 2

# 4. Their main difference is what happens when nothing matches
'''
| Method | Match found | Match missing |
|---|---|---|
| `find()` | Returns its starting index | Returns `-1` |
| `index()` | Returns its starting index | Raises a `ValueError` |
An unhandled error stops the program. For now, use find() when you want to
check whether something exists without handling an error.
'''
print(fruit.find("z"))   # -1
#print(fruit.index("z"))  # ValueError

# 5. Searching is case-sensitive
text = "Hello Python"

print(text.find("Python"))  # 6
print(text.find("python"))  # -1
message = "I love Python"

print(message.find("I"))
print(message.find("love"))
print(message.index("Python"))
print(message.find("Java"))
print(message.find("Love"))