import pandas as pd
import matplotlib.pyplot as plt
import datetime


def profit_loss_menu():
    """
    Simple menu outputted to the console which allows the user to decide what data they would like to see.
    Uses try except to catch any user error.
    """
    flag = True
    
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show profit/loss for specific products")
        print("2. Show profit/loss for all products")
        print("3. Get total amount of product sold by a supplier")
        print("4. Profit on products sold from different suppliers")
        print("###############################################")

        profit_loss_choice = input("Please enter the number of your choice (1-4): ")

        try:
            int(profit_loss_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 4:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return int(profit_loss_choice) 




def get_product_choice():
    """
    Prints the list of all products within the CSV and returns the chosen product back to the profit/loss calculation function.
    """
    flag = True

    while flag:
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")
        print("1.  Potatoes")
        print("2.  Carrots")
        print("3.  Peas")
        print("4.  Lettuce")
        print("6.  Apples")
        print("5.  Onions")
        print("7.  Oranges")
        print("8.  Pears")
        print("9.  Lemons")
        print("10. Limes")
        print("11. Melons")
        print("12. Cabbages")
        print("13. Asparagus")
        print("14. Broccoli")
        print("15. Cauliflower")
        print("16. Celery")
        print("######################################################")

        product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]
        # Catches user errors if a product is not selected properly.

        product_choice = input("Please enter the number of your choice (1-16): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name
            

def profit_product_supplier():
    """
    Calculates how much each product profited from an inputted supplier.
    """
    with pd.option_context("mode.chained_assignment", None): # with statement used with option_context to avoid chain error, reverts after function has ran.
        df = pd.read_csv("Term 2\Pandas_Dictionary\Pandas_Task4\Task4a_data.csv")
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
        suppliers = []
        # Get individual supplier names
        for supplier in df["Supplier"]:
            if supplier not in suppliers:
                suppliers.append(supplier)
        suppliers_str = ", ".join(suppliers)
        print(f"Suppliers: {suppliers_str}")
        while True:
            # Request for user input then catch any user errors
            supplier = input("Input Supplier: ")
            if supplier == "Quit":
                break
            elif supplier not in suppliers:
                print("Please input an avaliable supplier.")
            else:
                # Sort by Supplier
                df_new = df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date) & (df["Supplier"] == supplier)].copy()
                # Create new column(s) to find profit
                df_new["Cost Subtotal"] = df["KGs Purchased"] * df["Purchase Price"]
                df_new["Sales Subtotal"] = df["KGs Sold"] * df["Selling Price"]
                df_new["Profit"] = df_new["Sales Subtotal"] - df_new["Cost Subtotal"]
                product_list = []
                total = []
                # Find each type of product
                for product in df_new["Product"]:
                    if product not in product_list:
                        product_list.append(product)
                # Sort by product, calculate the total profit, then append the result to a list
                for product in product_list:
                    df_temp = df_new.loc[df_new["Product"] == product]
                    result = df_temp["Profit"].sum()
                    total.append(result)
                    
                
                # Plot the graph showing the profit per product for the inputted supplier.
                x = product_list
                y = total
                plt.figure(figsize=(16,8))
                plt.bar(x,y)
                plt.axhline(y=0, color="r",linestyle="-")
                plt.xlabel("Product")
                plt.ylabel("Total Profit")
                plt.title(f"Total product profit from {supplier}")
                plt.show()
                print("Type 'Quit' in input to stop the program.")
                



def get_supplier_products():
    """
        Function that takes a user inputted supplier and calculates the amount of total KGs they supplied, then displayed as a graph.
    """
    df = pd.read_csv("Term 2\Pandas_Dictionary\Pandas_Task4\Task4a_data.csv")
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    suppliers = []
    for supplier in df["Supplier"]:
        if supplier not in suppliers:
            suppliers.append(supplier)
    suppliers_str = ", ".join(suppliers)
    print(f"Suppliers: {suppliers_str}")
    while True:
        supplier = input("Input Supplier, or type 'Quit' to stop: ")
        if supplier == "Quit":
            break
        elif supplier not in suppliers:
            print("Please input an avaliable supplier.")
        else:
            df_supplier = df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date) & (df["Supplier"] == supplier)].copy()
            result = df_supplier["KGs Purchased"].sum()
            print(f"The total amount of KGs supplied from {supplier} was {result}")
            x = df_supplier["Date"]
            y = df_supplier["KGs Purchased"]
            plt.figure(figsize=(16,8))
            plt.bar(x,y)
            plt.xlabel("Date")
            plt.ylabel("KGs Supplied")
            plt.title(f"{supplier} KGs supplied over {start_date} to {end_date}")
            plt.show()


