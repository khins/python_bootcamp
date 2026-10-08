# --- 5. __all__ controls a module's star exports ---
# To try this independently, create export_demo.py with these contents:
#
__all__ = ["creator", "_year"]
creator = "Boris"
_year = 2020
description = "Calculator tools"
#
# Then use a separate script:
# from export_demo import *
#
print(creator)  # Boris
print(_year)  # 2020 — explicitly listed in __all__
print(description)  # Intentional NameError; keep commented out
#
# description still exists in export_demo. __all__ limits the star import;
# it does not delete attributes or prevent explicit access to them.
# An empty __all__ list exports no names through a star import.

# export_demo.py                     Your script

# creator = "Boris"  ──────────────► creator
# _year = 2020       ──────────────► _year

# description = ...                 ✗ not imported by *