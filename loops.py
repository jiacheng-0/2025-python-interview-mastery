# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("__________________________________________________")

# Print numbers from 0 to 4
for i in range(5):
    print(i)
print("__________________________________________________")

# Countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1
print("__________________________________________________")

# Create a list of squares
squares = [x**2 for x in range(5)]
print(squares)

print("__________________________________________________")

squares_dict = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Create a set of unique squares
squares_set = {x**2 for x in range(-3, 4)} 
print(squares_set) # Output: {0, 1, 4, 9}

# Create a set of even squares
even_squares_set = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares_set)

# Create a list of squares for even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)


print("__________________________________________________")
print("__________________________________________________")
print("__________________________________________________")
print("__________________________________________________")
print("__________________________________________________")
print("__________________________________________________")
print("__________________________________________________")

