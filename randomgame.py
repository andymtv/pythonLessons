import sys
import random
 
# In that way we can give parameters for Python file from the terminal
start = sys.argv[1]
try:
	first = int(sys.argv[2])
	last = int(sys.argv[3])
except:
	print('You wrote wrong numbers, in cause of that we\'re using our numbers.')
	first = random.randint(1, 5)
	last = random.randint(6, 15)

if start == 'start' or start == 'Start':
	print(f'Hey guess a number from {first} to {last}')
	answer = random.randint(first,last)
	user_guess = ''
	while user_guess != answer:
		user_guess = int(input('What\'s the number: '))
		if user_guess != answer:
			print('Oh, sorry, but it\'s not correct answer')
		else:
			print('Yeah, you are right!')
			break