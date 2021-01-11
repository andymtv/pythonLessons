from time import time

def my_dec(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        t3 = t2 - t1
        print(f'It took {t3} seconds')
        return res
    return wrapper

@my_dec
def my_own_range(num, start=0):
    new_list = []
    while start < num:
        start += 1
        new_list.append(start)
    return new_list

@my_dec
def py_range(n):
    res = []
    for i in range(n):
        res.append(i)
    return res

l1 = py_range(1000000)
l2 = my_own_range(1000000)

@my_dec
def generator(num):
    for i in range(num):
        yield i

n = generator(10)
print(next(n))
print(next(n))
print(next(n))
