import math



# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]


# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

squaredList= []
for i in data:
    minusVal = int(i) - mean(data)
    squareVal = minusVal**2
    squaredList.append(squareVal)

sum = 0
for i in squaredList:
    sum = sum+i

division = sum/(len(data) - 1)

sd = math.sqrt(division)

print(sd)