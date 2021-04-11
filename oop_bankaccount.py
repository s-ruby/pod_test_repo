class BankAccount():

    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance


    def deposit(self, amount):
        self.validate()
        self.balance += amount
        print(f"Sucessfully deposited ${amount}")
        
        
    def getBalance(self):
        print(f"Your current balance is: {self.balance}")
        

    def withdraw(self, amount):
        self.validate()
        if amount <= self.balance:
            self.balance-= amount
            print(f"Sucesfully withdrew ${amount}")
        else:
            print(f'Insufficient funds! Only ${self.balance} available')
            
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
            
    

# checkingsAccount = BankAccount("sruby", "ilovecats", 200)
# checkingsAccount.deposit(1000)
# print(checkingsAccount.balance)
# checkingsAccount.withdraw(500)
# print(checkingsAccount.balance)


# savingsAccount = BankAccount("sruby", "meow321", 1000)
# print(savingsAccount.balance)
# savingsAccount.deposit(5000)