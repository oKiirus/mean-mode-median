import csv

median = 0

with open('ye.csv', newline = '') as f:
    file = csv.reader(f)
    data = list(file)
    
data.pop(0)
height = []
for i in range(0, len(data)):
    q = data[i][1]
    
    height.append(float(q))

n = len(height)
height.sort()
if n % 2 == 0:
    n1 = float(height[n // 2])
    n2 = float(height[n // 2  + 1])

    median = (n1 + n2) / 2
    
else:
    median = height[n // 2]


print(median)

