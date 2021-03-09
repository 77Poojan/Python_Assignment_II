import csv

csvfile=open('Q13_CSV/data.csv','r', newline='')     
obj=csv.DictReader(csvfile)
my_list = []
for row in obj:
    r = dict(row)
    my_list.append(r)
print(my_list)