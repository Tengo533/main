import pandas as pd



menu = {[0,0,0,0,0,0],
        [0,0,0,0,0,0]}

df = pd.DataFrame[menu]
print(df)




fruit = 0
muffin = 0
french = 0
french = 0
coffee = 0
tea = 0
fruittotal = 0
muffintotal = 0
frenchtotal = 0
coffeetotal = 0
teatotal = 0
order = 1

def OrderMenu():
    #Displays the avaiable options to order and adds it to the total amount of each item when selected.
    #The section repeats until the user is happy with the order and wishes to proceed
    global fruit
    global muffin
    global french
    global coffee
    global tea
    print("\nMenu\n1. Fruit Smoothie - £3.00\n2. Muffin - £2.00\n3. French Toast - £5.00\n4. Coffee - £2.50\n5. Tea - £1.50\n6. Cancel order\n")
    food = input("Enter the number of your order: ")
    if food == "1":
        fruit = fruit + 1
    elif food == "2":
        muffin = muffin + 1
    elif food == "3":
        french = french + 1
    elif food == "4":
        coffee = coffee + 1
    elif food == "5":
        tea = tea + 1
    elif food == "6":
        print("Order cancelled!\n")
        ResetNumbers()
    else:
        print("Invalid input")
        OrderMenu()
    print("Added to order!")
    itemtotal = fruit + muffin + french + coffee + tea
    print("Currently " + str(itemtotal) + " in order.")
    end = input("Press enter to continue or 1 to proceed to checkout: ")
    if end == "1":
        Totals()
    else:
        OrderMenu()

def Totals():
    #Finds the total cost of each item and displays the amount of items in the order
    #Displays the cost and provides the user with their order number
    #Allows the user to confirm if they wish to make this purchase
    global total
    fruittotal = fruit * 3.00
    muffintotal = muffin * 2.00
    frenchtotal = french * 5.00
    coffeetotal = coffee * 2.50
    teatotal = tea * 1.50
    print("Order number", str(order), "has:")
    if fruit >= 1:
        print("x" + str(fruit) + " Fruit Smoothie")
    if muffin >= 1:
        print("x" + str(muffin) + " Muffin")
    if french >= 1:
        print("x" + str(french) + " French Toast")
    if coffee >= 1:
        print("x" + str(coffee) + " Coffee")
    if tea >= 1:
        print("x" + str(tea) + " Tea")
    total = fruittotal + muffintotal + frenchtotal + coffeetotal + teatotal
    print("The total cost of the order is " + str(total))
    Purchasing()

def Purchasing():
    global order
    finalchoice = input("Do you wish to continue with purchase (Y/N) ")
    if finalchoice == "Y":
        print("Your order number is",  str(order)  + ".\nPlease collect your order at the till.\n")
        order = order + 1
    elif finalchoice == "N":
        print("Order cancelled!\n")
    else:
        print("Invalid Input")
        Purchasing()
    ResetNumbers()


def HelpMenu():
    #Has space to include accessibility options as well as change the language of the program
    option = input("1. Language options\n2. Accessibility options\n3. Return to order screen ")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    else:
        print("Invalid input")
        HelpMenu()

def ResetNumbers():
    global fruit
    global muffin
    global french
    global coffee
    global tea
    french = 0
    tea = 0
    coffee = 0
    muffin = 0
    fruit = 0
    Welcome()

def Welcome():
    #Welcomes the user and gives them the option to access the help menu for accessibility or language options
    print("Welcome to the cafe!")
    choice = input("Press enter to order now or press 1 for help ")
    if choice == "":
        OrderMenu()
    elif choice == "1":
        HelpMenu()
    else:
        print("Invalid input")
        Welcome()
Welcome()