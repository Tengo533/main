import pandas as pd
import matplotlib.pyplot as plt


df_gbl = pd.DataFrame({
"name":["Bill","Liz","Emma","Jane","Ron"],
"region":["East","North","East","South","West"],
"sales":[30,20,90,50,40],
"costs":[20,15,50,40,10]})


def menu():
    print("\n\n****MAIN MENU****")
    print('1) Report Highest Cost')
    print("2) Report Sum of Sales")
    print("3) Report Profits")
    print("4) Records for Region Report")
    print("5) Excessive Costs Report")
    print("6) Plot Sales Report")
    ip = int(input(": "))
    return ip


def process_choice(choice):
    if(choice == 1):
        highest_cost_rpt()
    elif(choice == 2):
        sum_of_sales_rpt()
    elif(choice == 3):
        calc_profits_rpt()
    elif(choice == 4):
        filter_by_region_rpt()
    elif(choice == 5):
        try:
            th_cost = int(input("Threshold Cost: "))
            excessive_costs_rpt(th_cost)
        except:
            print("Please input a number.")
    elif(choice == 6):
        plot_sales_rpt()
    else:
        print("error unknown option")
   
def sum_of_sales_rpt():
    """Rport to print the sum of all the sales"""
    df = df_gbl.copy(deep=True)
    result = df.sales.sum()
    print("Total sum of all sales")
    print(result)

def calc_profits_rpt():
    """Rport to calculate profits and create a new "Profits" column"""
    df = df_gbl.copy(deep=True)
    df["profits"] = df["sales"] - df["costs"]
    print("Total profit")
    print(df)

def filter_by_region_rpt():
    """Rport to filter by region"""
    while True:
        df = df_gbl.copy(deep=True)
        regions = ["North","East","South","West"]
        region_ip = input("Enter region (North, East, South, West): ")
        if region_ip not in regions:
            print("Region not found.")
        else:
            df = df.loc[df["region"] == region_ip]
            print(df)
            break

def excessive_costs_rpt(threshold_cost):
    """Rport to filter by costs greater than the inputed threshold"""
    df = df_gbl.copy(deep=True)
    df = df.loc[df["costs"] > int(threshold_cost)]
    print(df)

def plot_sales_rpt():
    df = df_gbl.copy(deep=True)
    x = df["name"]
    y = df["sales"]
    plt.bar(x,y)
    plt.title("Sales Report")
    plt.xlabel("Names")
    plt.ylabel("Sales")
    plt.show()

def highest_cost_rpt():
    """Rport to print row with highest cost"""
    # Make local copy of dataframe
    df = df_gbl.copy(deep=True)

    df = df.sort_values('costs', ascending=False)
    highest_cost_row = df.iloc[0]

    print("Record With Highest Cost")
    print(highest_cost_row)


def main():
    """Main program"""
    while True:
        choice = menu()
        process_choice(choice)


# Main Program
if __name__ == "__main__":

    main()
