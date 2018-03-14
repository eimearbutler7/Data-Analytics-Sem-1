#Project Euler Question 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


######### Solution 1 ###############################

i = 20

while i > 1: #i greater then 1 gurantees while loop will be used
  i += 20  #the final number must be divisible by 20 so increasing by 20 is relevant and faster than increasing by 1
  if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0: 
    break #condition to stop is when the number is divisible by 11 - 19 evenly also. 
print(i) 


######### Solution 2 ###############################

x = 1
for i in range (1,21): #rane function means loop will repeat throuh i being 1-20
    if (x % i) > 0: #where x / i results in an even division
        for s in range (1,21): 
            if (x * s) % i == 0: #where (x(1) * s(1-20) / i(1-20) results in an even division    
                x = x * s #increase x by a multiplying it by the value of s which should speed up the loops as the result will be the next largest divisible number as the loop continues
                break #end when lwest number divisible by all numbers found
print (x)     #print answer







######## Solution 3 - IN PROGRESS, to test #####################

i = 20

for x in range(1,20): 
  if i % x == 0: 
    i = i + 20
  else:
    i = i + 20
  print(i) 

  #or

numbers = [11,12,13,14,15,16,17,18,19]
i = 1
x = 1
while x >= len(numbers): #or for n in numbers: if i % n == 0: 
  if i % numbers[x] == 0: 
    x = x + 1
  else:
    i = i + 20
  print(i) 

#or

n = int()
start = [n]
x = 11

if n > 3000000:
  quit
while n < 3000000:
  if n % x == 0:
    x = (x + 1)
    print(n)
  else:
    n = 3 * n + 1
    print(n)
    start.append(n)  
    
#or Compute the lowest common multiple of a and b

def lcm(11, 12):
  print 11 * 12 / gcd(11, 12)

#or

from fractions import gcd
a = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i/gcd(lcm, i)
print lcm

#Project Euler Question 1  #Ian McLoughlan Example
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

sum = 0
n = 1
while n < 1000:
  if n % 3 == 0:
    sum = sum + n
  elif n % 5 == 0:
  n = n + 1
  
  print(sum)
   
#Testing Sum all Even numbers 1 to 100

sum = 0
i = 0

while i <= 100:
  if i % 2 == 0:
    sum = sum + i
  i = i + 1  

print(sum)
