def my_dec(func):
    def wrap_func(*args, **kwargs):
        print('Start of the Program')
        func(*args, **kwargs)
        print('End of the Program')
    return wrap_func

@my_dec
def hello(greeting, emoji):
    print(greeting, emoji)

s = 'Hiiiii!!!!'
e = '♥'
hello(s, e)

# Here we're going to create our performance decorator
# It will show us how many milliseconds it takes to complete a function
from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000):
        i*55

long_time()