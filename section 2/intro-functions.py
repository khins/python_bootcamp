'''
A **function** is a named, reusable block of code that performs a task.
 You define it once, then **call** it whenever you want it to run.

In Python, defining a function involves:

- The keyword `def`
- A function name followed by parentheses `()`
- A colon `:`
- An indented body containing the instructions

Defining a function doesn’t run it—calling it does.

Try defining a function named `greet` that prints a short greeting. Share your attempt, and I’ll check it.
Your code is correct! It prints:

```text
Hello Bob how are you
```

- `name` is a **parameter**—a placeholder for input.
- `'Bob'` is the **argument** you pass when calling `greet`.
- The **f-string** inserts the value of `name` into the greeting.
- `return` sends the string back to the caller; `print()` displays it.

Quick check: if you called `greet('Bob')` without `print()` in your Python file, would anything appear in the terminal?
'''
def greet(name):
    return f'Hello {name} how are you'

print(greet('Bob'))