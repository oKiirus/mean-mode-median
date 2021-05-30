import csv

mean = 0

with open('ye.csv', newline = '') as f:
    file = csv.reader(f)
    data = list(file)
    
data.pop(0)
height = []
for i in range(0, len(data)):
    q = data[i][1]
    
    height.append(float(q))

n = len(height)
sum = 0
for e in height:
    sum += e

mean = sum / n

print(mean)