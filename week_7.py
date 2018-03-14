### Function for factorials of intigers only tested with 5, 7, 10 and 10.5 ### Eimear Butler

def fact(x): #define "fact" function with "x" as the placeholder for the input for the function later
  while x == int(x): #when "x" is an integer
    for i in range(1, x):  #for "i" in the variable range, dependin on the value of "x" 
      x = x * i #multiply "x" by each "i" generated as each loop is run 
    return x #return x when loop is finished i.e. when loop comes to the end of the range

#instruct function to be run with x replaced with 5, 7, 10 and 10.5. Print result (returned "x" at the end of function)
print(fact(5)) #result 120
print(fact(7)) #result 5040
print(fact(10)) #result 3628800 
print(fact(10.57)) #result "none" as expected as this is not an integer
