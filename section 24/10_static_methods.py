# Static methods — Study Summary
# Instructor summary:
# - Define a static method by placing @staticmethod above a method definition.
# - Static methods receive neither self nor cls automatically.
# - They receive only the arguments supplied by the caller.
# - Use them for utility operations related to a class that need no instance
#   state or class state to perform their work.
# - Call a static method through either the class or an instance.
# - An instance method can call a static helper through self.helper(arguments).
# - A module-level function is also a valid home for independent helper logic.
# - Keep a helper in a class when that grouping makes its purpose clearer.
#
# Clarifications to the transcript:
# - Calling through an instance does not turn a static method into an instance
#   method. Calling through the class does not turn it into a class method.
# - @staticmethod changes binding: Python does not insert an implicit first
#   argument. It does not enforce purity or prevent changes to mutable inputs.
# - A static method can access objects passed explicitly or names in its scope;
#   it simply receives no automatic instance or class reference.
# - Not using self can suggest a static helper, but does not prove that every
#   such method should be static. The intended interface also matters.
# - Class-body names do not become bare local names inside method bodies.
#   Use self.helper(...) or ClassName.helper(...) to find the helper here.
# - The conversion formula is (fahrenheit - 32) * 5 / 9. Parentheses matter.
# - round(value, 2) rounds a numeric result; it does not format exactly two
#   displayed decimal places. Use formatting such as f"{value:.2f}" for that.
# - Floating-point arithmetic is approximate; these examples assume numeric
#   inputs and use rounding for convenient display of the converted values.


# --- 1. Define an instance method and a static helper ---
class WeatherForecast:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    def in_celsius(self):
        return [
            self.convert_from_fahrenheit_to_celsius(temp)
            for temp in self.temperatures
        ]

    @staticmethod
    def convert_from_fahrenheit_to_celsius(fahrenheit):
        calculation = (fahrenheit - 32) * 5 / 9
        return round(calculation, 2)


forecast = WeatherForecast([100, 90, 80, 70, 60])
print(forecast.in_celsius())  # => [37.78, 32.22, 26.67, 21.11, 15.56]
# in_celsius needs self to read this forecast's temperature list.
# The helper needs only one supplied number, so it has no self or cls parameter.
# The comprehension returns a new list containing each converted temperature.


# --- 2. Call the helper directly through the class ---
print(WeatherForecast.convert_from_fahrenheit_to_celsius(100))  # => 37.78
print(WeatherForecast.convert_from_fahrenheit_to_celsius(32))   # => 0.0
print(WeatherForecast.convert_from_fahrenheit_to_celsius(212))  # => 100.0
# No WeatherForecast instance is needed for a single conversion.
# The caller supplies one argument, and the helper receives that one argument.


# --- 3. Call the same helper through an instance ---
print(forecast.convert_from_fahrenheit_to_celsius(100))  # => 37.78
print(forecast.convert_from_fahrenheit_to_celsius(-40))  # => -40.0
# Even through forecast, Python does not pass forecast into the helper.
# The forecast's stored temperatures have no effect on these direct conversions.
# Keyword arguments work too:
print(forecast.convert_from_fahrenheit_to_celsius(fahrenheit=50))  # => 10.0
# Keep these intentional errors commented out:
# WeatherForecast.convert_from_fahrenheit_to_celsius()
# TypeError: required fahrenheit argument missing.
# forecast.convert_from_fahrenheit_to_celsius(forecast, 100)
# TypeError: too many arguments; do not supply an extra instance manually.


# --- 4. Convert without replacing the stored Fahrenheit list ---
celsius = forecast.in_celsius()
print(forecast.temperatures)  # => [100, 90, 80, 70, 60]
print(celsius is forecast.temperatures)  # => False
# This method calculates a result without assigning to self.temperatures.
# That behavior comes from its implementation, not from @staticmethod alone.

source = [32, 212]
other_forecast = WeatherForecast(source)
print(other_forecast.temperatures is source)  # => True
source.append(50)
print(other_forecast.in_celsius())  # => [0.0, 100.0, 10.0]
# The initializer stores the input list by reference rather than copying it.
# Changing that list later changes the temperatures seen by the instance method.


# --- 5. Compare the three method types ---
class MethodExample:
    def instance_method(self):
        return self

    @classmethod
    def class_method(cls):
        return cls

    @staticmethod
    def static_method(value):
        return value