def get_start_date():
    """
    Function used to find the dates in which the user wishes to search for, 
    catches any user error if the dates are inputted incorrectly.
    """
    print("The date ranges from 01/01/2021 to 31/03/2021")
    while True:
        try:
            df = pd.read_csv("Term 2\Pandas_Dictionary\Pandas_Task4\Task4a_data.csv")
            flag = True
            # Get the min date and the max date in the csv file
            date_min = df.Date.min()
            date_max = df.Date.max()
            while flag:
                start_date = input('Plese enter start date for your time range (DD/MM/YYYY): ')
                # Catch user error if the date inputted is not in range.
                if pd.to_datetime(start_date, dayfirst=True) >= pd.to_datetime(date_min, dayfirst=True) and pd.to_datetime(start_date, dayfirst=True) <= pd.to_datetime(date_max, dayfirst=True):
                    try:
                        pd.to_datetime(start_date, dayfirst=True)
                    except:
                        print("Sorry, you did not enter a valid date")
                        flag = True
                    else:
                        return pd.to_datetime(start_date, dayfirst=True)
                else:
                    print("Date not in range.")
        except:
            print("Error: Incorrect Date")


def get_end_date():
    """
    Same as the "get_start_date" fuction, but instead we are finding the end date.
    """
    while True:
        try:
            df = pd.read_csv("Term 2\Pandas_Dictionary\Pandas_Task4\Task4a_data.csv")    
            flag = True
            date_min = df.Date.min()
            date_max = df.Date.max()
            while flag:
                end_date = input('Plese enter end date for your time range (DD/MM/YYYY): ')
                if pd.to_datetime(end_date, dayfirst=True) >= pd.to_datetime(date_min, dayfirst=True) and pd.to_datetime(end_date, dayfirst=True)  <= pd.to_datetime(date_max, dayfirst=True):
                    try:
                        pd.to_datetime(end_date, dayfirst=True)
                    except:
                        print("Sorry, you did not enter a valid date")
                        flag = True
                    else:
                        return pd.to_datetime(end_date, dayfirst=True)
                else:
                    print("Date not in range.")
        except:
            print("Error: Incorrect Date")


def get_date_range_all():
    df1 = pd.read_csv("Term 2\Pandas_Dictionary\Pandas_Task4\Task4a_data.csv") 

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    results_print = results.to_string(index=False)
    print(results_print)
    print(f"The overall profit/loss for the selected time frame was £{round(total,2)}")
    display_graph_all(df1,start_date,end_date)


def display_graph_all(df1,start_date,end_date):
    product_list = []
    total_profit = []
    for product in df1.Product:
        if product not in product_list:
            product_list.append(product)
    with pd.option_context("mode.chained_assignment", None):
        for product in product_list:
            df_new = df1.loc[df1["Product"]==product]
            df_new["Total Sold"] = df_new["KGs Sold"] * df_new["Selling Price"]
            df_new["Total Cost"] = df_new["KGs Purchased"] * df_new["Purchase Price"]
            df_new["Profit"] = df_new["Total Sold"] - df_new["Total Cost"]
            total_profit.append(df_new.Profit.sum())
        x = product_list
        y = total_profit
        plt.figure(figsize=(16,8))
        plt.bar(x,y)
        plt.xlabel("Product")
        plt.ylabel("Total Profit")
        plt.title(f"Total Profit per product between {start_date} and {end_date}")
        plt.show()
        

def get_date_range_product():
    """
    Calculates the total profit/loss from a selected product over the selected timeframe.
    """
    product_name = get_product_choice()
    df2 = pd.read_csv("Term 2\Pandas_Dictionary\Pandas_Task4\Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)
   
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    results_print = product_results.to_string(index=False)
    
    print(results_print)
    print("The profit/loss for the {} for selected time frame was £{}".format(product_name, total))
    product_graph_display(product_results)


def product_graph_display(product_results):
    """
    Produces a graph for the single product profit/loss
    """

    x = product_results["Date"]
    y = product_results["Profit subtotal"]
    plt.figure(figsize=(16,8))
    plt.bar(x,y)
    plt.axhline(y=0, color="r",linestyle="-")
    plt.xlabel("Date over time")
    plt.ylabel("Profit per day")
    plt.title("Profit over time")
    plt.show()


def process_menu_choice():
    # After getting user choice, the appropriate function is called.
    if profit_choice == 1:
        get_date_range_product()
    elif profit_choice == 2:
        get_date_range_all()
    elif profit_choice == 3:
        get_supplier_products()
    else:
        profit_product_supplier()


start_date = get_start_date()
end_date = get_end_date()
profit_choice = profit_loss_menu()
process_menu_choice()


while True:
    choice = input("Continue?(y/n): ")
    if choice == "y":
        profit_choice = profit_loss_menu()
        process_menu_choice()
    elif choice == "n":
        break
    else:
        print("Incorrect value, please input y or n.")


