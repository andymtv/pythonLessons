def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

# This function keeps us DRY(Do not Repeat Yourself)
def new_multiply_by2(item):
    return item *2

# The Map Built-In function in Python gives us a way to execute a specified function given as a first argument,
# on each item of a list given as a second argument

print(list(map(new_multiply_by2, [1,2,3])))

def only_odd(item):
    return item % 2 != 0

# The Filter Built_in Python function gives us an opportunity to call a function given as a first argument,
# which will helps us to filter items of a list given as a second argument
print(list(filter(only_odd, [1,2,3])))

def my_subs(a, b):
    return a - b

# The Reduce  function gives us an opportunity to call a function given as a first argument,
# which will helps us to filter items of a list given as a second argument

def my_reduce(func, sequence, initial = 0):
    it = iter(sequence)
    new_list = []
    for item in it:
        initial = func(initial, item)
        new_tuple = (initial, item)
        new_list.append(new_tuple)
    return new_list

print(my_reduce(my_subs,[1,2,3,4,5,6,7], 0))

# This is how to use 'lambda expressions' in Python
my_list = [1,2,3,4,5]
new_list = []
for item in my_list:
    x = lambda a: a * 2
    new_list.append(x(item))

print(new_list)