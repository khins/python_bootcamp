# --- 6. Name collisions replace local bindings ---
# Suppose first_tools.py contains creator = "Boris", and second_tools.py
# contains creator = "Alex". Neither module defines __all__.
# In a separate script:
#
from first_tools import *
print(creator)  # Boris
from second_tools import *
print(creator)  # Alex — the later import replaces the local binding
#
# Module prefixes preserve clarity and allow access to both values:
import first_tools
import second_tools
#
print(first_tools.creator)  # Boris
print(second_tools.creator)  # Alex
#
# Explicit aliases are another option:
from first_tools import creator as first_creator
from second_tools import creator as second_creator