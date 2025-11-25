Introduction

A list is a fundamental data structure in Python that allows storing multiple values in a single variable.

Lists are widely used due to their flexibility and efficiency in handling sequences of data. They can hold elements of different data types, including numbers, strings, and even other lists.

Key Characteristics of Lists:
Ordered – Lists maintain the order of elements, meaning elements are stored in the order they were inserted.
Mutable – Unlike tuples, lists can be modified after creation by adding, updating, or removing elements.
Dynamic – The size of a list is not fixed; elements can be added or removed dynamically.
Indexed – Elements in a list can be accessed using their position (index).
Heterogeneous – Lists can store multiple data types in a single collection.

In this section, we will explore:

How to create lists in Python.
How to access elements using indexing and slicing.
How to modify lists by adding, removing, and updating elements.
How to use common list operations such as concatenation, repetition, and iteration.

By the end of this section, you will be able to create, manipulate, and efficiently work with lists in Python.

6.1.1 Creating a List

Lists are created using square brackets [ ], with elements separated by commas.

Syntax:
list_name = [element1, element2, element3, ...]

Example: Creating Different Types of Lists
# List of integers
numbers = [10, 20, 30, 40, 50]

# List of strings
fruits = ["apple", "banana", "cherry"]

# List with mixed data types
mixed_list = [42, "hello", 3.14, False]

# Empty list
empty_list = []

# Nested list (a list within a list)
nested_list = [[1, 2, 3], ["A", "B", "C"], [True, False]]

print(numbers)       # Output: [10, 20, 30, 40, 50]
print(mixed_list)    # Output: [42, 'hello', 3.14, False]
print(nested_list)   # Output: [[1, 2, 3], ['A', 'B', 'C'], [True, False]]

6.1.2 Accessing Elements in a List

Since lists are ordered, elements can be accessed using their index positions. Python uses zero-based indexing (as most other programming languages), meaning that the first element is at index 0, the second at index 1, and so on.

Example: Accessing Elements Using Indexing
fruits = ["apple", "banana", "cherry"]

# Accessing elements by positive index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

Negative Indexing

Python allows negative indexing, where -1 refers to the last element, -2 to the second-last, and so on.

print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

6.1.3 Slicing a List

Slicing allows extracting a subset of elements from a list. The general syntax for slicing is:

list[start:stop:step]

start: The index where slicing begins (inclusive).
stop: The index where slicing stops (exclusive).
step: (Optional) The interval between elements.
Example: List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[1:4])   # Output: [20, 30, 40] (from index 1 to 3)
print(numbers[:3])    # Output: [10, 20, 30] (first three elements)
print(numbers[3:])    # Output: [40, 50, 60, 70] (from index 3 to end)
print(numbers[::2])   # Output: [10, 30, 50, 70] (every second element)
print(numbers[::-1])  # Output: [70, 60, 50, 40, 30, 20, 10] (reversed)

6.1.4 Modifying a List

Lists are mutable, meaning they can change, and thus, elements can be modified after creation.

Example: Updating Elements in a List
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"

print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

6.1.5 Adding Elements to a List

Python provides several methods to add elements to a list. We revert to the contents of a list as "elements":

append() – Adds an element to the end of the list.
insert() – Inserts an element at a specific index.
extend() – Adds multiple elements from another list.
# Append method
fruits.append("mango")

# Insert method
fruits.insert(1, "grape")

# Extend method
fruits.extend(["pear", "orange"])

print(fruits)  
# Output: ['apple', 'grape', 'blueberry', 'cherry', 'mango', 'pear', 'orange']


Summary

Here is a summary of what we have covered in this section

Lists allow storing multiple elements and support various operations like indexing, slicing, and modification.
Lists are mutable, meaning they can be modified after creation.
Python provides multiple methods like append(), insert(), and remove() to manipulate lists efficiently.
What’s Next?

In the next section, 6.2 Tuples: Immutable Collections, we will explore a similar data structure that differs in its immutability.


# Tuples

Introduction

A tuple is a built-in data structure in Python used to store multiple items in a single variable.

Unlike lists, tuples are immutable, meaning their elements cannot be modified after creation. Tuples are commonly used when data must remain unchanged throughout the execution of a program.

