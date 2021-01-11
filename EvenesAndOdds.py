# How to loop on matrix
image = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1]
]

fill = '$'
empty = ' '
for row in image:
    for pixel in row:
        pixel = empty if pixel == 1 else fill
        print(pixel, sep='', end=' ')
    print('')

# How enumerate() function works
simple_tuple = ('a', 'b', 'c', 'd', 'e')
for index, item in enumerate(simple_tuple):
    print(index, item)


# Function which returns the highest even number manually!
def highest_even_manually(li):
    evens = []
    for num in li:
        if (num % 2 == 0 and num not in evens):
            evens.append(num)
            for i in evens:
                for a in evens:
                    if (a > i):
                        evens.clear()
                        evens.append(a)
    return evens[0]


# Function which returns the highest even number using max() function
def highest_even_max(li):
    evens = []
    for num in li:
        if (num % 2 == 0 and num not in evens):
            evens.append(num)
    return max(evens)


user_li = [22, 14, 81, 96, 96, 24, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
print(highest_even_manually(user_li))
print(highest_even_max(user_li))


# Function which returns the highest odd number manually!
def highest_odd_manually(li):
    odd = []
    for num in li:
        if (num % 2 != 0 and num not in odd):
            odd.append(num)
            for i in odd:
                for a in odd:
                    if (a > i):
                        odd.clear()
                        odd.append(a)
    return odd[0]


# Function which returns the highest odd number using max() function
def highest_odd_max(li):
    odd = []
    for num in li:
        if (num % 2 != 0 and num not in odd):
            odd.append(num)
    return max(odd)


user_li = [22, 14, 81, 96, 96, 24, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
print(highest_odd_manually(user_li))
print(highest_odd_max(user_li))

# Using 'walrus' operator let us do not calculate a value of the variable twice
if ((n := len(user_li)) < 100):
    print(n)

# Scopes in Python
# There is a Global Scope and Function Scope;

some_variable = 0  # This variable is created in Global Scope


def some_func(some_variable):
    some_variable += 5
    return some_variable


# This is the better way to use a 'global scope' variable
# It's called - Dependencies Injection
print(some_func(some_func(some_func(some_variable))))


# nonlocal variable

def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: ', x)

    inner()
    print('outer: ', x)


outer()