'''
https://chat.deepseek.com/a/chat/s/57d74b0c-c478-456f-80ba-422f131ba515
'''

# Integer example
age = 25
print("Age:", age)
print("Type of age:", type(age))
print("__________________________________________________")

print(int('35')) # Converts string "35" to integer 35
print(abs(-10))  # Output: 10
print(round(3.6))  # Output: 4
print(divmod(10, 3))  # Output: (3, 1)

print("__________________________________________________")

# Float example
height = 5.9
print("Height:", height)
print("Type of height:", type(height))

num = float("3.14")  # Converts string "3.14" to float 3.14
print(round(3.14159, 2))  # Output: 3.14

import math
print(math.floor(3.7))  # Output: 3
print(math.ceil(3.2))   # Output: 4

print("__________________________________________________")

# String example
name = "Alice"
print("Name:", name)
print("Type of name:", type(name)) 
print("_______________________")
text = str(42)  # Converts integer 42 to string "42"
print(len("hello"))  # Output: 5
print("hello world".split())  # Output: ['hello', 'world']
print(", ".join(["apple", "banana", "cherry"]))  # Output: "apple, banana, cherry"
print("  hello  ".strip())  # Output: "hello"
print("hello world".replace("world", "Python"))  # Output: "hello Python"
print("hello world".find("world"))  # Output: 6
print("Hello".upper())  # Output: "HELLO"
print("Hello".lower())  # Output: "hello"

print("__________________________________________________")

# List example
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("Type of fruits:", type(fruits)) # Output: <class 'list'>
print("________________________")

# Accessing elements
print("First fruit:", fruits[0]) # Output: apple
print("________________________")

# Modifying list
fruits.append("orange")   
print("Updated fruits:", fruits) # Output: ['apple', 'banana', 'cherry', 'orange']

print("__________________________________________________")

my_list = list("hello")  # Output: ['h', 'e', 'l', 'l', 'o']

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

fruits.extend(["orange", "mango"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'mango']

fruits.insert(1, "kiwi")
print(fruits)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange', 'mango']

fruits.remove("banana")
print(fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange', 'mango']

print(fruits.pop(1))  # Output: 'kiwi'
print(fruits)  # Output: ['apple', 'cherry', 'orange', 'mango']

print(fruits.index("cherry"))  # Output: 1

fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'mango', 'orange']

fruits.reverse()
print(fruits)  # Output: ['orange', 'mango', 'cherry', 'apple']

print(fruits.pop()) # Output: 'apple', default index is -1

print("__________________________________________________")

# Tuple example
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print("Type of coordinates:", type(coordinates)) # Output: <class 'tuple'>

# Accessing elements
print("X coordinate:", coordinates[0])

# Tuples are immutable, so this will raise an error:
# coordinates[0] = 15.0

print("__________________________________________________")
my_tuple = tuple([1, 2, 3])  # Output: (1, 2, 3)
print((1, 2, 2, 3).count(2))  # Output: 2
print((1, 2, 3).index(2))  # Output: 1

print("__________________________________________________")

# Set example
unique_numbers = {1, 2, 3, 4, 3, 2}
print("Unique numbers:", unique_numbers)
print("Type of unique_numbers:", type(unique_numbers))

# Adding elements
unique_numbers.add(5)
print("Updated unique numbers:", unique_numbers)

# Sets automatically remove duplicates
unique_numbers.add(3)
print("After adding duplicate:", unique_numbers)

my_set = set([1, 2, 2, 3])  # Output: {1, 2, 3}

my_set.add(4) # Output: {1, 2, 3, 4}

# remove(): Removes an element from the set (raises an error if not found).
my_set.remove(2) # Output: {1, 3, 4}

# discard(): Removes an element if it exists (no error if not found).
my_set.discard(5)  # No error

# union(): Returns the union of two sets.
print({1, 2}.union({2, 3}))  # Output: {1, 2, 3}

# intersection(): Returns the intersection of two sets.
print({1, 2}.intersection({2, 3}))  # Output: {2}

print("__________________________________________________")

# Dictionary example
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Person:", person)
print("Type of person:", type(person))

# Accessing values
print("Name:", person["name"])

# Modifying dictionary
person["age"] = 31
print("Updated person:", person)

# Adding new key-value pair
person["email"] = "john@example.com"
print("Person with email:", person)

print("__________________________________________________")

my_dict = dict(name="John", age=30)  # Output: {'name': 'John', 'age': 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
print(my_dict.values())  # Output: dict_values(['John', 30])

# items(): Returns key-value pairs as tuples.
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)])

# get(): Returns the value for a key (returns None or a default value if the key doesn't exist).
print(my_dict.get("name"))  # Output: 'John'
print(my_dict.get("city", "Unknown"))  # Output: 'Unknown'
print(my_dict["city"]) # Raises an error

# update(): Updates the dictionary with another dictionary or iterable.
my_dict.update({"city": "New York"})
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# pop(): Removes and returns the value for a key.
print(my_dict.pop("age"))  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

print("__________________________________________________")