Key Characteristics of Tuples:
Ordered – Tuples maintain the order of elements.
Immutable – Once a tuple is created, its elements cannot be changed, added, or removed.
Indexed – Elements can be accessed using their position (index).
Heterogeneous – Tuples can contain different data types, including numbers, strings, and even other tuples.
More Memory Efficient – Tuples use less memory compared to lists, making them a better choice for storing constant data.

In this section, we will explore:

How to create tuples in Python.
How to access elements using indexing and slicing.
How to perform basic operations on tuples.
When to use tuples instead of lists.

By the end of this section, you will understand how tuples work and when to use them in Python programming.

6.2.1 Creating a Tuple

A tuple is defined using parentheses ( ), with elements separated by commas.

Syntax:
tuple_name = (element1, element2, element3, ...)

Example: Creating Different Types of Tuples
# Tuple of integers
numbers = (10, 20, 30, 40, 50)

# Tuple of strings
fruits = ("apple", "banana", "cherry")

# Tuple with mixed data types
mixed_tuple = (42, "hello", 3.14, False)

# Empty tuple
empty_tuple = ()

# Nested tuple (tuple within a tuple)
nested_tuple = ((1, 2, 3), ("A", "B", "C"), (True, False))

print(numbers)       # Output: (10, 20, 30, 40, 50)
print(mixed_tuple)   # Output: (42, 'hello', 3.14, False)
print(nested_tuple)  # Output: ((1, 2, 3), ('A', 'B', 'C'), (True, False))

6.2.2 Creating a Tuple with One Element

When defining a tuple with a single element, a trailing comma is required.

single_element_tuple = (42,)  # Correct way to define a single-element tuple
print(type(single_element_tuple))  # Output: <class 'tuple'>

not_a_tuple = (42)  # This is NOT a tuple; it is an integer
print(type(not_a_tuple))  # Output: <class 'int'>

6.2.3 Accessing Elements in a Tuple

Tuples are indexed, meaning elements can be accessed using their position.

Example: Accessing Elements Using Indexing
fruits = ("apple", "banana", "cherry")

# Accessing elements by positive index
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

Negative Indexing

Negative indexing allows accessing elements from the end of the tuple.

print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana

6.2.4 Slicing a Tuple

Tuples support slicing, allowing extraction of a subset of elements.

Example: Tuple Slicing
numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[1:4])   # Output: (20, 30, 40) (from index 1 to 3)
print(numbers[:3])    # Output: (10, 20, 30) (first three elements)
print(numbers[3:])    # Output: (40, 50, 60, 70) (from index 3 to end)
print(numbers[::2])   # Output: (10, 30, 50, 70) (every second element)
print(numbers[::-1])  # Output: (70, 60, 50, 40, 30, 20, 10) (reversed)

6.2.5 Tuple Immutability

Tuples are immutable, meaning elements cannot be modified after creation.

Example: Attempting to Modify a Tuple
fruits = ("apple", "banana", "cherry")

# Attempting to change an element (this will raise an error)
fruits[1] = "blueberry"  # TypeError: 'tuple' object does not support item assignment


Since tuples cannot be changed, the only way to modify them is by creating a new tuple.

fruits = ("apple", "banana", "cherry")
new_fruits = fruits[:1] + ("blueberry",) + fruits[2:]

print(new_fruits)  # Output: ('apple', 'blueberry', 'cherry')

6.2.6 Tuple Operations
Concatenation

Tuples can be combined using the + operator.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

Repetition

The * operator repeats the tuple.

numbers = (1, 2, 3)
repeated_tuple = numbers * 3

print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


What’s Next?

In the next section, 6.3 Dictionaries: Key-Value Pairs, we will explore another important data structure that allows storing data in a key-value format.



####### Dictionaries

A dictionary in Python is a powerful data structure that allows you to store key-value pairs. Unlike lists and tuples, which use numeric indexing, dictionaries use unique keys to access values, making them fast and efficient for data lookups.

In this section, we will explore:

How to create dictionaries
How to access, modify, and delete key-value pairs
Dictionary operations and methods
Use cases for dictionaries
6.3.1 Creating Dictionaries

