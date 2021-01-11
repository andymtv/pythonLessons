import sys

# In that way we can give parameters for Python file from the terminal
first_name = sys.argv[0]
last_name = sys.argv[1]
print(f'Hi, I\'m {first_name} {last_name}')