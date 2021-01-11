def foobar(li):
    for item in li:
        if item % 15 == 0:
            print('foobar')
        elif item % 5 == 0:
            print('bar')
        elif item % 3 == 0:
            print('foo')
        else:
            print(item)

my_list = []

for i in range(1,35001):
    my_list.append(i)

foobar(my_list)