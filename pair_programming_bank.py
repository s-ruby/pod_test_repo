
#let's re-write the pair programming challenge as a class 

class BankAccount():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0


    def deposit(self, amount):
        self.balance += amount
        
    def getBalance(self):
        return f"Your current balance is: {self.balance}"


    def withdraw(self, amount):
        self.validate()
        if amount <= self.balance:
            self.balance -= amount
            print(f"Sucessfully withdrew ${amount}")
        else:
            print(f"Insufficient funds! Only ${self.balance} available")
            

    def validate(self):
        logged_in = False
        while logged_in == False:
            print('Validating account info:')
            username = input('Enter username: ')
            password = input('Enter password: ')
            if username == self.username and password == self.password:
                logged_in = True
                print('Logged in!')
            else:
                print('Incorrect username/password combo!')
                
                


