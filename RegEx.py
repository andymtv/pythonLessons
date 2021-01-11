import re

string = 'search this inside of this text'
# We can put a pattern inside of a variable, to use the variable instead of Class
pattern = re.compile('this')
# RegEx can find a string inside a text and returns this string as a Match object
s = pattern.search(string)
# span() returns a tuple with start and end indices
print(s.span())
# group() returns the searched text
print(s.group())
# findall() returns all occurrences of searched value as a list
f = pattern.findall(string)
print(f)
# fullmatch() returns Match Object if there is a full match, otherwise returns None
d = pattern.fullmatch(string)
print(d)
# match() matches zero or more characters at the beginning of the string
e = pattern.match(string)
