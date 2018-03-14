###Formatting of Iris information ###http://archive.ics.uci.edu/ml/datasets/Iris
#############  Solution 1  #######################

f = open("iris.csv") #opens csv file

for line in f:
  line = line.replace(',', ' ') #for each line in the file, replace commas with spaces
  line = line.rstrip() #strips whitespace form ends
  print(line[:11], line[12:16], line[16:].strip()) #aligns columns evenly 

  
f.close() #closes csv file

############  Solution 2  ########################

print ("petal length ", "petal width ", "sepal length ", "sepal width") #adds titles

with open ("iris.csv") as f: #opens csv file
  for line in f: #for each line in the file. And below: align column and remove commas 
    print ("{:>7} {:>12} {:>13} {:>12}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))

f.close() #closes csv file
