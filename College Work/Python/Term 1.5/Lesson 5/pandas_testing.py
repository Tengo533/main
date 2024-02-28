import datetime
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

df = pd.read_csv(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 5\Task_4a_data.csv', index_col='ID')

#main menu
def menu():
    print("\t\t****MAIN MENU****")
    print('1) Enter sales records')
    print('2) Run reports')
    x = int(input(""))
    return x

#reports menu
def menu2():
    print("**** Reports Dashboard ****")
    print("1. Individual Employee Report")
    print("2. Sales By Region Report")
    print("3. Employees Highest Sales")
    x = int(input(""))
    return x




def ind_emp_check(df_r, id, date1, date2):
    df_r = df_r.loc[df.index == id]

    df_r = df_r.T[3:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    date1 = pd.to_datetime(date1, format='%d/%m/%Y')
    date2 = pd.to_datetime(date2, format='%d/%m/%Y')
    mask = (df_r['ID1'] >= date1) & (df_r['ID1'] <= date2)
    df_search = df_r.loc[mask]
    print(df_search)
    print('Total by id = {} is {}'.format(id, sum(df_search[id])))

    plt.bar(df_search['index'], df_search[id])
    plt.xticks(rotation=90)
    plt.show()



def sales_by_region_report(region, s_date, e_date):
    """ Function to display sales by region for a date range """

    print(f"In sales by region report: region={region} , start={s_date}, end={e_date}")

    # Read file locally for security 
    df_r = pd.read_csv(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 5\Task_4a_data.csv', index_col='ID')
    
    # Filter rows based on region
    region_mask = (df_r['Region'] == region)
    df_region = df_r.loc[region_mask]

    #print(df_region)

    # Transpose - cols to rows
    df_r = df_r.T[3:]
    
    # Rebuild index as transposed
    df_r.reset_index(inplace=True)

    # Add new ID1 row which is a date version of the date string column
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')

    # Format date strings to be date objects
    date1 = pd.to_datetime(s_date, format='%d/%m/%Y')
    date2 = pd.to_datetime(e_date, format='%d/%m/%Y')

    # Create mask for date range
    dt_mask = (df_r['ID1'] >= s_date) & (df_r['ID1'] <= e_date)
    # Apply mask and store wanted date range in new df df_dt_rng
    df_dt_rng = df_r.loc[dt_mask]

    # Calculate the sum of sales figure columns    
    df_dt_rng["SumSales"] = df_dt_rng.iloc[:, 1:-2].sum(axis=1)

    # Create a new dataframe just with the data we want, ie date and sales per date
    df_result = df_dt_rng.loc[:, ["index", "SumSales"]]
    print(df_result)

    # Plot data of date vs sales for date range for the specified location
    df_result.plot(x='index', y='SumSales', kind='bar')
    plt.xticks(rotation=90)
    plt.show()


def employees_highest_sales(s_date, e_date):
    print("In employees highest sales fn") 

    # Read file locally for security 
    df = pd.read_csv(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 5\Task_4a_data.csv', index_col='ID')

    # drop date cols before start col
    start_date_col_idx = df.columns.get_loc(s_date)
    pre_start_date_cols_to_remove = df.columns[3:start_date_col_idx]
    df = df.drop(columns=pre_start_date_cols_to_remove)

    # drop date cols after end col
    end_date_col_idx = df.columns.get_loc(e_date)
    post_end_date_cols_to_remove = df.columns[end_date_col_idx+1:]
    df = df.drop(columns=post_end_date_cols_to_remove)

    # Calc total sales for each salesperson and store in new SumSales column
    df["TotalSales"] = df.iloc[:, 3:].sum(axis=1)
    print(df)

    # Sort salespersons based on total sales
    sorted_df = df.sort_values(by='TotalSales', ascending=False)

    # Just take top 10 salespersons
    top_10_df = sorted_df.head(10).copy()

    print("Top 10 Salespersons")
    print(top_10_df)
  
    # Plot of top 10 salespersons vs total sales for date range
    top_10_df['TotalSales'].plot(kind='bar')
    plt.xlabel('Sales Person ID')  # Label for the x-axis
    plt.ylabel('Total Sales')      # Label for the y-axis
    plt.title('Top 10 Salesperson Sales')
    plt.xticks(rotation=45)
    plt.show()



y = menu()
while y == 1 or y == 2:
    if y == 1:
        try:
            ID = int(input("Enter the Staff ID "))
            if ID not in df.index.values:
                print('yes')

            date1 = input("Enter Date in dd/mm/yy: ")
            day, month, year = date1.split("/")
            date1 = datetime.date(int(year), int(month), int(day))

            if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
                    dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
                print("Date is in the future")
            else:
                cost = float(input("Enter the cost : "))
                df.loc[ID, date1.strftime('%d/%m/%Y')] = cost
            # df.to_csv('test2.csv')
        except:
            print("\n\nError Occurred Please try again\n\n")
            y = menu()

    if y == 2:
        x = menu2()
        if x == 1:
            try:
                id = int(input("Enter the Employee Id : "))
                s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                day, month, year = s_date.split("/")
                s_date = datetime.date(int(year), int(month), int(day))

                e_date = input("Enter Date in dd/mm/yyyy: ")
                day, month, year = e_date.split("/")
                e_date = datetime.date(int(year), int(month), int(day))

                s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                ind_emp_check(df, id, s_date, e_date)
            except:
                print("\n\nError Occurred Please try again\n\n")
                x = menu2()
        elif x == 2:
            try:
                region = (input("Enter the Region : "))

                s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                day, month, year = s_date.split("/")
                s_date = datetime.date(int(year), int(month), int(day))

                e_date = input("Enter End Date in dd/mm/yyyy: ")
                day, month, year = e_date.split("/")
                e_date = datetime.date(int(year), int(month), int(day))

                s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                
                sales_by_region_report(region, s_date, e_date)
            except:
                print("\n\nError Occurred Please try again\n\n")
                x = menu2()


        elif x == 3:
            s_date = input("Enter Starting Date in dd/mm/yyyy: ")
            #day, month, year = s_date.split("/")
            #s_date = datetime.date(int(year), int(month), int(day))

            e_date = input("Enter End Date in dd/mm/yyyy: ")
            #day, month, year = e_date.split("/")
            #e_date = datetime.date(int(year), int(month), int(day))

            #s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            #e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            
            employees_highest_sales(s_date, e_date) 
        else:
            x = menu2()
    else:
        x = menu()
    x = menu()