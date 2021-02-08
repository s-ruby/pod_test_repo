print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name.")

# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input("How much are you interested in saving?"))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

if stock == "amzn":
    price = amazon
    shares = price/savings
elif stock == "aapl":
    price = apple
    shares = price/savings
elif stock == "fb":
    price = fb
    shares = price/savings
elif stock == "goog":
    price = google
    shares = price/savings 
elif stock == "msft":
    price = msft
    shares = price/savings
else:
    price = "try again"  

print()
if price == "try again":
    input("invaild entry")
else:
    input(f"{name} has ${savings} in savings and he can buy {shares} of {stock} at the current price of ${price}.") 
print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()