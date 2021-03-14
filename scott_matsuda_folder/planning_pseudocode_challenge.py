'''
Planning & pseudocode challenge!

For each piece here, write out the pseudocode as comments FIRST, then write your code!

At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Will you choose to make each shipping order as a dictionary or list? Why?

# A dictionary.  Each dictionary needs to have 3 keys: destination, date_shipped, and weight




'''
print('\nPART 1')

# Assign 3 separate orders to 3 separate variables
# Assign key/value pairs to include destination, date shipped, and weight

order1 = {'destination': 'Philadelphia', 'date_shipped': '03/10/21', 'weight': 5.6}
order2 = {'destination': 'San Francisco', 'date_shipped': '03/11/21', 'weight': 3.7}
order3 = {'destination': 'New York', 'date_shipped': '03/09/21', 'weight': 2.9}

'''
2. Building the database

Now, let's put the orders all into a database together (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')
print()
# Create a variable (list of all the orders), each order is an indexed item in the list
order_list = [order1, order2, order3]

# print order database
print(order_list)

'''
3. Define a function called add_order() that adds one more orders to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')
print()
# create an order inside of a dictionary
order4 = {'destination': 'Hawaii', 'date_shipped': '03/15/21', 'weight': 7.8}

# Define a function called add_order() with parameters (order_list, order4)
def add_order(order_list, order4):
    # Append the order to the database
    order_list.append(order4)
# call the add_order function
add_order(order_list, order4)
# print the database
print(order_list)

'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')
print()

# Define a function called complete_order() that takes two parameters (order_list, order_index)
def complete_order(order_list, order_index):
    # add True value to completed key
    order_list[order_index]['complete'] = True
# call the complete_order() function
complete_order(order_list, 2)
# print the database
print(order_list)
