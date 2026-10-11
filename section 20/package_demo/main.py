# --- 3. Import only the top-level package ---
# Put this in main.py and run it in a fresh Python process:
# import feature.copyright
# import feature.author

# print(feature.copyright.date_of_copyright)
# print(feature.author.author_name)
# import feature.sub_feature.calculator
# from feature.sub_feature import calculator

# # print(feature.sub_feature.calculator.subtract(10, 5))
# print(calculator.subtract(10, 5))
# from feature.sub_feature.calculator import subtract

# print(subtract(10, 5))
# from feature.sub_feature.calculator import subtract as difference

# print(difference(10, 5))
# --- 6. Parent initialization is reused ---
# In a fresh main.py process:
import feature.sub_feature.calculator
import feature.copyright
import feature.sub_feature.calculator
#
print(feature.sub_feature.calculator.subtract(10, 5))
print(feature.copyright.date_of_copyright)
