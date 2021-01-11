# A function that returns a list with only unique values
# Using Set
# Warning!!!
# This function working only with IMMUTABLE VALUES and DATA TYPES

def make_uniq_list_set(your_list):
    my_set = set(your_list)
    uniq_list = list(my_set)
    return uniq_list

# The end of the first function

# A function that returns a list with only unique values
# Using While Loop
# Warning!!! This function working with everything
def make_uniq_list_while_loop(your_list):
    i = 0
    uniq_list = []
    while (i < len(your_list)):
        if (your_list[i] not in uniq_list):
            uniq_list.append(your_list[i])
            i += 1
        else:
            i += 1
    return uniq_list


# Using FOr Loop
# Warning!!! This function working with everything
# The end of the second function

def make_uniq_list_for_loop(your_list):
    uniq_list = []
    for item in your_list:
        if (item not in uniq_list):
            uniq_list.append(item)
        else:
            continue
    return uniq_list


my_list = [1, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5]
my_list2 = [['abra', 'a', 'b', 'd', 'd', 'c', 'abra'], ['abra', 'a', 'b', 'd', 'd', 'c', 'abra'], None, None,
            {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, 'abra', 'a', 'b', 'd', 'd', 'c', 'abra']

print(make_uniq_list_set(my_list))
print(make_uniq_list_while_loop(my_list2))
print(make_uniq_list_for_loop(my_list2))


# Function which finds and prints duplicates from a list

def find_and_print_duplicates(your_list):
    uniq_list = []
    duplicates_list = []
    for item in your_list:
        if (item not in uniq_list):
            uniq_list.append(item)
        else:
            duplicates_list.append(item)
    print('The duplicates are: ' + str(duplicates_list))
    return duplicates_list


find_and_print_duplicates(my_list)

