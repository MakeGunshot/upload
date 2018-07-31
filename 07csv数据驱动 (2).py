
import csv
with open('./07data.csv') as csvfile:
    datas=csv.reader(csvfile)
    for row in datas:
        print(','.join(row))



