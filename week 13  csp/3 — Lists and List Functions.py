# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#lists are parts of a collections family in python
#creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list) #[1,2,3,4,5]
print(len(my_list))
print(type(my_list))
print(my_list[0])
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:])
print(my_list[:-2]) # [1, 2, 3, 4]
#reverse my list
print(my_list[::-1])

my_list.append(6)
print(my_list)

my_list.extend([7, 8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list.extend([9, 10])
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

my_list.reverse()
print(my_list) # [7, 6, 5, 4, 3, 2, 1]

my_list.remove(4)
print(my_list) # [7, 6, 5, 2, 1]

my_list.remove(-1)

new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
#my_list.extend(new_list)
#print(my_list)

more_list = list(range(120, 620))
my_list.extend(more_list)
print(len(my_list))
#print every 3rd item in the list
print(my_list[ : : 3])
#remove every 3rd element
del my_list[ : : 3]
print(len(my_list))
print(my_list)

# list functions
# .append() - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removes and returns an item at a given index
#   (default is the last item)
# .remove() - removes the first occurence of a specific value
# .sort - sorts the list in ascemding order
# .reverse()



cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
# access the first item
print(cakes[0])
# access the last item,
print(cakes[-1])
# want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes)

cakes.append('lemon')
print(cakes)
cakes[1] = 'chocolate'
print(cakes)

cakes.pop()
print(cakes)

cakes.insert(2, 'funfetti')
print(cakes)

# Examples:

my_list = ['apple', 'banana', 'cherry']
#print(my_list[0])         # apple
#print(my_list[1:])        # ['banana', 'cherry']

#my_list.append('grape')
#print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
fruits = ["mango", "strawberry", "banana", "apple", "grapes"]
# Print the second and last item.
print(fruits[1])
print(fruits[-1])
# Add a new item using .append().
fruits.append("pineapple")
# Remove the first item using .pop(0).
fruits.pop(0)
# Reverse your list using .reverse().
fruits.reverse()
# Create a list of 3 lists (matrix), and access the middle element.






my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_set.add(6)
print(type(my_set))

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

print(4 in my_set)
print(3 in my_set)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
