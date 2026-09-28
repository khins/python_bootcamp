# __init__.py, Relative Imports, and Re-exporting Names — Study Summary
# Instructor summary:
# - __init__.py can expose selected names from modules inside its package.
# - Importing those names in __init__.py makes them attributes of the package.
# - This is often called re-exporting: callers can use a shorter package-level
#   path without knowing which internal module implements each function.
# - from .calculator import subtract imports from calculator in the same package.
# - A package can expose useful names from several internal modules.
# - Parent packages can re-export names again to provide an even shorter path.
#
# Clarifications and connections:
# - A leading dot means the current PACKAGE, not the shell's working directory.
# - Two leading dots refer to the parent package.
# - Relative imports can appear in other package modules, not just __init__.py.
# - They require package context; directly running a file that uses a relative
#   import can raise ImportError because no parent package is known.
# - __init__.py supplies the package's namespace, so its imported names become
#   ordinary package attributes. The original module and its functions remain.
# - Re-exporting a function binds a reference to it; it does not copy or move it.
# - __all__ controls star imports. It is not required for ordinary attribute access
#   or explicit from imports, and it does not make unlisted attributes private.
# - Re-exporting loads the referenced modules during package initialization.
# - Circular imports can occur if those modules depend on package names that
#   have not yet been initialized. Keep dependencies straightforward.


# --- 1. Set up the example package ---
# These examples belong in separate files and remain commented here so this
# lesson does not require an existing feature package just to be opened or run.
#
# package_demo/
#     main.py
#     feature/
#         __init__.py
#         subfeature/
#             __init__.py
#             calculator.py
#
# Initially leave both __init__.py files empty.
# In feature/subfeature/calculator.py, place:
#
# creator = "Boris"
# PI = 3.14159
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def area(radius):
#     return PI * radius * radius
#
# Run main.py as the entry point for each experiment below.


# --- 2. Access the original nested module ---
# In main.py, before adding any re-exports:
# import feature.subfeature.calculator
#
# print(feature.subfeature.calculator.subtract(20, 9))  # 11
#
# The full path identifies the package, subpackage, module, and function.
# A direct import is another option if only this function is needed:
# from feature.subfeature.calculator import subtract
# print(subtract(20, 9))  # 11


# --- 3. Re-export names from the subpackage ---
# Replace the contents of feature/subfeature/__init__.py with:
# from .calculator import PI, add, area, creator, subtract
#
# Then use this in main.py:
# import feature.subfeature
#
# print(feature.subfeature.subtract(20, 9))  # 11
# print(feature.subfeature.add(3, 5))  # 8
# print(feature.subfeature.creator)  # Boris
# print(feature.subfeature.PI)  # 3.14159
#
# Python initializes feature, then subfeature. While executing subfeature's
# __init__.py, it imports calculator and binds the selected names in subfeature.
# The caller no longer needs calculator in the attribute path.


# --- 4. Read the relative import precisely ---
# Inside feature/subfeature/__init__.py:
# from .calculator import subtract
#
# The dot means feature.subfeature, the package containing this initializer.
# The module being imported is feature.subfeature.calculator.
# This is an absolute-import alternative for the same module:
# from feature.subfeature.calculator import subtract
#
# The relative spelling expresses the relationship within the package without
# repeating its full name. It is not based on whichever folder the shell is in.
# Do not launch __init__.py directly to test this; import the package from main.py.


# --- 5. Import a re-exported function directly ---
# With the re-exports from section 3 in place, this also works in main.py:
# from feature.subfeature import subtract
#
# print(subtract(20, 9))  # 11
#
# Both access paths still refer to the same function object:
# from feature.subfeature import calculator, subtract
#
# print(subtract is calculator.subtract)  # True
#
# The function remains defined in calculator.py. Re-exporting adds another
# way to access it; it does not remove the original path.


