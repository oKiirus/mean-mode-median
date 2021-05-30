import csv
import statistics as st

mode = 0

with open('ye.csv', newline = '') as f:
    file = csv.reader(f)
    data = list(file)
    
data.pop(0)

height = []
for i in range(0, len(data)):
    q = data[i][1]
    
    height.append(float(q))

mode = st.mode(height)
print(mode)

