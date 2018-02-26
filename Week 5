#Project Euler Question

######### Solution 1 ###############################

i = 20

while i > 1:
  i += 20
  if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0: 
    break
print(i) 

######### Solution 2 ###############################

x = 1
for i in range (1,21):
    if (x % i) > 0: 
        for s in range (1,21):
            if (x * s) % i == 0:    
                x = x * s
                break
print (x)     
    
######## Solution 3 - in progress, to test #####################

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

#Testing Sum all Even numbers 1 to 100

sum = 0
i = 0

while i <= 100:
  if i % 2 == 0:
    sum = sum + i
  i = i + 1  

print(sum)
