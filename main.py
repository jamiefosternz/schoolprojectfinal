#import dependencies
import os
import time

#init global cust. variables
cust_name = ""
cust_address = ""
cust_ph_number = None 
cust_pizza_number = None

order_cost = 0

#constant variables
pizzas = ["Cheese", "Pepperoni", "Hawaiian", "Veggie", "Beef & Onion", "Garlic Cheese", "Ham & Cheese", "Butter Chicken", "Shrimp", "Meatlovers", "Apricot Chicken", "Supreme"]
pizza_prices = [10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 15.5, 15.5, 15.5, 15.5, 15.5]


#display related variables
seperator = "*********************************************************"



#main function to printout.  Integer input for state of program to print out specific page -
	#pre deliv/pickup   = 1
	#cust. info input	= 2
	#confirm order		= 3
	#display order 		= 4

def printout(x):
	os.system("cls")
	if x == 1:
		title()
		blankline(2)
		custInfo()
		blankline(1)
		print(seperator)
	elif x == 2:
		title()
	elif x == 3:
		title()
	elif x == 4:
		title()
	else:
		print("Output error in printout(). Halting...")
		exit()
			
#functions used in printout() to simplify process
def title():
	print(seperator)
	print("************** Pizza Order Management v1.0 **************")
	print(seperator) 

def blankline(x):
	for i in range(x):
		print("")

def custInfo():
	print("Customer name: ", end="")
	if cust_name != "":
		print(cust_name)
	else:
		print("")
	
	print("Customer address: ", end="")
	if cust_address != "":
		print(cust_address)
	else:
		print("")
	
	print("Customer phone number: ", end="")
	if cust_ph_number != None:
		print(cust_ph_number)
	else:
		print("")
	
	print("Total number of pizzas ordered: ", end="")
	if cust_pizza_number != None:
		print(cust_pizza_number)
	else:
		print("")
		
	print("Total order cost: $", end="")
	print(order_cost)





while True:
	printout(1)
	time.sleep(1)