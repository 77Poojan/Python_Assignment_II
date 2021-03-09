from functools import reduce

my_tuple = ("John","Neuman",15)
my_list=[("Rick","Coleman",None)]
my_list.append(my_tuple)

x = int(input(f'Enter number of entries: '))

for i in range(x):
    print(f'{i}th data entry:')
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    next_tuple = tuple([first_name,last_name,age])
    my_list.append(next_tuple)
    
avg = 0
cnt = 0
for j in my_list:
    if j[2]==None:
        avg = avg + 0
    else:    
        avg = avg + j[2]
    cnt += 1
avg = avg/cnt

next_list = []
tup = tuple()

for j in my_list:
    if j[2]==None:
       pass
    
    elif j[2] <= avg:
        tup = tuple([j[0],j[1],"Young"])   
             
    else:
       tup = tuple([j[0],j[1],"Old"]) 
    next_list.append(tup) 
    
print(next_list)          