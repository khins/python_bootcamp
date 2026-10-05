# Create greetings.py and define greet(name) to return a greeting string.
def greet(name):
    return f'greeting string for {name}'

# Define main() to print greet("Kevin") and the current __name__.
if __name__ == "__main__":
    print(greet("Kevin"))

# Call main() under an if __name__ == "__main__": guard.
# print()