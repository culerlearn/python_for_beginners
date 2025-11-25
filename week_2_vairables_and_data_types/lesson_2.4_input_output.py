
# Built-in functions for handling input
# And Displaying data on-screen

# Taking User Input with input()

# name = input("Enter your name: ")
# print("Hello,", name)

# Handling Numeric Input
###################################
# age = input("Enter your age: ")
# age = int(age)  # Convert string to integer
# print("Next year, you will be", age + 1)


# Converting Input to a Float
###################################
# height = float(input("Enter your height in meters: "))
# print("Your height is", height, "meters.")

# Displaying Output with print()
###################################
# The print() function is used to display output. It can print strings, numbers, and variables.

# Printing Multiple Values

# name = "Alice"
# age = 25
# location = "London"
# print("Name:", name, "Age:", age, "Location:", location)

# Formatting Output
###################################
# print("Python", "is", "awesome", sep=" ")
# print("dot", "gmail.com", sep="@")

# Using end to Control Line Endings
###################################
# print("Hello", end="\n")
# print("World!")

# Use f strings for print out
# name = "Alice"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
#
# # Use format for output
# template = "My name is {} and I am {} years old."
# print(template.format(name, age))
# print(template.format('dot', 39))

# Taking Multiple Inputs
###################################
#
# name, age = input("Enter your name and age: ").split('@')
# print(f"Name: {name}, Age: {age}")

name, age = input("Enter your name and age separated by a comma: ").split(",")
print(f"Name: {name}, Age: {age}")
