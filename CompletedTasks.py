# Task 1 - Create a function that creates a Fibonacci Sequence
def fib_seq(n):
    fib_seq_list = []
    a = 0
    b = 1
    fib_seq_list.append(a)
    fib_seq_list.append(b)
    count = 2
    while count < n:
        c = a + b
        a = b
        b = c
        fib_seq_list.append(c)
        count += 1
    return fib_seq_list

# Task 2 - Return the list with items that are less than 5 from the list
def less_than_5(li):
    new_li = []
    for i in li:
        if i < 5:
            new_li.append(i)
        else:
            continue
    return new_li

task2_list1 = less_than_5(fib_seq(10))
# print(task2_list1)
# Another way to make this is use List Comprehension
task2_list2 = [n for n in fib_seq(10) if n < 5]

# Task 3 - Return the list with items that are existing in both of the list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def comparing_lists1(li1, li2):
    new_li = []
    for item in li1:
        for elem in li2:
            try:
                if item == elem:
                    new_li.append(item)
                else:
                    continue
            except IndexError:
                break
    return new_li


print(comparing_lists1(a, b), ' comparing lists 1') # using loops, the duplicated numbers weren't deleted


def comparing_lists2(li1, li2):
    s1 = set(li1)
    s2 = set(li2)
    new_li = list(s1.intersection(s2))
    return new_li


print(comparing_lists2(a, b), ' comparing lists 2') # [1,2,3,5,8,13] duplicated numbers were deleted

# Comparing lists 3 - using List Comprehension
task3_list = [elem for elem in a if elem in b] # [1,1,2,3,4,5,13]

# Comparing lists 4 - using filter() and lambda


task3_list2 = list(filter(lambda elem: elem in b, a))
print(task3_list2)

# the 'ampersand' (&) symbol and the 'vertical line' (|)symbol are used to do the intersection and the union, respectively
li = list(set(a) & set(b)) # Do the intersection
print(li)


# Task 4 - Sort the values in the dictionary ascending and descending
d = {
    'user_1' : {
        'name' : 'John',
        'surname' : 'Stevenson',
        'age' : 22
    },
    'user_5': {
        'name': 'Robert',
        'surname': 'De Niro',
        'age': 55
    },
    'user_3': {
        'name': 'Sam',
        'surname': 'Galakey',
        'age': 34
    },
    'user_4': {
        'name': 'Rocky',
        'surname': 'Balboa',
        'age': 68
    },
    'user_8': {
        'name': 'Obi',
        'surname': 'Wan',
        'age': 255
    }
}

# With this function you can sort a dictionary by the key or by the value, also you can reverse it if you want
def sorting_dict(dictionary, *args, key=False, value=False, reverse=False):
    """
    Info: In *args pass the string y which you want to sort the list and set value to True
    """
    if key == False and value == True:
        l = sorted(list(dictionary.items()), key=lambda i: i[1][str(*args)], reverse=reverse)
        return dict(l)
    elif key == True and value == False:
        l = sorted(list(dictionary.items()), key=lambda i: i[0], reverse=reverse)
        return dict(l)
    else:
        print('If sort by value, pass value=True as function argument, else pass key=True as function argument')


d1 = sorting_dict(d, key=True, reverse=False)
print(d1)