example = MethodExample()
print(example.instance_method() is example)  # => True
print(MethodExample.class_method() is MethodExample)  # => True
print(example.class_method() is MethodExample)        # => True
print(MethodExample.static_method("hello"))  # => hello
print(example.static_method("hello"))        # => hello
# Normal instance call: Python supplies the instance as self.
# Normal class-method call: Python supplies the receiving class as cls.
# Static-method call: Python supplies no implicit first argument.
# self and cls are conventional parameter names; the decorators determine the
# special binding for class methods and static methods.


# --- 6. Distinguish numeric rounding from display formatting ---
freezing = WeatherForecast.convert_from_fahrenheit_to_celsius(32)
print(freezing)          # => 0.0
print(f"{freezing:.2f}")  # => 0.00
# The first output displays a float. The second creates a formatted string.
# Returning round(calculation, 2) does not force two digits in every printout.


# --- 7. Recognize when a plain function is sufficient ---
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)


print(fahrenheit_to_celsius(100))  # => 37.78
# This function performs the same independent calculation.
# A static method groups the operation under WeatherForecast; a module-level
# function can be convenient when the conversion is useful in unrelated code.
# Neither placement changes the temperature conversion formula.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Exercises using WeatherForecast refer to the class defined in section 1 above.
# Keep intentional-error lines commented out.

# Exercise 1 — Direct conversion
# Predict both outputs. How many arguments does each helper call receive?
# print(WeatherForecast.convert_from_fahrenheit_to_celsius(32))
# print(WeatherForecast.convert_from_fahrenheit_to_celsius(212))
# ANSWER:


# Exercise 2 — Class call versus instance call
# Predict both outputs. Does the stored temperature list affect these calls?
# forecast = WeatherForecast([100, 90])
# print(WeatherForecast.convert_from_fahrenheit_to_celsius(50))
# print(forecast.convert_from_fahrenheit_to_celsius(50))
# ANSWER:


# Exercise 3 — Instance state and a new result list
# Predict both outputs. Does in_celsius replace the original list?
# forecast = WeatherForecast([32, 50, 68])
# print(forecast.in_celsius())
# print(forecast.temperatures)
# Explain why in_celsius needs self but the conversion helper does not.
# ANSWER:


# Exercise 4 — Diagnose a missing decorator
# Explain why the class call succeeds but the instance call raises TypeError.
# class Converter:
#     def double(number):
#         return number * 2
#
# print(Converter.double(5))
# converter = Converter()
# print(converter.double(5))
# Add the decorator that makes both forms work with one explicit argument.
# Keep the failing call commented out until the definition is fixed.
# ANSWER:


# Exercise 5 — Choose a method type
# Choose instance method, class method, or static method for each operation.
# Explain what automatic first argument, if any, the operation needs.
# A. Read a forecast's stored temperatures and return their average.
# B. Construct a new forecast with a predefined temperature list using cls(...).
# C. Convert one caller-supplied Fahrenheit number to Celsius.
# ANSWER:


# Exercise 6 — Write the reverse conversion helper
# 1. Define TemperatureTools.
# 2. Add a static method celsius_to_fahrenheit(celsius).
# 3. Calculate celsius * 9 / 5 + 32 and return the result rounded to two places.
# 4. Call the helper through both the class and an instance.
# 5. Try inputs 0, 100, and -40.
# 6. Explain why the helper needs neither self nor cls.
# Assume numeric inputs; no validation is required.
# Write your code below:

# ANSWER:


# Optional challenge — Combine all three method types
# Work through this one together when you are ready.
# Define TemperatureReport with __init__(self, temperatures) storing a list
# of Fahrenheit temperatures on the instance.
# Add a static method to_celsius(fahrenheit) using the lesson's conversion.
# Add an instance method in_celsius(self) that converts the stored list.
# Add a class method freezing_and_boiling(cls) that returns cls([32, 212]).
# Use self.to_celsius(...) in the instance method and cls(...) in the factory.
# Write your code below:


# Uncomment these checks after defining your class:
# report = TemperatureReport.freezing_and_boiling()
# print(report.temperatures)              # => [32, 212]
# print(report.in_celsius())              # => [0.0, 100.0]
# print(TemperatureReport.to_celsius(50))  # => 10.0
# print(report.to_celsius(50))            # => 10.0
# another = TemperatureReport.freezing_and_boiling()
# print(report is another)  # => False
# print(report.temperatures is another.temperatures)  # => False
# Explain which method receives self, which receives cls, and which receives
# only an explicit temperature argument. Why are the two stored lists separate?
