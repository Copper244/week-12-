# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.


print(groceries[1][2])

groceries = [["apple", "orange," "banana," "coconut"]
            ["celery", "carrots," "potatoes"]
            ["chicken", "fish", "turkey"]]

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()





for collection in groceries:
    for food in collection:
        print(food, end=" ")

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.
print(matrix[0])

# Print the second item from the third list.
print(matrix[2])

# Use a list comprehension to extract the last item from each sub-list.
print(last_items)

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range(1, 11)]
for x in range(1, 11):
    print(x**2)

print(squares)


