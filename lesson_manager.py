
# Common Data Types in Python: Strings, Integers, Floats, and Booleans
# Str

# text1 = "Hello, Python!"  # Using double quotes
# text2 = 'Python is fun!'  # Using single quotes
#
# text3 = """This is a
# multi-line string."""  # Using triple quotes

# Accessing Characters in a String
# message = "Python"
# print(message[0])  # Output: P
# print(message[4])  # Output: h

# # String Operations
# # Concatenation (joining strings)
# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print(full_name)  # Output: John Doe

#
# # Repeating a string
# repeat_text = "Hello " * 3
# print(repeat_text)  # Output: Hello Hello Hello
#
# # String length
# full_name = "Charles Brown Hesketh"
# print(len(full_name))  # Output: 8

#
# #######
# # Integer (int)
#
# # Creating Integers
# num1 = 10  # Positive integer
# num2 = -5  # Negative integer
# num3 = 0   # Zero

# # Basic Operations with Integers
# a = 15
# b = 4
# #
# print(a + b)  # Addition: Output: 19
# print(a - b)  # Subtraction: Output: 11
# print(a * b)  # Multiplication: Output: 60
# print(a // b)  # Floor division: Output: 3
# print(a % b)  # Modulus (remainder): Output: 3
# print(a ** b)  # Exponentiation: Output: 50625

# # Using Integers in Comparisons
# x = 10
# y = 20
#
# print(x < y)  # Output: True
# print(x == y)  # Output: False
#
#
# # Floats (float)
# # # Creating Floats
# pi = 3.14159  # A floating-point number
# temperature = -12.5  # A negative float
#
# # Basic Operations with Floats
#
# num1 = 7.5
# num2 = 2.5
#
# print(num1 + num2)  # Output: 10.0
# print(num1 - num2)  # Output: 5.0
# print(num1 * num2)  # Output: 18.75
# print(num1 / num2)  # Output: 3.0
#
#
# # Using Floats in Comparisons
# a = 10.5
# b = 10
#
# print(a > b)  # Output: True
# print(a == b)  # Output: False
#
#
# # Converting Between Integers and Floats
# # You can convert an integer to a float and vice versa using float() and int() functions.
#
# x = 10
# y = 3.7
#
# x_float = float(x)  # Convert int to float - 10.0
# y_int = int(y)  # Convert float to int
#
# print(x_float)  # Output: 10.0
# print(y_int)  # Output: 3
#
# # Booleans (bool)
# # A boolean (bool) represents one of two values: True or False. Booleans are often used in conditional statements and logical operations.
#
# Creating Boolean Variables
# is_sunny = True
# is_raining = False

# Boolean Expressions
# Boolean values result from comparison operations.

# a = 10
# b = 20
#
# print(a > b)  # Output: False
# print(a < b)  # Output: True
# print(a == 10)  # Output: True
#
# # Boolean Values of Different Data Types
#

print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(""))  # Output: False (empty string)
print(bool("Hello"))  # Output: True (non-empty string)
print(bool([]))  # Output: False (empty list)
print(bool([1, 2, 3]))  # Output: True (non-empty list)

## End