A dictionary is created using curly braces {}, with each key-value pair separated by a colon (:).

Example: Creating a Dictionary
# Defining a dictionary with student details
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print(student)


Key Points:

Keys must be unique and immutable (strings, numbers, or tuples).
Values can be any data type, including lists or other dictionaries.
Creating an Empty Dictionary
empty_dict = {}  # Empty dictionary

Using dict() Constructor
person = dict(name="John", age=25, city="New York")
print(person)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}

6.3.2 Accessing Values in a Dictionary

You can retrieve values using keys inside square brackets [] or with the .get() method.

Accessing a Value Using a Key
student = {"name": "Alice", "age": 20, "grade": "A"}

print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20


Important: If the key doesn’t exist, using [] will raise a KeyError.

Using .get() Method
print(student.get("name"))  # "Not Found"))  # Output: Not Found


Advantage: .get() prevents errors by allowing a default value when the key is missing.

6.3.3 Modifying Dictionaries

Dictionaries are mutable, meaning you can update existing values or add new key-value pairs.

Updating an Existing Value
student["age"] = 21
print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

Adding a New Key-Value Pair
student["city"] = "New York"
print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A', 'city': 'New York'}

Updating Multiple Keys Using .update()
student.update({"age": 22, "grade": "A+"})
print(student)  # Output: {'name': 'Alice', 'age': 22, 'grade': 'A+', 'city': 'New York'}

6.3.4 Removing Items from a Dictionary

You can remove dictionary entries using del, pop(), or popitem().

Using del to Remove a Specific Key
del student["city"]
print(student)  # Output: {'name': 'Alice', 'age': 22, 'grade': 'A+'}

Using .pop() to Remove and Return a Value
grade = student.pop("grade")
print(grade)  # Output: A+
print(student)  # Output: {'name': 'Alice', 'age': 22}

Using .popitem() to Remove the Last Inserted Item
student["city"] = "London"
removed_item = student.popitem()
print(removed_item)  # Output: ('city', 'London')

Clearing a Dictionary
student.clear()
print(student)  # Output: {}

6.3.5 Looping Through a Dictionary

You can iterate over a dictionary using for loops.

Looping Through Keys
person = {"name": "John", "age": 25, "city": "New York"}

for key in person:
    print(key)


Output:

name
age
city

Looping Through Values
for value in person.values():
    print(value)


Output:

John
25
New York

Looping Through Key-Value Pairs
for key, value in person.items():
    print(f"{key}: {value}")


Output:

name: John
age: 25
city: New York

6.3.6 Dictionary Methods
Method	Description	Example
.keys()	Returns a list of keys	person.keys() → dict_keys(['name', 'age', 'city'])
.values()	Returns a list of values	person.values() → dict_values(['John', 25, 'New York'])
.items()	Returns key-value pairs as tuples	person.items() → dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])
.update()	Updates dictionary with another dictionary	person.update({"age": 26})
.pop(key)	Removes a key and returns its value	person.pop("age")
.popitem()	Removes the last added key-value pair	person.popitem()
.clear()	Removes all items	person.clear()
6.3.7 Nested Dictionaries

A nested dictionary contains dictionaries within dictionaries.

Example: Storing Multiple Students' Data
students = {
    "student1": {"name": "Alice", "age": 20, "grade": "A"},
    "student2": {"name": "Bob", "age": 22, "grade": "B"}
}

print(students["student1"]["name"])  # Output: Alice

6.3.8 When to Use Dictionaries
Feature	Dictionary	List
Key-Value Access	Fast	Slow (requires searching)
Ordering	Ordered (Python 3.7+)	Ordered
Mutability	Mutable	Mutable
Use Case	Data with named attributes	Sequential data
Example Use Cases
Storing user profiles ({"username": "Alice", "email": "alice@email.com"})
Counting word occurrences ({"hello": 3, "world": 2})
Database-like records ({"product1": {"name": "Laptop", "price": 1000}})
Summary

Here is a summary of what we have covered in this section

A dictionary stores key-value pairs, where keys must be unique.
Keys are used to access, modify, and delete values.
Dictionaries support looping, updating, and removal operations.
Nested dictionaries allow storing complex data.
Dictionaries are ideal for structured data and fast lookups.