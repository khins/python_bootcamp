# --- 7. Local reassignment does not change the module attribute ---
# Try this in a separate script:
# after a direct import, the local name pi and the module attribute math.pi are two separate names.
import math
from math import pi
# Your script

# math ─────────────► math module
#                          │
#                          └── pi ──► 3.141592653589793
#
pi = 3 # Instead, you're rebinding the local name pi.
# Your script

# math ─────────────► math module
#                          │
#                          └── pi ─────┐
#                                     │
# pi ─────────────────────────────────┘
#                                     ▼
#                            3.141592653589793
print(pi)  # 3
print(math.pi)  # 3.141592653589793
#
# pi = 3 rebinds the local name. It does not assign to math.pi.
# A directly imported name is not a live link to future attribute reassignments.

# Your script                         math module
# ───────────                         ───────────

# pi ──────► 3                       pi ──────► 3.141592653589793

# math ─────────────────────────────► math module
# pi = 3 rebinds the local name.
# It does not assign to math.pi.
# A directly imported name is not a live link to future attribute reassignments.
# "Take the object currently referenced by math.pi and bind my local name pi to it."
# So the mental rule for this lesson is:
# from math import pi gives your script its own name pi. Reassigning that local name does not reassign math.pi.