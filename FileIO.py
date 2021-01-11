# open('filename', 'mode') allows us to work with file
my_file = open('../../Desktop/app/test.txt')

# read() returns all content of the file and set the cursor at the end of the file
print(my_file.read())

# readline() returns a single line from the file and set the cursor at the next line's beginning
print(my_file.readline())

# seek(index) put the cursor at the specified position
# The cursor will be standing at the beginning
my_file.seek(0)

# close() stops working with the file
my_file.close()

# action_modes: r, rb, r+, rb+, w, wb, w+, wb+, a, ab, a+, ab+
# r - read the file, the cursor stands at the beginning of the file
# rb - read the file in binary format, the cursor stands at the beginning of the file
# r+ - read and write the file, the cursor stands at the beginning of the file
# rb+ - read and write the file in binary format, the cursor stands at the beginning of the file
# w - write the file, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# wb - write the file in binary format, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# w+ - write and read the file, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# wb+ - write and read the file in binary format, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# a - append the information to the file, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# ab - append the information to the file in binary format, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# a+ - append the information and read the file, the cursor stands at the end of the file, if the file doesn't exist - creates the file
# ab+ - append the information and read the file in binary format, the cursor stands at the end of the file, if the file doesn't exist - creates the file

# pathlib - it is a library tha allows us easily work with file's paths