# This is how the 'For' loop works underneath the hood
def my_for_loop(iterable):
    # We create an 'iterator' with 'iter()' function
    # This function allows us to use 'next()' function and its returns an 'iterator' object
    # The 'iterator' object return its items one by one
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
    # Here we're trying to handle the 'StopIteration' Error if there is no more items in the 'iterator' object
        except StopIteration:
            break


my_li = range(0,11)

for i in my_li:
    print(i)

def fib_seq(n):
    a = 0
    b = 1
    fib_seq_list = []
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


