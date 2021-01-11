def custom_sort(a,b):
    return a if a > b else b

my_list = [22,1,2,6,4,26,23,15,14]

i = 0
k = i + 1
while k < len(my_list):
    custom_sort(my_list[i], my_list[k])
    i += 1
    k += 1
print(my_list)