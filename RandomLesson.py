import random

# Create a list for future reference
li = []

# Add numbers 0 through 10 in the list
for i in range(10):
    li.append(i)

# This function randomly shuffle numbers in the list, provides changes 'in place'< returns None.
random.shuffle(li)

# This function randomly choose N elements from the "1st" argument list, and returns it as a list.
random.sample(range(100), 10)

# This function choose a random element from a non-empty sequence and returns it
random.choice(li)

# This function choose a random element from a range(start, stop, step)
random.randrange(0,10001)

# This function randomly choose N in the interval [0,1]
random.random()
(random.random() * 60) + 1

# This function returns random integer in range [a, b], including both end points.
random.randint(1,203)