# Week 1 Fibonacci Program #Ian McLoughlin Example
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 23
ans = fib(x)
print("Fibonacci number", x, "is", ans) 

# OUTPUT: My name is Eimear so the first and last letter of my name (E + R = 5 + 18) give the number  23. The 3rd Fibonacci number is 28657.



# Week 2 Fibonacci Program #Ian McLoughlin Example
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Butler"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# OUTPUT My surname is Butler
# The first letter B is number 66
# The last letter r is number 114
# Fibonacci number 180 is 18547707689471986212190138521399707760

# when ord() is given a string of a single unicode character, it generates the intiger representing the unique code point of that character as per the unicode list. 
