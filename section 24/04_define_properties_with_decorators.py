# Define properties with decorators — Study Summary
# Instructor summary:
# - Decorators offer another syntax for creating properties.
# - Place @property immediately above the getter definition.
# - The getter's name becomes the public property name.
# - Place @name.setter immediately above the setter for that property.
# - Use the same name for the getter and setter in this standard pattern.
# - Reading object.dollars invokes the getter without call parentheses.
# - Assigning object.dollars = value invokes the setter with that value.
# - Store one internal value and convert it when reading or writing the property.
# - A setter can check a value before updating internal storage.
#
# Clarifications to the transcript:
# - A decorator is a callable that receives the decorated object and returns
#   its replacement; it does not have to return another function.
# - @property replaces the getter's class-body name with a property object.
# - @dollars.setter creates a new property with the existing getter and the
#   supplied setter, then binds that property to the setter definition's name.
# - This is not method overloading: one property holds both accessors.
# - A property is a managed attribute. Callers still use attribute syntax.
# - Both decorators go ABOVE their respective definitions, not after them.
# - _cents is internal by convention; the underscore does not restrict access.
# - The lesson silently ignores negative updates but accepts zero.
# - Direct initialization of _cents bypasses the setter's validation.
# - Nonnegative balances are a rule for this example, not for all currency data.
# - These examples teach properties, not complete money handling. Multiplying
#   a float by 100 does not guarantee exact integer cents; production code needs
#   an explicit numeric representation and rounding policy.


# --- 1. Define a getter with @property ---
class ReadOnlyCurrency:
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100


balance = ReadOnlyCurrency(50_000)
print(balance.dollars)  # => 50000.0
print(balance._cents)   # => 5000000
# @property is equivalent to dollars = property(dollars) after the getter def.
# The public read converts cents to dollars without storing a second amount.
# Reading _cents here is only to illustrate the internal representation.
# Keep these intentional errors commented out:
# balance.dollars()      # TypeError: the returned float is not callable.
# balance.dollars = 100  # AttributeError: this property has no setter.


# --- 2. Add a setter with the same property name ---
class Currency:
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, new_dollars):
        if new_dollars >= 0:
            self._cents = new_dollars * 100


bank_account = Currency(50_000)
print(bank_account.dollars)  # => 50000.0

bank_account.dollars = 100_000
print(bank_account.dollars)  # => 100000.0
print(bank_account._cents)   # => 10000000
# The getter needs only self. The setter also receives the assigned value.
# new_dollars is a parameter name; it does not need to match the property name.
# @dollars.setter refers to the property created by the preceding @property.
# Without that decorator, a second def dollars would replace the earlier name
# with an ordinary function instead of adding a setter to the property.


# --- 3. Accept valid updates and ignore negative ones ---
bank_account.dollars = -20_000
print(bank_account.dollars)  # => 100000.0
# Assignment invokes the setter, but its condition prevents the storage update.
# The next read invokes the getter and returns the unchanged amount.

bank_account.dollars = 0
print(bank_account.dollars)  # => 0.0
# Zero passes the >= 0 condition. Invalid negative input raises no exception
# in this version; the setter simply finishes without changing _cents.


# --- 4. Compare decorators with the property(...) form ---
class CurrencyWithMethods:
    def __init__(self, dollars):
        self._cents = dollars * 100

    def _get_dollars(self):
        return self._cents / 100

    def _set_dollars(self, new_dollars):
        if new_dollars >= 0:
            self._cents = new_dollars * 100

    dollars = property(_get_dollars, _set_dollars)


decorated = Currency(5)
explicit = CurrencyWithMethods(5)
decorated.dollars = 8
explicit.dollars = 8
print(decorated.dollars)  # => 8.0
print(explicit.dollars)   # => 8.0
# Both forms provide the same public read/write behavior in these examples.
# The decorator form keeps each accessor next to its property declaration.


# --- 5. Apply validation during initialization too ---
negative_balance = Currency(-5)
print(negative_balance.dollars)  # => -5.0
# Currency.__init__ writes _cents directly, so its setter never checks -5.


class ValidatedCurrency:
    def __init__(self, dollars):
        self.dollars = dollars

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter
    def dollars(self, new_dollars):
        if new_dollars < 0:
            raise ValueError("Dollar amount cannot be negative.")
        self._cents = new_dollars * 100


