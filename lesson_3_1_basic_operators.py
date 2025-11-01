
# Arithmetic Operators
# Arithmetic operators in Python are used to perform mathematical operations on numbers.
# It is common for programming languages to provide data types for storing numbers since this is needed to compute math. The same thing applies to the Python language. Python supports the following arithmetic operators:

# +	Addition	5 + 3 = 8
# -	Subtraction	10 - 4 = 6
# *	Multiplication	6 * 2 = 12
# /	Division (floating-point)	7 / 2 = 3.5
# %	Modulus (remainder)	7 % 2 = 1
# //	Floor division	7 // 2 = 3
# **	Exponentiation (power)	2 ** 3 = 8

# These operators allow mathematical operations in Python
# and are commonly used in various applications, including data processing,
# calculations, and programming logic.


############
# Multiplication (*)
# p = 7
# q = 3
# product = p * q
# print("Product:", product)
#
#
# # Division (/)
# m = 10
# n = 4
# division = m / n
# print("Division:", division)

# Modulus (%)
# The % operator returns the remainder when one number is divided by another.
# This is useful for checking divisibility and working with even/odd numbers.

# num1 = 17
# num2 = 5
# remainder = num1 % num2
# print("Remainder:", remainder)

# Floor Division (//)
# The // operator performs integer (floor) division,
# which discards the decimal part and returns only the whole number.

# num1 = 17
# num2 = 5
# floor_division = num1 // num2
# print("Floor Division:", floor_division)

# Exponentiation (**)
# The ** operator raises a number to the power of another number.

# base = 2
# exponent = 3
# power_result = base ** exponent
# print("Exponentiation:", power_result)
#
# Operator Precedence
# ** (Exponentiation)
# *, /, //, % (Multiplication, Division, Floor Division, Modulus)
# +, - (Addition, Subtraction)

# result = 2 + 3 * 4 ** 2 // 5 - 1
# print("Result:", result)

4 ** 2 = 16
3 * 16 = 48
48 // 5 = 9
2 + 9 = 11
11 - 1 = 10
# Summary

# Python provides seven arithmetic operators: +, -, *, /, %, //, and **.
# + adds, - subtracts, * multiplies, and / performs floating-point division.
# % returns the remainder, // performs floor division, and ** calculates exponents.
# Python follows operator precedence, where exponentiation has the highest precedence.


# Comparison Operators
# Introduction
# Comparison operators in Python are used to compare values and return a Boolean result (True or False).
# These operators are essential for making decisions in programming, such as in conditional statements (if statements) and loops.

# Python provides six comparison operators:

# Operator	Description	Example
# ==	Equal to	5 == 5 → True
# !=	Not equal to	5 != 3 → True
# <	Less than	3 < 7 → True
# >	Greater than	10 > 6 → True
# <=	Less than or equal to	4 <= 4 → True
# >=	Greater than or equal to	9 >= 2 → True


# Equal to (==)
# The == operator checks if two values are equal. It returns True if the values are the same and False otherwise.


x = 10
y = 10
print(x == y)  # Output: True

a = 5
b = 7
print(a == b)  # Output: False


# Not Equal to (!=)
# The != operator checks if two values are not equal. It returns True if the values are different and False if they are the same.


x = 5
y = 10
print(x != y)  # Output: True

a = 8
b = 8
print(a != b)  # Output: False


# Less than (<)
# The < operator checks if the left operand is less than the right operand.


x = 3
y = 7
print(x < y)  # Output: True

a = 10
b = 4
print(a < b)  # Output: False
#  Greater than (>)
# The > operator checks if the left operand is greater than the right operand.

x = 9
y = 2
print(x > y)  # Output: True

a = 5
b = 10
print(a > b)  # Output: False

# Less than or Equal to (<=)
# The <= operator checks if the left operand is less than or equal to the right operand.

x = 5
y = 5
print(x <= y)  # Output: True

a = 3
b = 8
print(a <= b)  # Output: True

p = 12
q = 6
print(p <= q)  # Output: False

# Greater than or Equal to (>=)
# The >= operator checks if the left operand is greater than or equal to the right operand.


x = 6
y = 6
print(x >= y)  # Output: True

a = 15
b = 9
print(a >= b)  # Output: True

p = 2
q = 5
print(p >= q)  # Output: False


# Using Comparison Operators in Conditional Statements
# Comparison operators are frequently used in if statements to make decisions.

# E.g. Checking Age Eligibility
# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# Summary

# Comparison operators (==, !=, <, >, <=, >=) return True or False based on the comparison between values.
# These operators are widely used in conditional statements and loops.
# Comparison operators help determine conditions such as age restrictions, eligibility, and value comparisons.
# What’s Next?
#
# Logical Operators
# Logical operators in Python are used to combine multiple Boolean expressions (conditions) and return a True or False value.
# These operators are essential for making complex decisions in programming, especially in if statements and loops.


# 3 logical operators:

# and	Returns True if both conditions are True	(5 > 3) and (10 > 5) → True
# or	Returns True if at least one condition is True	(5 > 3) or (10 < 5) → True
# not	Reverses the Boolean value of an expression	not(5 > 3) → False
# These operators allow for more flexible and efficient decision-making in programs.


# The and Operator
# The and operator returns True only if both conditions are True. If either condition is False, the result is False.

age = 25
has_id = True

if age >= 18 and has_id:
    print("You are allowed to enter.")
else:
    print("Access denied.")


You are allowed to enter.
The condition age >= 18 is True
The condition has_id is True
Since both conditions are True, the overall expression evaluates to True.
Example 2: Evaluating and Expressions
print(True and True)   # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False) # Output: False
3.3.2 The or Operator
The or operator returns True if at least one condition is True. It only returns False when both conditions are False.

Example 1: Using or in a Conditional Statement
has_ticket = False
is_vip = True

if has_ticket or is_vip:
    print("You can enter the event.")
else:
    print("Access denied.")
Output:

You can enter the event.
The condition has_ticket is False, but is_vip is True.
Since at least one condition is True, the overall expression evaluates to True.
Example 2: Evaluating or Expressions
print(True or True)   # Output: True
print(True or False)  # Output: True
print(False or True)  # Output: True
print(False or False) # Output: False
3.3.3 The not Operator
The not operator reverses the Boolean value of an expression.

Example 1: Using not in a Conditional Statement
is_raining = False

if not is_raining:
    print("You can go outside without an umbrella.")
else:
    print("Take an umbrella with you.")
Output:

You can go outside without an umbrella.
The condition is_raining is False.
not False becomes True, so the if condition is executed.
Example 2: Evaluating not Expressions
print(not True)   # Output: False
print(not False)  # Output: True
3.3.4 Combining Logical Operators
Logical operators can be combined to create complex conditions.

Example: Checking Multiple Conditions
age = 20
has_id = True
has_permission = False

if (age >= 18 and has_id) or has_permission:
    print("You are allowed.")
else:
    print("Access denied.")
Output:

You are allowed.
The condition (age >= 18 and has_id) is True.
The condition has_permission is False.
Since at least one condition is True in the or statement, the overall condition evaluates to True.
Summary
This section has covered the following topics

The and operator requires both conditions to be True.
The or operator requires at least one condition to be True.
The not operator reverses a Boolean value.
Logical operators help build complex conditions for decision-making.
What’s Next?
In the next lesson, 3.4 Combining Operators and Expressions, we will explore how arithmetic, comparison, and logical operators work together to create more advanced expressions.

Empty material!