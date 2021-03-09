#Basic Format for Banking Application of a Customer

# Customer Class
class Customer:
    # Some Customer Attributes
    def __init__(self, name, phone_number,password):
        self.name = name
        self.phone_number = phone_number
        self.password = password
    
    # Login Module
    def login(self,name,password):
        if (self.name == name) & (self.password == password):
           my_Account()

# Account Module after Login
class my_Account:
    def send_Money(self):
        pass
    def payments_and_transfers(self):
        PT()
    def activity_Log(self):  
        pass
    def extras(self):
        pass   
   
class PT:
    # Methods of Payment
    def bill_Payment(self):
        pass
    def topup_Payment(self):
        pass
    def recharge_Card(self):
        pass
            
# A Customer Object
c1 = Customer("Mina", 36,"12332122")
c1.login("Mina","12332122")