# --- 6. Re-export again from the parent package ---
# Keep the subpackage re-exports from section 3.
# In feature/__init__.py, add:
# from .subfeature import add, subtract
#
# In main.py:
# import feature
#
# print(feature.subtract(20, 9))  # 11
# print(feature.add(3, 5))  # 8
#
# The dot now means feature because this import is inside feature/__init__.py.
# Its initialization imports subfeature, which in turn imports calculator.
# Only add and subtract are explicitly re-exported at this parent level.
# PI does not automatically become feature.PI merely because it exists in
# feature.subfeature. Each initializer selects its own names.


# --- 7. Expose names from more than one module ---
# Add feature/subfeature/labels.py containing:
# def album_label(title, artist):
#     return f"{title} by {artist}"
#
# Add this import to feature/subfeature/__init__.py:
# from .labels import album_label
#
# In main.py:
# from feature.subfeature import add, album_label
#
# print(add(3, 5))  # 8
# print(album_label("Hemispheres", "Rush"))  # Hemispheres by Rush
#
# Callers can access selected functions from calculator.py and labels.py through
# one package interface, without having to remember each implementation file.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before testing each example.
# Use the separate package files described above.
# Each exercise specifies which re-exports it assumes; run in a fresh process
# after editing package files so an earlier import cache does not hide changes.

# Exercise 1 — Shorten the path
# Assume subfeature/__init__.py contains:
# from .calculator import subtract
#
# Rewrite this main.py code to access subtract through the subpackage directly:
# import feature.subfeature.calculator
# print(feature.subfeature.calculator.subtract(12, 5))
# Predict the output.
# ANSWER:


# Exercise 2 — What does the dot mean?
# Inside feature/subfeature/__init__.py, explain what package the leading dot
# refers to in from .calculator import add.
# Write the equivalent absolute import.
# ANSWER:


# Exercise 3 — Selected names only
# Assume feature/__init__.py is empty and subfeature/__init__.py contains only:
# from .calculator import add
#
# Which expressions succeed after import feature.subfeature in main.py?
# A: feature.subfeature.add(2, 3)
# B: feature.subfeature.subtract(8, 2)
# C: feature.subfeature.calculator.subtract(8, 2)
# Explain why the original module remains accessible, even though only add
# was explicitly re-exported. Keep the failing expression commented out.
# ANSWER:


# Exercise 4 — Follow two levels of re-exports
# Assume feature/__init__.py contains from .subfeature import subtract,
# and subfeature/__init__.py contains from .calculator import subtract.
# Predict the output of this main.py code:
# import feature
# print(feature.subtract(15, 6))
# Explain the initialization path that makes feature.subtract available.
# ANSWER:


# Exercise 5 — One function, two access paths
# Assume subfeature/__init__.py re-exports subtract from calculator.
# Predict both outputs and explain why re-exporting does not duplicate a function.
# from feature.subfeature import calculator, subtract
# print(subtract is calculator.subtract)
# print(subtract(9, 4))
# ANSWER:


# Exercise 6 — Design a small package interface
# 1. Create the layout and calculator definitions from section 1.
# 2. Re-export only add and area explicitly in subfeature/__init__.py.
# 3. In main.py, import add and area from feature.subfeature.
# 4. Print add(10, 4) and area(2), and predict both outputs.
# 5. Explain why no calculator prefix is needed in main.py.
# 6. Explain whether an __all__ declaration is required for these explicit imports.
# Write your code in the separate files described above:


# Optional challenge — A music package with a simple public interface
# Work through this one together when you are ready.
# Create this separate layout:
# music_demo/
#     main.py
#     music/
#         __init__.py
#         labels.py
#         totals.py
#
# 1. In labels.py, define album_label(title, artist, year) to return a label
#    such as "Hemispheres by Rush (1978)".
# 2. In totals.py, define total_tracks(*counts) to return sum(counts).
# 3. Use relative imports in music/__init__.py to re-export both functions.
# 4. In main.py, import album_label and total_tracks directly from music.
# 5. Print a label of your choice and total_tracks(4, 7, 6).
# 6. Explain how Python finds each function through music/__init__.py and why
#    main.py does not need to name labels.py or totals.py in its imports.
# Write your code in the separate files described above:
