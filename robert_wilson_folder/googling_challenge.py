from collections import Counter
import numpy as np

'''
GOOGLING CHALLENGE!!
Today, we'll ask you to write a bunch of small pieces of code.
Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.
So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!
For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
# The sort function can be used to sort a list in either an ascending or descending order
# https://www.codespeedy.com/sort-words-in-a-list-in-alphabetical-order-in-python/#:~:text=Sort%20Words%20in%20a%20List%20in%20Alphabetical%20Order,sort%20words%20in%20a%20list%20in%20alphabetical%20order.

print('QUESTION 1\n')

my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
my_friends.sort()
print(my_friends)

# 1B. Comment your code in 1A to convince yourself you understand how it works

print()

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
# The for loop below will iterate throught the keys only and then print the name of the each key
# https://pythonexamples.org/python-print-dictionary/

print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}
for key in my_account.keys():
    print(key)
# 2B. Comment your code in 2A to convince yourself you understand how it works

print()

# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
# The function does several things. The .lower() turns the entire string to lower case
# The function will return the word count using --return my_string.count(wood)
# Lastly, the print statement displays the number of times the word "wood" appears in the my_string variable
#https://www.pythonpool.com/python-count-words-in-string/#:~:text=%20Different%20Ways%20in%20Python%20to%20count%20words,in%20a%20String%20in%20Python%20using...%20More%20

print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

def return_count(my_string,wood):
    my_string=my_string.lower() 
    return my_string.count(wood)

print(return_count(my_string, 'wood'))
# 3B. Comment your code in 3A to convince yourself you understand how it works

print()

# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
# First, I had to import a library --from collections import Counter
# Counter() iterates throught the list and return a dictionary. This dictionary then has a <key>, the name of the item and a <value>, 
    # the number of times the items appears
# https://stackoverflow.com/questions/20510768/count-frequency-of-words-in-a-list-and-sort-by-frequency

print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
counts = Counter(my_list)
print(counts)
# 4B. Comment your code in 4A to convince yourself you understand how it works

print()

# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
#
# https://www.tutorialspoint.com/get-unique-values-from-a-list-in-python
print('QUESTION 5\n')

my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
A_set = set(my_list)
New_List=list(A_set)

print("The unique values from the list are:")
print(New_List)

# 5B. Comment your code in 5A to convince yourself you understand how it works

print()

# 6A. Import numpy, then use it to generate a random number between 0-1
# The function will print random numbers between 0 - 10 and only display 6 number in the list
# https://www.sharpsightlabs.com/blog/np-random-randint/
print('QUESTION 6\n')

# b = np.random.randint(low = 0, high = 10, size = 6)
# print(b)

# 6B. Comment your code in 6A to convince yourself you understand how it works

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 
Remember to comment all your code and push your work to your Github repo when you're done!
'''
print()




