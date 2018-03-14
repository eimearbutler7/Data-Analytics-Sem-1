#Collatz Con #Ian McLoughlin Example

n = int(input("Please enter an integer: "))
start = [n]

if n < 1:
  quit #stops loop once "n" is less than 1
while n > 1: #otherwise, this loop will run
  if n % 2 == 0: #makes sure "n" is an even number
    n = n/2 # halves "n" for the next loop
    print(n)
  else: #if while loop fails (returns false) else loop kicks in
    n = 3 * n + 1
    print(n)
    start.append(n) #once we have a new "n" it is appended back into the "start" list to begin the loop again
    
    


#FizzBuzz #Ian McLoughlin Example

i = 1

while i <= 100: #sets limits of loop
  if (i % 3 == 0) and (i % 5 == 0): #requires 3 and 5 as an even denominator to print fizzbuzz  
      print("FizzBuzz")
  elif i % 3 == 0: #requires only 3 as an even denominator to print fizzbuzz
    print("Fizz")
  elif i % 5 == 0: ##requires only 5 as an even denominator to print fizzbuzz
    print("Buzz")
  else: 
    print(i) #is not evenly divisible by 3 or 5
  i = i + 1 #increases i by 1 before begining loop again



# is it tuesday?? #Ian McLoughlin Example

import datetime #imports standard module within python for date/time

if (datetime.datetime.today().weekday()) == 1: # where 1 means Tuesday as per predetermined set of rules for datetime module
  print("yeah it is Tuesday")
else:
  print("no not today!")
  
  
  
  
#Week 3 if/elif example #Ian McLoughlin Example

x = int(input("Please enter an integer: ")) #allows user to enter any integer

if x < 0:
  x = 0
  print('Negative changed to zero') #if "x" less than 0 change it to 0 and print "negative..."
elif x == 0: #if "x" is 0 print "zero"
  print('Zero')
elif x == 1: #if "x" is "1" print "single"
  print('Single')
else:
  print('More') #otherwise print "more"
print("the final value of x is:", x) #value of x varies depending on the above statement applicable
