# calculator.py
creator = "Kevin"
PI = 3.14159

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

# Add multiply(a, b) to calculator.py and return the product of its arguments.
def multiply(a, b):
    return a * b



area = 100

if __name__ == "__main__":
    print("Calculator demo")
    print(subtract(3, 5))

import calculator as calc

print(calc.add(3, 5))  # 8
print(calc.subtract(10, 4))  # 6
print(calc.creator)  # Boris — with the original lesson's definition
print(calc.__name__)  # calculator    