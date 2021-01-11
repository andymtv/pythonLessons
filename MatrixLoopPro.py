# define the function

def print_matrix_values(matrix):
    # Trying to catch a TypeError if the element passed in function is not iterable
    try:
        matrix_length = len(matrix)
        i = 0
        while (i < 1):
            # Here are some linguistic tricks just to be more correct
            end_of_word = 'items' if matrix_length > 1 else 'item'
            end_of_sentence = 'they are' if matrix_length > 1 else 'it is'
            print(f'\nMatrix has {matrix_length} {end_of_word} inside and here {end_of_sentence}:', '\n')
            for item in matrix:
                print(item, '\n')
                i += 1
            user_response = input('Do you want to go deeper inside your matrix?(Yes or No)\n')
            if (user_response == 'Yes' or user_response == 'yes'):
                k = 0
                # Looping while we get the correct form of user response
                while (k < 1):
                    # Trying to catch errors if form of user response isn't correct
                    try:
                        k += 1
                        number_of_item = int(input('\nType the number of item you want to go to (As a number):\n'))
                        print('\nGoing deeper...\n')
                        try:
                            iter(print_matrix_values(matrix[number_of_item]))
                        except TypeError:
                            i = 1
                    except ValueError:
                        print('\nType the correct number!')
                        k = 0
                    except IndexError:
                        print('\nThis number is out of range!')
                        k = 0
            elif (user_response == 'No' or user_response == 'no'):
                i += 1
                print('Okay, Goodbye!\n')
            else:
                i = 0
                print('Sorry, but i don\'t understand you. Can you repeate please?\n')
    except TypeError:
        print('''
Oh, sorry, but you can\'t going deeper...

There are 2 ways why this is happened: First - the element passed in function is not iterable. Second - you\'ve reached the uniterable element in your matrix.
    ''')
        the_end = '''
This is the end
Hold your breath and count to ten...
    '''
        print(the_end)


# The end of the function

list_one = [1, 2, 3, 4, 5, 6, 7]
list_second = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_third = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
list_mix12 = [list_one, list_second]
list_mix23 = [list_second, list_third]
list_mix31 = [list_third, list_one]
matrix_one = [list_mix12, list_mix23]
matrix_second = [list_mix23, list_mix31]
matrix_third = [list_mix31, list_mix12]
matrix_mix = [matrix_one, matrix_second, matrix_third]

print_matrix_values(matrix_mix)