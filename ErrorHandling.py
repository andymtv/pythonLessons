# Simple Error Handling
def try_err1():
    # With the loop we can rerun our program until we get an expected result
    while True:
        # With this block we can avoid errors
        try:
            age = int(input('What is your age?: \n'))
            print(age)
        # If we catching an error then code in this block will be executed
        except:
            print('Please enter a number.')
        else:
            print('Thank you!')
            # We can stop the loop with this keyword
            break

# We also can handle specified types of errors, we do this in the 'exception' block.
# Only one exception block can be executed, it means that only one type of error can be handled at the time
def try_err2_error_types():
    # With the loop we can rerun our program until we get an expected result
    while True:
        # With this block we can avoid errors
        try:
            age = int(input('What is your age?: \n'))
            10/age
            print(age)
        # This block will be executed if there was a ValueError
        except ValueError:
            print('Please enter a number.')
        # This block will be executed if there was a ZeroDivisionError
        except ZeroDivisionError:
            print('Please enter a number greater than zero.')
        else:
            print('Thank you!')
            # We can stop the loop with this keyword
            break

# We can define any types of errors as variables in our exception block
def try_err3_cust_sum(num1, num2):
    # With this block we can avoid errors
    try:
        return num1 + num2
    # This block will be executed if there was a TypeError
    except TypeError as err:
        print('Please enter a number,', err)
    else:
        print('Thank you!')

def try_err4_finally():
    # With the loop we can rerun our program until we get an expected result
    while True:
        # With this block we can avoid errors
        try:
            age = int(input('What is your age?: \n'))
            10/age
            print(age)
        # This block will be executed if there was a ValueError
        except ValueError:
            print('Please enter a number.')
            continue
        # This block will be executed if there was a ZeroDivisionError
        except ZeroDivisionError:
            print('Please enter a number greater than zero.')
            break
        else:
            print('Thank you!')
            # We can stop the loop with this keyword
            break
        finally:
            print('ok, i\'m finally done')
        print('can you hear me?')

try_err4_finally()