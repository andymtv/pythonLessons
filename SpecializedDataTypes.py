from collections import Counter, defaultdict, OrderedDict
import datetime
import time
from array import array

# Counter counts how many times each item of an iterable is occurred
# n = [1,2,3,4,5,5]
# s = 'My name is Andrew'
# print(Counter(n))
# print(Counter(s))

# defaultdict - gives us a way to avoid wrong key/value errors, and return a function instead
# di = defaultdict(lambda: 'Something went wrong',{'a' : 1, 'b' : 2})
# print(di['asda'])

# OrderedDict - allows us to order our dictionaries
# It keeps the order with which items was inserted
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
# d2 = OrderedDict()
# d2['a'] = 1
# d2['b'] = 2
# print(d == d2)

# Datetime allows us to work with date and time in Python in different ways
# print(datetime.date.today())
# print(time.time())

# Arrays in Python are different from another languages
# Arrays intialized with typecode - it means that we have to say what datatype we're going to use
# in this array.
# Arrays a little bit 