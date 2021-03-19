'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''

# https://www.programiz.com/python-programming/methods/list/sort
# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
my_friends.sort() # sorts the list of names
print(my_friends) # prints the sorted list
print()
# 1B. Comment your code in 1A to convince yourself you understand how it works

# I understand how it works.  I sorted the list using the sort method, then I printed it out

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')
# https://www.geeksforgeeks.org/python-dictionary-keys-method/
my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}
print(my_account.keys()) # prints the keys from the dictionary called my_account
print()


# 2B. Comment your code in 2A to convince yourself you understand how it works

# keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary.


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
# https://www.tutorialspoint.com/python3/string_count.htm
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
print(my_string.count('wood')) 
print()

# 3B. Comment your code in 3A to convince yourself you understand how it works

# The count() method returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
print(my_list.count('banana')) # count the number of times banana appears in the list
print()

# 4B. Comment your code in 4A to convince yourself you understand how it works

# same as 3B.

# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')

print(list(set(my_list)))
print()

# 5B. Comment your code in 5A to convince yourself you understand how it works

# https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/
# Banana is not unique, but I included it anyway because it's different from an apple, manago, and a cherry

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')
import numpy as np # import numpy library
rand_num = np.random.rand(1) # create a variable and assign it a random value between 0 and 1
print("Random number between 0 and 1:") # extraneous print statement
print(rand_num) # print results
print()

# 6B. Comment your code in 6A to convince yourself you understand how it works

# https://www.w3schools.com/python/numpy_random.asp

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
