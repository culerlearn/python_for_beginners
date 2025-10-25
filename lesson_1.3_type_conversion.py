## Type Conversion

## Implicit conversion happens automatically when Python promotes a lower data type (e.g., int to float).
## Explicit conversion requires functions like int(), float(), str(), and bool().

##################################

## Integer to Float Conversion
# num_int = 10      # Integer
# num_float = 2.5   # Float
# result =  num_int + num_float
#
# print(result)      # Output: 12.5
# print(type(result))  # Output: <class 'float'>
# print(type(num_int))  # Output: <class 'float'>

#############################

# ## Integer to Boolean Conversion
# num = 0
# print(bool(num))  # Output: False
#
# num = 5
# print(bool(num))  # Output: True

#############################

## Converting a Numeric String to an Integer
# num_str = "25"  # This is a string
# num_int = int(num_str)  # Convert to integer
#
# print(num_int)   # Output: 25
# print(type(num_int))  # Output: <class 'int'>
# print(type(num_str))  # Output: <class 'int'>

#############################
## Converting a Numeric String to a Float
# num_str = "12.34"
# num_float = float(num_str)  # Convert to float
#
# print(num_float)   # Output: 12.34
# print(type(num_float))  # Output: <class 'float'>

#############################

## Integer to String
# age = 25
# print(type(age))
# message = "I am " + str(age) + " years old."
#
# print(message)  # Output: I am 25 years old.
#############################

## Converting Strings to Boolean
# print(bool(""))  # Output: False (empty string)
# print(bool("Hello"))  # Output: True

#################################

## Processing User Input
# Converting strings to numbers is useful when working with user input.

# age = input("Enter your age: ")  # 'input' Always returns a string
# age = int(age)  # Convert to integer
# print("Next year, you will be", age + 1)

###########################################

# ## Mathematical Calculations
#
price = 19.99
discount_price = int(price) * 15 # Convert float to integer

print(discount_price)
print(type(discount_price))


##############################

# Implicit conversion happens automatically when Python promotes a lower data type (e.g., int to float).
# Explicit conversion requires functions like int(), float(), str(), and bool().
# Converting strings to numbers is useful when working with user input.
# Converting numbers to strings is necessary for text formatting.
# Boolean conversions help evaluate conditions in Python.