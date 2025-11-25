
# How to use the input() function to get user input
# How to use the print() function to display output

##################################
# The input() function allows a program to receive user input as a string.
#
# Basic Usage of input()
# name = input("Enter your name: ")
# print("Hello,", name)
#
# How It Works:
# The input() function displays the prompt ("Enter your name: ").
# The user enters a value and presses Enter.
# The entered value is stored in the variable name as a string.
# The print() function displays a greeting using the input value.

####################################
# Printing Multiple Values
# You can print multiple values by separating them with commas (,).
#
# name = "Alice"
# age = 25.5
# print("Name:", name, "Age:", age)
# print(type(age))
#
# #######################
#
# Formatting Output
# 1. Using sep to Customize Separators
# By default, print() separates values with a space. You can change this using sep.
#
# print("Python", "is", "awesome", sep="-")
#
# ###########################
#
# Using end to Control Line Endings
# By default, print() adds a newline (\n) at the end. You can change this using end.
#
# print("Hello", end=" ")
# print("World!")
#
# #########################################
#
#  Using f-strings for Formatted Output
# F-strings (f"") allow inserting variables directly into strings.
#
# name = "Alice"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
#
# ########################################
#
#  Using .format() for Formatted Output
# The .format() method is an alternative to f-strings.
#
# name = "Alice"
# age = 25
# print("My name is {} and I am {} years old.".format(name, age))
#
# #########################################
#
# Taking Multiple Inputs
# You can take multiple inputs in a single line using .split().
#
# name, age, address = input("Enter your name and age: ").split("/")
# print(f"Name: {name}, Age: {age}, lives at {address}")

########################################

# Summary

# input() is used to get user input. By default, it returns a string.
# Convert input using int(), float() when working with numbers.
# print() displays output and supports multiple values.
# Use sep and end to customise print behaviour.
# Use f-strings (f"") or .format() for formatted output.
# .split() allows multiple inputs on a single line.