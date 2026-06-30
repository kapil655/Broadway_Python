import csv
with open('day16.py','r') as file:
    reader = csv.reader(file)
    for column in reader:
        print(column)

import csv

data = [["kapil", 12, 7896541230]]

with open('data1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)