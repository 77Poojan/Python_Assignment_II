class_list = dict()
class_list={'Pukar':2,'Samba':3}
data = input('Enter name & id separated by ":" ') 
temp = data.split(':') 
value = int(temp[1])

#Check id exists
if any([True for k,v in class_list.items() if v == value]):
    print("Same ID. ID will refer to new name.")

class_list[temp[0]] = int(temp[1]) 

#Sort item on basis of id
li = [(k, v) for k, v in sorted(class_list.items(), key=lambda item: item[1])] 
l1 = list(li[0])
l2 = list(li[1])

#First item on list
print(l1)

#Second item on list
print(l2)