validated = ValidatedCurrency(10)
validated.dollars = 20
print(validated.dollars)  # => 20.0
# Initial assignment to self.dollars invokes the setter, just like later writes.
# This version rejects negative values explicitly at both entry points.
# Assume ordinary numeric inputs; this is not comprehensive type validation.
# Keep these intentional errors commented out:
# ValidatedCurrency(-5)  # ValueError: Dollar amount cannot be negative.
# validated.dollars = -1 # ValueError; the existing amount remains unchanged.
# Routing initialization through the original silent setter alone could leave
# _cents missing after a negative initial value, so rejection matters here.


# --- 6. Avoid recursive access and mismatched decorator names ---
# A dollars getter must read backing storage, not return self.dollars.
# A dollars setter must update backing storage, not assign self.dollars again.
# Accessing the same property inside its own accessor repeatedly calls that
# accessor until Python raises RecursionError.
#
# Correct bodies for this lesson:
# Getter: return self._cents / 100
# Setter: self._cents = new_dollars * 100
#
# Use @dollars.setter, not @property.setter or @cents.setter.
# The name before .setter must refer to the property being extended.
# Keep the setter definition named dollars to rebind that same public name.
# No deleter was defined, so del bank_account.dollars would raise AttributeError.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using Currency refer to the class defined in section 2 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Read through a decorated getter
# Predict both outputs. Which amount is stored and which is calculated?
# wallet = Currency(12)
# print(wallet.dollars)
# print(wallet._cents)
# ANSWER:


# Exercise 2 — Trace valid, invalid, and zero updates
# Predict all three outputs. Identify when the getter and setter run.
# wallet = Currency(10)
# wallet.dollars = 25
# print(wallet.dollars)
# wallet.dollars = -5
# print(wallet.dollars)
# wallet.dollars = 0
# print(wallet.dollars)
# ANSWER:


# Exercise 3 — Explain the shared name
# Why can both accessor definitions be named dollars in Currency?
# What would happen to the class-body name dollars if the second definition
# had no @dollars.setter decorator?
# Does the parameter new_dollars have to be named dollars? Explain.
# ANSWER:


# Exercise 4 — Find the validation gap
# Compare Currency(-10) with ValidatedCurrency(-10).
# Explain why one stores a negative amount and the other raises ValueError.
# Which assignment in each initializer determines that behavior?
# ANSWER:


# Exercise 5 — Diagnose property mistakes
# Consider each mistake separately and explain the problem:
# A. Calling wallet.dollars() instead of reading wallet.dollars.
# B. Returning self.dollars inside the dollars getter.
# C. Assigning self.dollars inside the dollars setter.
# D. Assigning balance.dollars when balance is a ReadOnlyCurrency instance.
# ANSWER:


# Exercise 6 — Rewrite Height using decorators
# 1. Define Height with __init__(self, feet).
# 2. Store _inches = feet * 12 directly in the initializer.
# 3. Use @property on a feet getter that returns _inches / 12.
# 4. Use @feet.setter on a feet setter that accepts a new value.
# 5. Update _inches only when the new feet value is nonnegative.
# 6. Create an instance, read feet, then try positive and negative updates.
# 7. Explain how this matches the previous lesson's property(...) version.
# Assume ordinary numeric inputs and retain the lesson's silent rejection rule.
# Write your code below:

# ANSWER:


# Optional challenge — One setter for initialization and later updates
# Work through this one together when you are ready.
# Define Temperature with internal _celsius storage and a celsius property.
# Use @property and @celsius.setter for its accessors.
# Reject values below -273.15 with ValueError; otherwise store the new value.
# In __init__, assign through self.celsius so the same validation always runs
# when using the public interface. Assume ordinary numeric inputs.
# Write your code below:


# Uncomment these checks after defining your class:
# temperature = Temperature(20)
# print(temperature.celsius)  # => 20
# temperature.celsius = 0
# print(temperature.celsius)  # => 0
# temperature.celsius = -273.15
# print(temperature.celsius)  # => -273.15
# Try each invalid operation separately and explain the resulting ValueError:
# Temperature(-300)
# temperature.celsius = -300
# Explain why the setter writes _celsius rather than celsius.
