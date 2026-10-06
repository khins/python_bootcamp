# Exercise 2 — Diagnose a missing name
# In a fresh script, 
import datetime as dt
#
print(dt.date(2025, 1, 2)) 
# ANSWER:
# explain why the last line fails when it is datetime.date and correct it:
# the correction is shown above by using the aliases of dt ; datetime failed because we changed it 
# to use a aliase in the import statement ;
# datetime.date fails because the datetime module was imported
# using the alias dt. Therefore, the name datetime is not defined
# in this script. We must reference the module using its alias dt.

# import datetime as dt

# Your script's namespace:

# dt ─────────► datetime module
#                  │
#                  ├── date
#                  ├── time
#                  ├── datetime
#                  └── timedelta

# "Import this module, but in my program I'm going to refer to it by this name."