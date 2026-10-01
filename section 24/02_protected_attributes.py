# Protected attributes — Study Summary
# Instructor summary:
# - Encapsulation bundles data with the methods that work on that data.
# - Methods provide a public interface for reading and changing instance state.
# - A method can validate a change before assigning a new attribute value.
# - Ordinary instance attributes can be read and reassigned from outside a class.
# - A single leading underscore marks an attribute as internal by convention.
# - Use public methods to interact with internal state as the class intends.
# - The same underscore convention applies to internal instance methods.
# - Python trusts developers to respect these conventions: "consenting adults."
#
# Clarifications to the transcript:
# - "Protected" here means non-public by convention, not enforced access control.
# - A leading underscore does not prevent reading or assigning an attribute.
# - Public attributes are a normal part of Python interfaces; direct assignment
#   is not inherently wrong. Methods help when an operation needs extra behavior.
# - Encapsulation and strict data hiding are related but distinct ideas.
# - Naming a method public does not automatically add validation or safety.
# - Internal methods remain callable from outside; callers should respect the
#   convention because implementation details may change.
# - A method without an explicit return statement returns None.
# - This lesson uses a float for a simplified firmware version. Real version
#   identifiers are not generally numbers that can be updated by adding one.
# - The server message below is illustrative; the code makes no network request.


# --- 1. Public attributes allow direct access and assignment ---
class PublicSmartPhone:
    def __init__(self):
        self.company = "Apple"
        self.firmware = 10.0


public_phone = PublicSmartPhone()
print(public_phone.company)   # => Apple
print(public_phone.firmware)  # => 10.0

public_phone.company = "Samsung"
public_phone.firmware = "nonsense"
print(public_phone.company)   # => Samsung
print(public_phone.firmware)  # => nonsense
# This class performs no validation. Assignment can replace a number with text.
# Later code expecting a numeric firmware value could fail as a result.


# --- 2. Mark internal state and provide a public interface ---
class SmartPhone:
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version.")
        self._firmware += 1


iphone = SmartPhone()
print(iphone.get_os_version())  # => 10.0
# _company and _firmware signal internal implementation details.
# get_os_version and update_firmware are public methods with no leading underscore.
# Inside the class, self._firmware reads or changes the receiving instance's state.


# --- 3. Update state through a public method ---
result = iphone.update_firmware()
# => Reaching out to the server for the next version.
print(result)                   # => None
print(iphone.get_os_version())   # => 11.0
# The method prints a message and changes state, but does not return the version.
# get_os_version returns the version; print displays that returned value.
# A real update method could check compatibility before changing internal state.


# --- 4. An underscore is a convention, not a lock ---
example_phone = SmartPhone()
print(example_phone._company)   # => Apple
print(example_phone._firmware)  # => 10.0

example_phone._firmware = 12.0
print(example_phone.get_os_version())  # => 12.0
# These direct accesses work, but deliberately bypass the intended interface.
# Use them here to understand the convention, not as the normal usage pattern.
# Keep this misuse commented out:
# example_phone._firmware = "nonsense"
# example_phone.update_firmware()  # TypeError when adding 1 to a string.
# The underscore alone neither validates values nor makes them read-only.
# company and _company are different names. With SmartPhone as defined above,
# reading example_phone.company would raise AttributeError.


# --- 5. Internal methods follow the same naming convention ---
class SmartPhoneWithHelper:
    def __init__(self):
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def _get_next_version(self):
        return self._firmware + 1

    def update_firmware(self):
        self._firmware = self._get_next_version()


helper_phone = SmartPhoneWithHelper()
helper_phone.update_firmware()
print(helper_phone.get_os_version())  # => 11.0
# update_firmware calls the internal helper through self.
# External callers should use update_firmware rather than _get_next_version.
# Calling helper_phone._get_next_version() is technically possible, but the
# helper is an implementation detail and is not promised as a public interface.


# --- 6. Each instance keeps its own firmware state ---
first = SmartPhone()
second = SmartPhone()
first.update_firmware()
# => Reaching out to the server for the next version.
print(first.get_os_version())   # => 11.0
print(second.get_os_version())  # => 10.0
# self refers to first during this update, so second's attribute is unchanged.
# The underscore does not determine whether state is shared between instances.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using SmartPhone refer to the class defined in section 2 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Identify the public interface
# Which names indicate internal details, and which are intended for callers?
# _company, _firmware, get_os_version, update_firmware, _get_next_version
# Does Python prevent callers from accessing any of the underscored names?
# ANSWER:


# Exercise 2 — Trace an update and its return value
# Predict the entire output, including the message printed inside the method.
# phone = SmartPhone()
# result = phone.update_firmware()
# print(result)
# print(phone.get_os_version())
# ANSWER:


# Exercise 3 — Bypass the convention
# Predict both outputs. Explain why the assignment is allowed and why callers
# should still use the public interface in ordinary code.
# phone = SmartPhone()
# phone._firmware = 25.0
# print(phone._firmware)
# print(phone.get_os_version())
# ANSWER:


# Exercise 4 — Separate instances
# Predict both versions and the number of server messages printed.
# first = SmartPhone()
# second = SmartPhone()
# first.update_firmware()
# first.update_firmware()
# print(first.get_os_version())
# print(second.get_os_version())
# ANSWER:


# Exercise 5 — Diagnose invalid internal state
# Explain which statement would fail and why. Does a leading underscore
# prevent an invalid value from being assigned?
# phone = SmartPhone()
# phone._firmware = "broken"
# phone.update_firmware()
# Keep the failing call commented out.
# ANSWER:


# Exercise 6 — Write your own public interface
# 1. Define MusicPlayer with __init__(self, volume=5).
# 2. Store volume in an internal attribute named _volume.
# 3. Define get_volume(self) to return the current volume.
# 4. Define increase_volume(self) to increase _volume by one.
# 5. Create two players and increase only the first player's volume.
# 6. Print both volumes through get_volume and explain their different values.
# 7. Explain why callers should avoid assigning to _volume directly.
# No volume limits or input validation are required for this exercise.
# Write your code below:

# ANSWER:


# Optional challenge — Validate a change through a public method
# Work through this one together when you are ready.
# Define VolumeControl with an initial _volume of 5 and a get_volume method.
# Add set_volume(self, value). Assume value is an integer.
# Accept values from 0 through 10, updating _volume and returning True.
# For values outside that range, leave _volume unchanged and return False.
# Write your code below:


# Uncomment these checks after defining your class:
# control = VolumeControl()
# print(control.get_volume())  # => 5
# print(control.set_volume(8)) # => True
# print(control.get_volume())  # => 8
# print(control.set_volume(20)) # => False
# print(control.get_volume())   # => 8
# Explain why the validation works only when callers use set_volume.
# Could a caller still write control._volume = 20? Why?
