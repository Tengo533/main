from datetime import datetime

# Products customer can choose to buy
products = [['Desktop', 799.00, 5], ['Laptop A', 1200.00, 6]]  

# Keeps track of all sales 
# - 2D list with each row representing a sale
# - last row is latest sale
sales = []


def stock_check():
    """Display all products for sale"""

    print("\nSTOCK INVENTORY")
    print("[Type, Cost, stock]")
    for i in products:                 #FIX replaced { with :
        print(i)
    print("\n")



def add_stock():
    """ Add inventory to stock"""
    data = []

    # Enter product and price
    stock_type = input("Enter product name: ").capitalize()
    check = False  
    while not check:   # note: nasty 'not False' logic 
        try:
            cost1 = float(input("Enter Product cost up to 2 Decimal Places: "))
            cost = round(cost1, 2)
            check = True
        except:
            print("Entered value is not in required format.")

    # Enter qty of product
    check_1 = False            #FIX True should be False as per example above  
    while not check_1:
        try:
            stock = int(input("Enter the amount of stock: "))
            check_1 = True
        except:
            print("Entered value is not in required format.")

    data.append(stock_type)
    data.append(cost)
    data.append(stock)

    # Add new product to global products list
    products.append(data)


def addition():
    """Checks if product exists to buy and that 
    there is enough quantity to cover what buyer requested"""
    
    s_check = False
    q_check = False
    data1 = []
    while not s_check:
        s_type = input("Enter the Stock Type which you want to buy: ")

        # Loop over products to identiy if product the user entered exists 
        # nb: products list format is 0=product_name, 1=price, 2=qty 
        for i in products:
            # Check if product exists
            if s_type.lower() == i[0].lower():       #FIX index 0 not 1 for product name
                s_check = True
                
                # If product exists then ask user to entry qty 
                while not q_check:
                    s_quantity = int(input("Enter the quantity for %s which you want to buy: " % s_type))
                    # If user entered qty greater than inventory then print info and ask for qty again 
                    if s_quantity > i[2]:
                        print("Max available stock is: %s" % str(i[2]))
                    else:
                        i[2] = i[2] - s_quantity
                        q_check = True
                        break

        # If loop completes without product being found then flag doesnt exist    
        if s_check == False:
            print("Entered stock does not exist")

        # If loop completes and product is found and qty is sufficient then add stock to returned data1 list
        # nb: note price has not been added into returned data1 value    
        if (s_check == True and q_check == True):
            data1.append(s_type)
            data1.append(s_quantity)
            break

    return data1



def price(value):
    """ Returns the value (price*qty) of the passed in order.
        An order [name, qty] is passed in and its name compared to 
        all products in the products list. if there is a match
        then the order qty (value[1]) is multiplied by the price (i[1]) listed in products"""
    
    for i in products:
        if value[0].lower() == i[0].lower():
            cost = value[1] * i[1]  
            break
    return cost



def record_sale():
    """Enter a sale (option 3)"""

    data = []
    
    # Get customer and company details
    c_name = input("Enter Customer Name: ")
    comp_name = input("Enter Company Name: ")
    data.append(c_name)
    data.append(comp_name)
    
    # Get current date
    now = datetime.now()  
    date_time = now.strftime("%d%m%Y")          #FIX1 add missing trailing ", FIX2 fix string format
    data.append(date_time)
    
    # Display all products for sale
    print("Stock products are shown below")
    stock_check()

    # Get customer's order for first product (note: only product name and qty returned)
    data.append(addition())
    
    # Loop for any additional orders customer wishes to place
    while True:
        opt = input("Add more products? press y or n: ")
        if opt.lower() == "y":
            data.append(addition())
        elif opt.lower() == "n":
            break
        else:
            print("invalid option")

    # Variable to track total qty ordered
    sum = 0
    # Variable to hold value (price*qty) across all entered orders
    sub_total = 0

    # Loop over data list to locate the product entries as identified by
    # its type being a list, ie. addition() adds [product, qty] sublists
    for j in data:
        if isinstance(j, list):               # check if entry in data has type 'list'
            sum = sum + int(j[1])             # track total qty across all orders
            sub_total = sub_total + price(j)  # track total value (price*qty) across all orders

    # Add value (price*qty) to data
    data.append( round(sub_total, 2) )        #FIX round value to 2dp, i.e. pounds and pence

    # If total qty of ordered products is greater than 5 then apply 5% discount
    if sum >= 5:
        discount = sub_total * 0.05           #FIX - 5% is 0.05 not /5 * 100
        final_total = sub_total - discount  
    else:
        discount = 0
        final_total = sub_total

    data.append( round(discount, 2) )         #FIX round value to 2dp                 
    data.append( round(final_total, 2) )      #FIX round value to 2dp             

    sales.append(data)
    
    # Checking record structure
    # print(f"Sales Record = {sales}")
    # sales example  [['cust', 'comp', 'DDMMYYY', ['Desktop', 4], ['Laptop A', 3], 6796.0, 339.8, 6456.2]]

    # FIX
    # sales can hold a variable number of products hence cannot simply print.
    # Instead printing is broken down into three stages:
    # 1. Print initial fixed position values: receipt, customer, company, date
    # 2. Print one or more products
    # 3. Print subtotal, discount, final total 
    print("\n\nCUSTOMER RECEIPT\n  Customer Name: {}\n  Company name: {}\n  Purchase date: {}"
          .format(sales[-1][0], sales[-1][1], sales[-1][2]));

    num_of_products = len(sales[-1]) - 6
    #print(f"Num Products= {num_of_products}")
    for idx in range(num_of_products):
        product_pos_offset = 3 + idx
        print("  Products (Type/Number) : {}".format(sales[-1][product_pos_offset]))
          
    print("  Subtotal: {} \n  Total Minus Discount: {} \n  Final Total: {}\n "
          .format(sales[-1][-3], sales[-1][-2], sales[-1][-1] ))               # use indexing from end of row



#-------------------
# Top level menu
#-------------------
while True:
    try:                                # FIX catch bad input
        option = int(input("\nMENU\nEnter 1 for Stock Check \nEnter 2 for Add stock\nEnter 3 for Record Sale\nEnter 4 to exit\n"))
        if option == 1:                 # FIX == instead of =
            stock_check()
        elif option == 2:               # FIX == instead of =
            add_stock()
        elif option == 3:               # FIX == instead of =
            record_sale()
        elif option == 4:               # FIX == instead of =
            break
        else:
            print("Invalid option, Select between 1 and 4")
    except:
        print("Invalid option, Select number between 1 and 4")