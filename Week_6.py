###Formatting of Iris information ###http://archive.ics.uci.edu/ml/datasets/Iris
##Solution 1

f = open("iris.csv")

for line in f:
  line = line.replace(',', ' ')
  line = line.rstrip()
  print(line[:11], line[12:16], line[16:].strip())

  
f.close()

##Solution 2

print ("petal length ", "petal width ", "sepal length ", "sepal width")

with open ("iris.csv") as f:
  for line in f:
    print ("{:>7} {:>12} {:>13} {:>12}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))

f.close()
