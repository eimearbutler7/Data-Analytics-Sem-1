### Function for factorials of intigers only tested with 5, 7, 10 and 10.5 ###

def fact(x):
  while x == int(x):
    for i in range(1, x): 
      x = x * i
    return x

print(fact(5)) #result 120
print(fact(7)) #result 5040
print(fact(10)) #result 3628800 
print(fact(10.57)) #result "none"
