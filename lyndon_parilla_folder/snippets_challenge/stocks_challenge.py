print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

name = input('Enter your name: ')
savings = input('What is your savings: ')
stock = input("Which stock are you interested in? Type 'amazon' for Amazon, 'apple' for Apple, 'fb' for Facebook, 'google' for Google and 'msft' for Microsoft.")
# I used the input function to take information from the user and store it in a variable. 
print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
#stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amazon':
    if int(savings) > 0:
            num_of_amazon_shares = int(savings)/3000
            print (f'{name} has {savings} in savings and can buy {num_of_amazon_shares} of {stock} shares at the current price of 3000 ') 

if stock == 'apple':
    if int(savings) > 0 :
        num_of_apple_shares = int(savings)/100
        print (f'{name} has {savings} in savings and can buy {num_of_apple_shares} of {stock} shares at the current price of 100') 

if stock == 'fb':
    if int(savings) > 0 :
        num_of_fb_shares = int(savings)/250
        print (f'{name} has {savings} in savings and can buy {num_of_fb_shares} of {stock} shares at the current price of 250') 


if stock == 'google':
    if int(savings) > 0:
        num_of_google_shares = int(savings)/1400
        print (f'{name} has {savings} in savings and can buy {num_of_google_shares} of {stock} shares at the current price  of 1400') 


if stock == 'msft':
    if int(savings) > 0:
        num_of_msft_shares = int(savings)/200
        print (f'{name} has {savings} in savings and can buy {num_of_msft_shares} of {stock} shares at the current price of 200 ') 


#I used two conditions for each stock in order for the program to reach the print function. for the 2nd if statment the string savings had to be converted to an int. 
# These if statements can be reduced to the format below, however I used this format in order to help me understand the flow better. 
'''
Your code should look like this:
if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()
