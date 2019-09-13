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

#Pizza menu.  each index for a given pizza and it's price 
pizzas = ["Cheese", "Pepperoni", "Hawaiian", "Veggie", "Beef & Onion", "Garlic Cheese", "Ham & Cheese", "Butter Chicken", "Shrimp", "Meatlovers", "Apricot Chicken", "Supreme"]
pizza_prices = [10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 15.5, 15.5, 15.5, 15.5, 15.5]


#display related variables
seperator = "***********************************************************************"




#main function to printout.  Integer input for state of program to print out specific page -
    #pre deliv/pickup   = 1
    #cust. info input   = 2
    #confirm order      = 3
    #display order      = 4
    
def printOut(x):
    screenlines = len(pizzas) + 31
    os.system("mode con: cols=71 lines="+str(screenlines))
    os.system("cls")
    if x == 1: 				#prints out title, customer info, and current pizzas ordered
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
        print("ORDER:\n")
        custInfo()
        blankLine(2)
        i = 0
        for i  in range(len(cust.pizzas)):
            print("{} ${}".format(cust.pizzas[i], pizza_prices[pizzas.index(cust.pizzas[i])]))
        if cust.delivery == True:
            print("Delivery $3")
        print("TOTAL= ${}".format(cust.price))
        print(seperator)
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
    flatSeperator = "-----------------------------------------------------------------------"
    print(flatSeperator)
    print("Customer name                  | ", end="")
    if cust.name != "":
        print(cust.name)
    else:
        print("")
        
    
    
    print(flatSeperator)
    print("Total number of pizzas ordered | ", end="")
    if cust.pizza_number != None:
        print(cust.pizza_number)
    else:
        print("")
        
    print(flatSeperator)    
    print("Total order cost               | $", end="")
    print(cust.price)
    
    print(flatSeperator)
    if cust.delivery == True:
        print("Customer address               | ", end="")
        if cust.address != "":
            print(cust.address)
        else:
            print("")
        print(flatSeperator)
        
        print("Customer phone number          | ", end="")
        if cust.ph_number != None:
            print(cust.ph_number)
        else:
            print("")
        print(flatSeperator)
    else:
        blankLine(4)

def currentPizzas():
    pizzaLines = 5
    print("Current Pizzas:\n")
    for i in range(len(cust.pizzas)):
        print(cust.pizzas[i])
        pizzaLines += -1
    blankLine(pizzaLines)

#appends ordinal numbers for numbers 1-5
def ordinal(x):
    suffix = ["st", "nd", "rd", "th", "th"]
    val = str(x) + "{}".format(suffix[x-1])
    return val

#input functions
def deliveryQuery():
    while True:
        cust_input = input("Is this order for delivery? (y/n) >")
        if cust_input.lower() == "y" or cust_input.lower() == "n":
            if cust_input.lower() == "y":
                cust.price += 3
                return True
            else:
                return False
        printOut(1)
        print("Wrong input, try again")

def confirmQuery():
    while True:
        cust_input = input("Do you want to confirm this order? (y/n) >")
        if cust_input.lower() == "y" or cust_input.lower() == "n":
            if cust_input.lower() == "y":
                return True
            else:
                return False
        printOut(3)
        print("Wrong input, try again")

def orderSizeQuery():
    while True:
        try:
            cust_input = int(input("How many pizzas is the customer ordering? (max 5) >").strip())
            if cust_input > 0 and cust_input < 6:
                return cust_input
            printOut(1)
            print("Wrong input, try again")
        except:
            printOut(1)
            print("That's not a valid number.  Try again.")

def pizzaQuery():
    i = 0
    while i < cust.pizza_number:
        try:
            cust_input = int(input("What is the {} pizza the customer is ordering? >".format(ordinal(i+1))))
            if cust_input > 0 and cust_input < 13:
                i += 1
                cust.pizzas.append(pizzas[cust_input-1])
                cust.price += pizza_prices[cust_input-1]
                printOut(2)
            else:
                printOut(2)
                print("Wrong input, try again")
        except:
            printOut(2)
            print("That's not a valid number.  Try again.")



#***********************MAIN PROCESS***********************
cust = cust()
while True:
    printOut(1)
    cust.delivery = deliveryQuery()
    
    printOut(1)
    cust.name = input("What is the customer's name? >")
    
    printOut(1)
    if cust.delivery == True:
        cust.address = input("What is the customer's address? >")
        
        printOut(1)
        cust.ph_number = input("What is the customer's phone number? >")

        printOut(1)
    
    cust.pizza_number = orderSizeQuery()
    
    printOut(2)
    pizzaQuery()
    
    printOut(3)
    validate = confirmQuery()
    printOut(3)
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
            docket.write("{} ${}\n".format(cust.pizzas[i], pizza_prices[pizzas.index(cust.pizzas[i])]))
        if cust.delivery == True:
            docket.write("Delivery $3 \n\n")
        docket.write("TOTAL= " + str(cust.price) + "\n")
        
        docket.close()
        
    else:
        print("ORDER CLEARED")
     
    cust.__init__()
    time.sleep(3)