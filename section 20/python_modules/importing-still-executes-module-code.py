# Exercise 5 — Importing still executes module code
# Suppose greeting_tools.py contains:
# print("Loading greetings")
#
# def greet(name):
#     return f"Hello, {name}!"
#
# Predict the output order when this separate script runs in a fresh process:
from greeting_tools import greet

print(greet("Kevin"))
# Explain why importing only greet does not skip the top-level print.
# ANSWER: