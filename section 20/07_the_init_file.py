# Packages and __init__.py — Study Summary
# Instructor summary:
# - A package organizes related modules and can contain nested subpackages.
# - Place __init__.py inside a directory to make it a regular Python package.
# - __init__.py may be empty; Python executes it when first importing the package.
# - Importing a module inside a package initializes its parent packages first.
# - Dots in import paths separate package, subpackage, and module names.
# - Use module attributes through dot notation or import specific names directly.
# - Repeated normal imports reuse packages and modules cached in the interpreter.
#
# Clarifications and connections:
# - A package is also a kind of module, with its own namespace and attributes.
# - Modern Python also supports namespace packages without __init__.py.
#   This lesson uses regular packages with explicit __init__.py files.
# - import feature does NOT automatically import every module or subpackage
#   inside feature. Its __init__.py can explicitly import them if needed.
# - A loaded submodule is available as an attribute on its parent package.
# - Importing a nested module initializes the packages along its import path,
#   not every sibling package in the project.
# - Initialization happens once per normal cached import, not on every access.
#   A fresh Python process performs initialization again.
# - __init__.py normally runs through imports, not as a directly launched script.
# - The project's location must be discoverable through Python's import path.
#   Running main.py from the example layout provides a straightforward setup.


# --- 1. Build the example directory structure ---
# The following examples belong in separate files. They remain commented here
# so this lesson can be read or run without creating the example package first.
#
# package_demo/
#     main.py
#     feature/
#         __init__.py
#         copyright.py
#         subfeature/
#             __init__.py
#             calculator.py
#
# Each __init__.py has two underscores before and after init.
# Use lowercase filenames exactly as shown in the import statements.


# --- 2. Add code to each package file ---
# In feature/__init__.py:
# print("Initializing feature")
#
# In feature/copyright.py:
# date_of_copyright = 2020
#
# In feature/subfeature/__init__.py:
# print("Initializing subfeature")
#
# In feature/subfeature/calculator.py:
# def subtract(a, b):
#     return a - b
#
# The print calls reveal initialization order for this lesson. Real packages
# often leave __init__.py empty or use it to expose selected public names.
# An empty file is enough to mark a regular package.


# --- 3. Import only the top-level package ---
# Put this in main.py and run it in a fresh Python process:
# import feature
#
# print(feature.__name__)
#
# Expected:
# Initializing feature
# feature
#
# This does not import copyright.py or initialize subfeature with the sample
# __init__.py contents above. A directory's contents are not loaded automatically.
# Leave this intentional error commented out in this experiment:
# print(feature.copyright.date_of_copyright)  # AttributeError: not imported yet


# --- 4. Import a module inside the package ---
# Replace main.py with this example and run it in a fresh process:
# import feature.copyright
#
# print(feature.copyright.date_of_copyright)
#
# Expected:
# Initializing feature
# 2020
#
# Python first initializes feature, then loads feature.copyright.
# The import binds feature in main.py; copyright is an attribute on that package.
# The subfeature package is not needed for this import and is not initialized.


# --- 5. Import a nested package or module ---
# Importing just the nested package in a fresh process:
# import feature.subfeature
#
# Expected:
# Initializing feature
# Initializing subfeature
#
# This does not itself load calculator.py with the sample initializers above.
# To load the calculator module, use this separate main.py experiment:
# import feature.subfeature.calculator
#
# print(feature.subfeature.calculator.subtract(10, 5))
#
# Expected in a fresh process:
# Initializing feature
# Initializing subfeature
# 5
#
# Import order follows the path: feature, then subfeature, then calculator.


# --- 6. Parent initialization is reused ---
# In a fresh main.py process:
# import feature.subfeature.calculator
# import feature.copyright
# import feature.subfeature.calculator
#
# print(feature.subfeature.calculator.subtract(10, 5))
# print(feature.copyright.date_of_copyright)
#
# Expected:
# Initializing feature
# Initializing subfeature
# 5
# 2020
#
# The first import initializes both packages. The second reuses feature and
# loads copyright. The third reuses the already-loaded calculator module.
# Neither __init__.py prints a second time in this process.


# --- 7. Use from imports at different levels ---
# These are separate alternatives for main.py. Each initializes feature and
# subfeature if they have not already been loaded in the current process.
#
# Import a subpackage:
# from feature import subfeature
# print(subfeature.__name__)  # feature.subfeature
#
# Import a module from the subpackage:
# from feature.subfeature import calculator
# print(calculator.subtract(10, 3))  # 7
#
# Import a function directly from the module:
# from feature.subfeature.calculator import subtract
# print(subtract(10, 3))  # 7
#
# The local names bound by these alternatives are subfeature, calculator,
# and subtract, respectively. Their different prefixes reflect what was imported.


# --- 8. Practice: predict, explain, then run ---
# Use the package files from sections 1 and 2 without changing their contents.
# Treat each exercise as a separate main.py run in a fresh Python process.
# Write predictions in ANSWER comments before running your code.
# Keep intentional-error examples commented out.

# Exercise 1 — Import the package
# Predict every output line. Does subfeature's __init__.py run? Explain.
# import feature
# print("Ready")
# ANSWER:


# Exercise 2 — Follow the nested path
# Predict every output line in order.
# import feature.subfeature.calculator
# print(feature.subfeature.calculator.subtract(8, 2))
# Explain which two __init__.py files execute and in which order.
# ANSWER:


# Exercise 3 — Reuse an initialized parent
# Predict every output line. How many times does each initializer print?
# import feature.copyright
# import feature.subfeature.calculator
# import feature
# print(feature.copyright.date_of_copyright)
# ANSWER:


# Exercise 4 — Import a function directly
# Predict every output line. Explain which name becomes available in main.py.
# from feature.subfeature.calculator import subtract
# print(subtract(20, 7))
# Would calculator.subtract(20, 7) work in this script without another import?
# ANSWER:


# Exercise 5 — Diagnose an unloaded submodule
# Explain why the second line fails with the sample package contents.
# Add an import that makes access to the copyright module work.
# import feature
# print(feature.copyright.date_of_copyright)  # Intentional AttributeError
# ANSWER:


# Exercise 6 — Write your own package imports
# 1. Create the example directory structure and file contents from sections 1–2.
# 2. In main.py, import calculator with from feature.subfeature import calculator.
# 3. Import copyright with from feature import copyright.
# 4. Print calculator.subtract(15, 6) and copyright.date_of_copyright.
# 5. Predict the full output, including the initializer messages, in order.
# 6. Explain why feature's initializer runs only once in this process.
# Write your code in the separate files described above:


# Optional challenge — Organize album labels in a package
# Work through this one together when you are ready.
# Create this separate layout:
# music_demo/
#     main.py
#     music/
#         __init__.py
#         labels.py
#
# 1. Keep music/__init__.py empty initially.
# 2. In labels.py, define album_label(title, artist, year) to return a string
#    such as "Hemispheres by Rush (1978)".
# 3. In main.py, import album_label directly from music.labels.
# 4. Create three album dictionaries with title, artist, and year keys.
# 5. Loop over the dictionaries, unpack each into album_label(), and collect
#    the returned strings in a new list. Print that list after the loop.
# 6. Temporarily add print("Initializing music") to music/__init__.py.
#    Predict where this message appears when main.py runs in a fresh process.
# 7. Explain why importing a function from music.labels initializes music too.
# Leave the original album dictionaries unchanged.
# Write your code in the separate files described above:
