from functools import lru_cache
from Decorators import performance
# A function that generates the Fibonacci Sequence
def fib(n):
  """
  Info: Please, type a quantity of iterations only as an integer value
  """
  a = 0
  b = 1
  for n in range(n):
    yield a # yield returns the current value of this variable, but don't stop the function
    c = b + a
    a = b
    b = c

for n in fib(5):
  print(n)

# A custom class that allows us to create a Fibonacci Sequence
class MyFibonacciGenerator():
  current = 0
  num1 = 0
  num2 = 1
  def __init__(self, nums):
    self.nums = nums

  def __iter__(self):
    return self

  def fib_seq(self, nums):
    self.nums = nums
    count = iter(list(range(0, nums)))
    a = 0
    b = 1
    for i in count:
      c = a + b
      a = b
      b = c
      return a

  def __next__(self):
    if MyFibonacciGenerator.current < self.nums:
      n1 = MyFibonacciGenerator.num1
      n2 = MyFibonacciGenerator.num2
      n3 = n2 + n1
      MyFibonacciGenerator.num1 = MyFibonacciGenerator.num2
      MyFibonacciGenerator.num2 = n3
      MyFibonacciGenerator.current += 1
      return n1
    raise StopIteration


for n in MyFibonacciGenerator(5):
  print(n)


@lru_cache(maxsize=1000)
def fib(n):
  if n == 1 :
    return 1
  elif n == 2 :
    return 1
  elif n > 2 :
    return fib(n-1) + fib(n-2)

print(fib(50))
