try:
    with open('../../Desktop/app/some.txt', mode='r+') as file:
        for i in range(3):
            file.write(f'Ha ha ha \n')
        file.seek(0)
        print(file.tell())
        print(file.read())
        print(file.tell())
except FileNotFoundError as err:
    print('File doesn\'t exist')