# List Comprehensions
my_list1 = [char for char in 'hello']
my_list3 = [n for n in range(0,11)]
my_list3 = [n*2 for n in range(0,11)]
my_list4 = [n**2 for n in range(0,11)]
my_list5 = [n for n in range(0,11) if n % 2 == 0]
print(my_list5)

# Sets Comprehensions
my_set1 = {char for char in 'hello'}
my_set3 = {n for n in range(0, 11)}
my_set3 = {n * 2 for n in range(0, 11)}
my_set4 = {n ** 2 for n in range(0, 11)}
my_set5 = {n for n in range(0, 11) if n % 2 == 0}
print(my_set5)

# Dictionary Comprehensions

# With created before dict
simple_dict = {'a':1,'b':2,'c':3,'d':4}
my_dict1 = {k:v*2 for k,v in simple_dict.items()}
print(my_dict1)

# Without created before dict
my_dict2 = {k:v*2 for k,v in [('a', 1), ('b', 2)]}
print(my_dict2)

# With optional condition
my_dict3 = {k:v for k,v in simple_dict.items() if v % 2 == 0}
print(my_dict3)

# Use number from a list as a key of the dictionary, and number*2 as a value
numbers1 = [1,2,3,4,5,6,7]
my_dict5 = {v:v*2 for v in numbers1}
print(my_dict5)

# Using list comprehension to create a list with duplicates from another list
number2 = [1, 2, 22, 3, 4, 5, 6, 5, 5, 8, 5, 1]
# Creating a set comprehension from a list to get duplicates and remove all repeated items
# The turn our set to a list
duplicates = list({n for n in number2 if number2.count(n) > 1})
print(duplicates)

my_l = [n*2 for n in range(0,5)]
print(my_l)
my_d = {k:k*2 for k in my_l}
print(my_d)