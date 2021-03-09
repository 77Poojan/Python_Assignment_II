class_list = ['Pukar','Samba','John']
name = 'John'
if any([True for k in class_list if k==name]):
    print("John Found")
else:
    print("Not Found")