import csv

data_list=[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':'John', 'address': '54 Love Ave', 'age': 21}]
csvfile=open('data.csv','w', newline='')
fields=list(data_list[0].keys())
obj=csv.DictWriter(csvfile, fieldnames=fields)      
obj.writeheader()      
obj.writerows(data_list)      
csvfile.close()