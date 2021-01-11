list_one = [1, 2, 3, 4, 5, 6, 7]
list_second = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_third = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
list_mix12 = [list_one, list_second]
list_mix23 = [list_second, list_third]
list_mix31 = [list_third, list_one]
matrix_one = [list_mix12, list_mix23]
matrix_second = [list_mix23, list_mix31]
matrix_third = [list_mix31, list_mix12]
matrix = [matrix_one, matrix_second, matrix_third]


def looping_through_matrix(matrix):
    # This while loop is needed if user will want to repeat this function on items in his matrix
    i = 0
    while (i < 1):
        for items in matrix:
            print(items, '\n')
            i += 1
        user_response = input('Should we go deeper? (Yes or No) \n')
        if (user_response == 'Yes'):
            i = 0
            item_in_matrix = int(input('Type a number of item you want to go to: \n'))
            looping_through_matrix(matrix[item_in_matrix])
            return matrix
        else:
            return matrix


looping_through_matrix(matrix)