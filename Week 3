#Collatz Con

n = int(input("Please enter an integer: "))
start = [n]

if n < 1:
  quit
while n > 1:
  if n % 2 == 0:
    n = n/2
    print(n)
  else:
    n = 3 * n + 1
    print(n)
    start.append(n) 
    
    


#FizzBuzz

i = 1

while i <= 100:
  if (i % 3 == 0) and (i % 5 == 0):
      print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else: 
    print(i) 
  i = i + 1 



# is it tuesday??

import datetime

if (datetime.datetime.today().weekday()) == 1:
  print("yeah it is Tuesday")
else:
  print("no not today!")
  
  
  
  
#Week 3 if/elif example

x = int(input("Please enter an integer: "))

if x < 0:
  x = 0
  print('Negative changed to zero')
elif x == 0:
  print('Zero')
elif x == 1:
  print('Single')
else:
  print('More')
print("the final value of x is:", x)
