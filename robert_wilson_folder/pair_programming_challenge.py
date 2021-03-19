'''
For this challenge, you will work in groups of 2 to 'pair program'
You'll need to work together to complete this challenge!
In general, 1 person should be typing, and the other should be leading what to code
But, it is always okay to swap roles or for the typing person to add their ideas too

-------------------------------------------------------------------


Your challenge: Make a bank account!
In this challenge, we want to make a bank account with 3 crucial functions
-create_account() - this function will initialize a bank account
-deposit() - add money to the account
-withdraw() - remove money from the account


PART 1: create_account()
This function should make a bank account!
The function does not need to take any arguments
The function should prompt the user using input() for username/password
The function should return a dictionary with 3 key/value pairs:
-username (string, should be what the user inputs)
-password (string, should be what the user inputs)
-balance (float, initialize this to 0)
'''

print('PART 1\n')
# TODO: define the create_account() function here and make sure it works
# HINT: make sure it works by doing something like my_account = create_account()
# Then print out my_account to see whether it has the correct info

def create_account():
    username  = input("What is your username?: ")
    password = input("What is your password?: ")
    user_acct = {
        "username": username,
        "password": password,
        "balance": 0           
    } 
    return (user_acct)

my_account = create_account()
print(my_account)

print()

'''
PART 2: deposit()
This function should make a deposit to add money to the account
The function should take 2 arguments
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to deposit)

The function does not need to return anything, but should increase the balance value by the appropriate amount

Test your function by making a few deposits to your account, then printing out your account
'''

print('PART 2\n')
# TODO define the deposit() function here and make sure it works

def deposit(account, amount):
    account["balance"] += amount

deposit(my_account, 380.23)
deposit(my_account, 124.89)
deposit(my_account, 80.23)
deposit(my_account, 54.12)

print(my_account)    


'''
PART 3: withdraw()
This function should make a withdrawal to take money out of the account
The function should take 2 arguments:
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to withdraw)

FIRST, the function should check whether there is enough money in the account to withdraw the requested amount
-If there is enough money, the function should decrease the balance value by the appropriate amount
-If there is not enough money, the function should print a message about the balance and tell the user there is not enough available to make that withdrawal

Test your function by making several withdrawals to your account
-try some you think will work AND some you think will not be allowed (more than the balance)
'''

print('PART 3\n')
# TODO define the withdraw() function here and make sure it works

def withdraw(account, amount):
    if amount <= account['balance']:
        account["balance"] -= amount
    else:
        print(f'Insufficient funds! Only ${account["balance"]} available')

withdraw(my_account, 455.44)
print(my_account)

print()

def withdraw(account, amount):
    if amount <= account['balance']:
        account["balance"] -= amount
    else:
        print(f'Insufficient funds! Only ${account["balance"]} available')

withdraw(my_account, 855.44)
print(my_account)


print()


print('PART 4\n')
'''
BONUS QUESTION 4: Password-protect withdrawal and deposits
Make new deposit_secure() and withdraw_secure() functions that prompt the user for their username/password FIRST
Only let the transaction proceed if they enter the right info!
Otherwise, tell the user the info is wrong

Test out your new functions to make sure they accept correct info, and let the user know if the password/username is incorrect
'''


# TODO: define password-protected withdraw_secure() and deposit_secure() functions
# HINT: there are tons of ways to do this correctly
# HINT: you can write any additional functions if you like

password_value = "Rob"   
input_password = ""
password_attempt = 1
is_password_lock = False

while input_password != password_value and not (is_password_lock):
    if password_attempt <= 3:
        input_password = input("Enter Password: ")
    else :
        is_password_lock = True 
    password_attempt = password_attempt + 1

if is_password_lock:
    print("Account is locked due to excessive attempts")
else :
    print("Login is successful!")   



def withdraw_secure(account, amount):
    if amount <= account['balance']:
        account["balance"] -= amount
    else:
        print(f'Insufficient funds! Only ${account["balance"]} available')    

withdraw_secure(my_account, 100)
print(my_account)        

print()

def deposit_secure(account, amount):
    account["balance"] += amount

deposit_secure(my_account, 300)
print(my_account)


