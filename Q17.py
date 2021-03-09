# Python program for simple calculator 
  
# Function to add two numbers  
def add(num1, num2): 
    return num1 + num2 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    return num1 - num2 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 
  
# Function to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 
  
print("Please select operation +,-,&,/")
  
  
# Take input from the user  
select = str(input("Select operations form: ")) 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == "+": 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == "-": 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == "*": 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == "/": 
    if number_2 == 0:
        number_2 = int(input("Second number is zero ReEnter second number: "))
        print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
    else:
        print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Invalid input") 