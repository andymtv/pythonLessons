# Testing the list methods
my_list = [0,1,2,3,4,5,6,7]

# Append - adding elements to the end of the list
my_list.append(8)
print(my_list, '- my list')

# Copy - returns the copy of the specified list
new_list = my_list.copy()
new_list.pop(3) # Modifying the copied list doesn't modify the old list
print(new_list, '- new list - 3 was deleted, but modifying the copied list doesn\'t modify the old list')
print(my_list, '- my list - the number 3 is existing in this list')

# Count - returns the number of the elements with the specified value
my_list.append(8) # Now there are 2 numbers 8
print(f'There are {my_list.count(8)} numbers 8 in my list')

# Extend - adds the specified list elements to the end of the current list
print(new_list, '- new list before extending')
new_list.extend(my_list)
print(new_list, '- new list after extending by my_list')

# Pop - removes the element at the specified position
new_list.pop(-1) # the last element will be removed
print(new_list, '- new list - 8 at the end was removed') # removes 8 at the end

# Remove - removes the first occurrence of the specified value
new_list.remove(0) # the first occurrence of 0 will be removed
print(new_list, '- new list - 0 at the beginning was removed') # removes 0 at the beginning

# Index - returns the position at the first occurrence of the specified value, starts from 0
print(new_list.index(5), 'the number 5 is the 3rd element in the list(starts counting from 0)')

# Reverse - reverses the sorting order of the elements
# we have to call this function first, because this function doesn't produce a value, returns None
# and only change the current list
my_list.reverse()
print(my_list, 'The sorting order of the list was changed') # The sorting order of the list was changed

# Insert - inserts the specified value at the specified position
my_list.insert(5, 12) # First argument - position, second argument - value
print(my_list, '- the number 12 was inserted in my list at the position 5 (starts from 0)')

# Sort - sorts the elements of the list ascending by default, can take the KEY as an argument
my_list.sort()
print(my_list, ' - my list - the number 12 was has been moved from position 5 to the end of the list as the greatest number')
my_list.sort(key = lambda num: num % 2 != 0) # The elements which modulo 2 not equals to 0 will go first
print(my_list, ' - my list - the elements which modulo 2 not equals to 0 will go first')

# Clear - removes all items from the list
my_list.clear()
new_list.clear()
print(my_list, ' - my list - all elements was deleted')
print(new_list, ' - new list - all elements was deleted too')