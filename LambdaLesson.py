def filter_by_letter(array, letter):
    new_list = []
    for item in array:
        if item[0:1] == letter:
            print(item[0:1])
            new_list.append(item)
    return new_list

my_list = ['quebec','alpaca','clementina','gorgeus','spa','air','armor','benedette']

print(filter_by_letter(my_list, 'a'))

def filter_by_letter_simple(item, letter):
    return item[0:1] == letter

print(list(filter(lambda item:  filter_by_letter_simple(item, 'a'), my_list)))

my_list_1 = [5,12,23,65,20,177,80,55,105,300]
print(list(filter(lambda x: (x % 5 == 0), my_list_1)))

x = ''.join(my_list)
print(x)

y = ' '.join(x)
print(y)

string_1 = 'Break down the Rules'
string_2 = ''.join(string_1)
print(string_2)

# Square List Lambda Function
num_list = [5,4,3,2,1]

x = lambda e: e*e
new_num_list = []
for item in num_list:
    print(x(item))
    new_num_list.append(x(item))

print(new_num_list)
print(list(map(lambda num: num**2, num_list)))
# Function to sort tuples in list by the second item ascending

tup_list = [(0,2),(4,3),(9,9), (10,-1)]

tup_list.sort(key = lambda item: item[1])
print(tup_list)

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=lambda employee: employee.get('Name'))
print(employees, end='\n\n')

