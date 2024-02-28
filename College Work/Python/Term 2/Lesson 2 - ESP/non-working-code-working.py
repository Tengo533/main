import datetime
# Name, Cost
products = [['Cheese', 1], ["Potatoes",1.70], ["Carrots", 1.50], 
["Peas",1.10], ["Lettuce",0.80], ["Onions",1], ["Apples",0.70]]

customers = []

# current implemented discounts
discounts = {
    'staff' : 5,
    'over25': 10,
}

def cast_input_to_int_safely(inp):
    try:
        return int(inp)
    except:
        return cast_input_to_int_safely(input("Please try again, number was not valid"))


def cast_input_to_float_safely(inp):
    try:
        return float(inp)
    except:
        return cast_input_to_float_safely(input("Please try again, decimal was not valid"))



def get_product(name):
    for product in products:
        if product[0].lower() == name.lower(): 
            return product
    return None


def sell_product():
    items = []
    while True:
        item = input("What item would you like to buy (type 'done' to continue to checkout):")
        if item == 'done': 
            break
        else:
            product = get_product(str(item))
            if product is not None:
                item_added = product[:]
                item_added.append(cast_input_to_int_safely(input("Input how many of the item you would like to buy: ")))
                items.append(item_added)
                print("Added item!")
                print("Current basket:" + ', '.join( ('{} ({})'.format(i[0], i[2]) for i in items)))
            else:
                print("Invalid product please type one of the following: " + ', '.join([i[0] for i in products]))
    customer_forename = input("What is the customers forename:").capitalize()
    customer_surname = input("What is the customers surname:").capitalize()
    customer_address = input("What is the customers address:")
    customer_postcode = input("What is the customers postcode:")
    customer_number = input("What is the customers phone number:")

    customers.append([customer_forename, customer_surname, customer_address, customer_postcode,
               customer_number])
    while True:
        employee_discount = input("Is the customer an employee (makes them legible for employee discount)? (Y/N)").lower()
        if employee_discount == "y":
            print("Employee discount: -{}%".format(discounts.get('staff')))
            total -= total * ((100 - discounts.get('staff')) / 100 )
            break
        elif employee_discount == "n":
            break
        else:
            print("Please type Y or N")
    print(items)
    subtotal = sum((i[2] * float(i[1]) for i in items))
    total = subtotal
    print("\n-------RECEIPT-------")
    print("Customer: {} {}".format(customer_forename, customer_surname)) 
    print("Items bought:\n" + '\n'.join( ('{} {} (TOTAL: £{:.2f})'.format(i[2], i[0], float(i[1]) * i[2]) for i in items)))
    print("Subtotal: £{:.2f}".format(subtotal))
    if subtotal > 25: 
        print("Spend over £25 discount: -{}%".format(discounts.get('over25')))

        total = total * ((100 - discounts.get('over25')) / 100 )
    print("Subtotal: £{:.2f}".format(total))

    str_items = ','.join( ('{}({})'.format(i[0], i[2]) for i in items))
    receipt = [datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), customer_forename, customer_surname, customer_address, customer_postcode,
               customer_number, "£" + str(total), str_items]
    time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open(time + ".txt", "a") as file:
        file.write('\n'.join(receipt) + '\n')






menu = {
    "Sell a product": sell_product
}


menu_keys = menu.keys()
while True:
    print("\n------ Main Menu ------")
    for i, description in enumerate(menu_keys):
        print("{}) {}".format(i + 1, description))  # prints and formats into 1) Add product

    choice = cast_input_to_int_safely(input("\nEnter your choice: ")) - 1
    # validation
    upper_bound = len(menu_keys)
    lower_bound = 0

    if choice > upper_bound or choice < lower_bound: #Mistake
        print("\nInvalid choice, please try again.\nEnter a number between {} and {}!".format(lower_bound, upper_bound))
    else:
        operation_name = list(menu_keys)[choice]
        print("\n------ {} ------".format(operation_name))
        try:
            menu[operation_name]()  # executes operation of choice
        except Exception as e:
            print("An error occurred: ")
            print(e)