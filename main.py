#import dependencies
import os
import time
from time import localtime, strftime

#init cust. class
class cust:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.ph_number = ""
        self.pizza_number = ""
        self.pizzas = []
        self.price = 0
        self.delivery = None

#Pizza menu.  Each index for a given pizza and it's price 
PIZZAS = ["Cheese", "Pepperoni", "Hawaiian", "Veggie", "Beef & Onion", "Garlic Cheese", "Ham & Cheese", "Butter Chicken", "Shrimp", "Meatlovers", "Apricot Chicken", "Supreme"]
PIZZA_PRICES = [10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 15.5, 15.5, 15.5, 15.5, 15.5]
DELIVERY_COST = 3
#main function to printout.  Integer input for state of program to print out specific page -
    #pre deliv/pickup   = 1
    #cust. info input   = 2
    #confirm order      = 3
    #display order      = 4

#display related variables
SEPERATOR = "***********************************************************************"

def print_out(x):
    screenlines = len(PIZZAS) + 31
    os.system("mode con: cols=71 lines="+str(screenlines))
    os.system("cls")
    if x == 1: 				#prints out title, customer info, and current pizzas ordered
        title()
        blank_line(1)
        cust_info()
        blank_line(1)
        print(SEPERATOR)
        current_pizzas()
        print(SEPERATOR)
        
    elif x == 2:            #prints out all in print_out(1) and available pizzas on menu
        title()
        blank_line(1)
        cust_info()
        blank_line(1)
        print(SEPERATOR)
        current_pizzas()
        print(SEPERATOR)
        print("Available pizzas:")
        for i in range(len(PIZZAS)):
            print("{}: ${} : {}".format(i+1, PIZZA_PRICES[i], PIZZAS[i]))
        print(SEPERATOR)

    elif x == 3:
        title()             #prints out order summary
        print("ORDER:\n")
        cust_info()
        blank_line(2)
        i = 0
        for i  in range(len(cust.pizzas)):
            print("{} ${}".format(cust.pizzas[i], PIZZA_PRICES[PIZZAS.index(cust.pizzas[i])]))
        if cust.delivery == True:
            print("Delivery $3")
        print("TOTAL= ${}".format(cust.price))
        print(SEPERATOR)

    else:                   #if print_out() argument is invalid.  Only used for debugging as no dynamic values are input into this.
        print("Output error in printout(). Halting...")
        exit()
            
#functions used in printout() to simplify process
#prints out program title
def title():
    print(SEPERATOR)
    print("********************* Pizza Order Management v1.0 *********************")
    print(SEPERATOR) 

#prints x blank lines
def blank_line(x):
    for i in range(x):
        print("")

#prints out relevant cust class variables
def cust_info():
    FLATSEPERATOR = "-----------------------------------------------------------------------"
    print(FLATSEPERATOR)
    print("Customer name                  | ", end="")
    if cust.name != "":
        print(cust.name)
    else:
        print("")
        
    
    
    print(FLATSEPERATOR)
    print("Total number of pizzas ordered | ", end="")
    if cust.pizza_number != None:
        print(cust.pizza_number)
    else:
        print("")
        
    print(FLATSEPERATOR)    
    print("Total order cost               | $", end="")
    print(cust.price)
    
    print(FLATSEPERATOR)
    if cust.delivery == True:
        print("Customer address               | ", end="")
        if cust.address != "":
            print(cust.address)
        else:
            print("")
        print(FLATSEPERATOR)
        
        print("Customer phone number          | ", end="")
        if cust.ph_number != None:
            print(cust.ph_number)
        else:
            print("")
        print(FLATSEPERATOR)
    else:
        blank_line(4)

#prints out pizzas in cust's order
def current_pizzas():
    pizzaLines = 5
    print("Current Pizzas:\n")
    for i in range(len(cust.pizzas)):
        print(cust.pizzas[i])
        pizzaLines += -1
    blank_line(pizzaLines)

#appends ordinal numbers for numbers 1-5
def ordinal(x):
    suffix = ["st", "nd", "rd", "th", "th"]
    val = str(x) + "{}".format(suffix[x-1])
    return val

#input functions.  All include relevant error trapping
def delivery_query():
    while True:
        cust_input = input("Is this order for delivery? (y/n) >")
        if cust_input.lower() == "y" or cust_input.lower() == "n":
            if cust_input.lower() == "y":
                cust.price += DELIVERY_COST
                return True
            else:
                return False
        print_out(1)
        print("Wrong input, try again")

def confirm_query():
    while True:
        cust_input = input("Do you want to confirm this order? (y/n) >")
        if cust_input.lower() == "y" or cust_input.lower() == "n":
            if cust_input.lower() == "y":
                return True
            else:
                return False
        print_out(3)
        print("Wrong input, try again")

def order_size_query():
    while True:
        try:
            cust_input = int(input("How many pizzas is the customer ordering? (max 5) >").strip())
            if cust_input > 0 and cust_input < 6:
                return cust_input
            print_out(1)
            print("Wrong input, try again")
        except:
            print_out(1)
            print("That's not a valid number.  Try again.")

def pizza_query():
    i = 0
    while i < cust.pizza_number:
        try:
            cust_input = int(input("What is the {} pizza the customer is ordering? >".format(ordinal(i+1))))
            if cust_input > 0 and cust_input < 13:
                i += 1
                cust.pizzas.append(PIZZAS[cust_input-1])
                cust.price += PIZZA_PRICES[cust_input-1]
                print_out(2)
            else:
                print_out(2)
                print("Wrong input, try again")
        except:
            print_out(2)
            print("That's not a valid number.  Try again.")



#***********************MAIN PROCESS***********************

#init cust class as cust
cust = cust()

#main loop to enable multiple entries
while True:
    print_out(1)                                                         #Get cust. information
    cust.delivery = delivery_query()    
    
    print_out(1)
    cust.name = input("What is the customer's name? >")
    
    print_out(1)
    if cust.delivery == True:
        cust.address = input("What is the customer's address? >")
        
        print_out(1)
        cust.ph_number = input("What is the customer's phone number? >")

        print_out(1)
                                                                        #Start query for # of pizzas, types of pizzas etc.
    cust.pizza_number = order_size_query()
    
    print_out(2)
    pizza_query()
    
    print_out(3)                                                        #Confirm order?
    validate = confirm_query()
    print_out(3)                                                        #Show order, output to a text file if validate = true
    if validate == True:
        print("ORDER CONFIRMED")
        filename = "dockets/"+strftime("%Y-%m-%d_%H.%M", localtime())+".txt"
        if cust.ph_number == None:
            cust.ph_number = ""
            cust.address = ""
        docket = open(filename,"w")
        docket.write(cust.name + "\n" + cust.address + "\n" + cust.ph_number + "\n\n")
        i = 0
        for i  in range(len(cust.pizzas)):
            docket.write("{} ${}\n".format(cust.pizzas[i], PIZZA_PRICES[PIZZAS.index(cust.pizzas[i])]))
        if cust.delivery == True:
            docket.write("Delivery $3 \n\n")
        docket.write("TOTAL= " + str(cust.price) + "\n")
        
        docket.close()
        
    else:
        print("ORDER CLEARED")
     
    cust.__init__()                                                      #reset cust. variables
    time.sleep(3)