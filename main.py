#import dependencies
import os
import time

#init global cust. variables
cust_name = ""
cust_address = ""
cust_ph_number = None 
cust_pizza_number = None
cust_pizzas = []
order_cost = 0
cust_delivery = None

#constant variables
pizzas = ["Cheese", "Pepperoni", "Hawaiian", "Veggie", "Beef & Onion", "Garlic Cheese", "Ham & Cheese", "Butter Chicken", "Shrimp", "Meatlovers", "Apricot Chicken", "Supreme"]
pizza_prices = [10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 15.5, 15.5, 15.5, 15.5, 15.5]


#display related variables
seperator = "***********************************************************************"
flatSeperator = "-----------------------------------------------------------------------"
pizzaLines = 5



#main function to printout.  Integer input for state of program to print out specific page -
	#pre deliv/pickup   = 1
	#cust. info input	= 2
	#confirm order		= 3
	#display order 		= 4
	
def printOut(x):
	os.system("cls")
	if x == 1:
		title()
		blankLine(1)
		custInfo()
		blankLine(1)
		print(seperator)
		currentPizzas()
		print(seperator)
		
	elif x == 2:
		title()
		blankLine(1)
		custInfo()
		blankLine(1)
		print(seperator)
		currentPizzas()
		print(seperator)
		print("Available pizzas:")
		for i in range(len(pizzas)):
			print("{}: {}".format(i+1, pizzas[i]))
		print(seperator)
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
	print("********************* Pizza Order Management v1.0 *********************")
	print(seperator) 

def blankLine(x):
	for i in range(x):
		print("")

def custInfo():
	print(flatSeperator)
	print("Customer name                  | ", end="")
	if cust_name != "":
		print(cust_name)
	else:
		print("")
		
	
	
	print(flatSeperator)
	print("Total number of pizzas ordered | ", end="")
	if cust_pizza_number != None:
		print(cust_pizza_number)
	else:
		print("")
		
	print(flatSeperator)	
	print("Total order cost               | $", end="")
	print(order_cost)
	
	print(flatSeperator)
	if cust_delivery == True:
		print("Customer address               | ", end="")
		if cust_address != "":
			print(cust_address)
		else:
			print("")
		print(flatSeperator)
		
		print("Customer phone number          | ", end="")
		if cust_ph_number != None:
			print(cust_ph_number)
		else:
			print("")
		print(flatSeperator)
	else:
		blankLine(4)

def currentPizzas():
	print("Current Pizzas:")
	for i in range(len(cust_pizzas)):
		print(cust_pizzas[i])
		pizzalines += -1
	blankLine(pizzaLines)
	
#input functions
def deliveryQuery():
	while True:
		cust_input = input("Is this order for delivery? (y/n) >")
		if cust_input.lower() == "y" or cust_input.lower() == "n":
			if cust_input.lower() == "y":
				return True
			else:
				return False
		printOut(1)
		print("Wrong input, try again")

def orderSizeQuery():
	while True:
		try:
			cust_input = int(input("How many pizzas is the customer ordering? (max 5) >"))
			if cust_input > 0 and cust_input < 6:
				return cust_input
			printOut(1)
			print("Wrong input, try again")
		except:
			printOut(1)
			print("That's not a valid number.  Try again.")

while True:
	printOut(1)
	cust_delivery = deliveryQuery()
	
	printOut(1)
	cust_name = input("What is the customer's name? >")
	
	printOut(1)
	if cust_delivery == True:
		cust_address = input("What is the customer's address? >")
		
		printOut(1)
		cust_ph_number = input("What is the customer's phone number? >")

		printOut(1)
	
	cust_pizza_number = orderSizeQuery()
	
	printOut(2)
	time.sleep(1)