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
Assign 3 separate orders to 3 separate variables

'''

# Each shipping order will contain 3 seperate pieces of information.
# I will structure my data as a dictionary containing a <key> <value> pair.
# All of the keys will various string and integer values.
# Using a dictionary will allow me to easily add a key for additional details that may be needed.
 #  or edit the existing values for each key within each dictionary.

print('\nPART 1') 

shipping_order_1 = {'destination':'225 Amsterdam Ave., NY, NY', 'shipped':'01/25/21', 'weight':'5.6'}
shipping_order_2 = {'destination':'104 Columbus Ave., NY, NY', 'shipped':'11/25/20', 'weight':'3.2'}
shipping_order_3 = {'destination':'2852 Broadway, NY, NY', 'shipped':'03/01/21', 'weight':'15.6'} 

print(shipping_order_1)
print(shipping_order_2) 
print(shipping_order_3)

# shipping_order_1['completed_order'] = True
# print(shipping_order_1) 

'''
2. Building the database
Now, let's put the orders all into a database togther (all the orders are stored in 1 variable).  
Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!).  
Print out the database to make sure all the info is in there.  

'''
# I want to create a variable called shipping_details to include the three seperate shipping orders
#  I will create a list with a nested dictionary inside the list.
# Because I only have 1 list, the list index.
# I will create a print statement -- print(shipping_details) to output all items listed in the dictionary. 

print('\nPART 2')

shipping_details = [

                        {'destination':'225 Amsterdam Ave., NY, NY', 'shipped':'01/25/21', 'weight':'5.6'},
                        {'destination':'104 Columbus Ave., NY, NY', 'shipped':'11/25/20', 'weight':'3.2'},
                        {'destination':'2852 Broadway, NY, NY', 'shipped':'03/01/21', 'weight':'15.6'}

                   ]   

print(shipping_details)

# shipping_details[2]['completed_order'] = True
# print(shipping_details) 

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 

'''
# I will define a function called add_order().
# I will append the shipping_details list with a new order.
# I will add a new dictionary keeping the same format as the previous three (3).
# I will use --len() in a print statement to see if the size of my dictionary has increased.
#  for ex: print(len(shipping_details)).
# I will print only the new dictionary to see the details of that dictionary.
# Lastly, I print the entire list of dictionaries. 

print('\nPART 3') 

def add_order(shipping_order_4):
    shipping_details.append(shipping_order_4)
add_order({'destination':'501 Manhattan Ave., NY, NY', 'shipped':'02/14/21', 'weight':'6.6'})

print(len(shipping_details))
print(shipping_details[3].items())

print()

print(f'My dictionary now contains 4 seperate orders-- {shipping_details}') 

'''
4. Define a function called complete_order() to mark a specific order in your database complete 
This means you'll need a new piece of data inside the order that is True when the order is complete. 
Test this out and print out your database to make sure it works! 
HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database

'''

print('\nPART 4')

# I will create a function called complete_order().
# Within my dictionary I want to callout a specific order.
# Once I have the order I've choosen, I want mark it as a complete order
# I will use a boolean value as a distinction for a completed order. 
# I will use the boolean value --True.
# I am going to add a new key value pair to completed_order with a value of --True.
# I will use a print statement to show the new key value of --completed_order: True. 

def complete_order(shipping_details):
    shipping_details[1]['completed_order'] = True  
shipping_details[1]['completed_order'] = True  
print(shipping_details[1]) 

print()