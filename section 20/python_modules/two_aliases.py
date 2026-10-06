'''from section 20\04_aliases.py'''
# --- 5. Two aliases can refer to the same module ---

import math as first_name
import math as second_name

print(first_name is second_name)  # True
print(first_name.sqrt(16))  # 4.0
print(second_name.sqrt(16))  # 4.0