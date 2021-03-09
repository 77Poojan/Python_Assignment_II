my_tuple = ('John','Neuman','15')
my_list=[("Rick","Coleman","20")]
my_list.append(my_tuple)

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = input("Enter age: ")

next_tuple = tuple([first_name,last_name,age])
my_list.append(next_tuple)
print(f'\nUnsorted List => {my_list}')

sort_list = sorted(my_list, key=lambda tup: tup[2])
print(f'Sorted List => {sort_list}\n') 