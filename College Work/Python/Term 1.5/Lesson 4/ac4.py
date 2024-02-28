import datetime
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt

df = pd.read_csv(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 4\Task_4a_data.csv', index_col='ID')

#main menu
def menu():
    print("\t\t****MAIN MENU****")
    print('1) Enter sales records')
    print('2) Run reports')
    print("3) Sales over time")
    x = int(input(""))
    return x

#reports menu
def menu2():
    print("**** Reports Dashboard ****")
    print("1. Individual Employee Report")
    print("2. Sales by Region")
    print("3. Highest Sales by Employee")
    x = int(input(""))
    return x

def sales_by_region(reigon, s_date, e_date):
    print(f"In sales by region {reigon}, start {s_date}, end {e_date}")

    # Read locally for security
    df_r = pd.read_csv(r'Term 2\Lesson 4\Task_4a_data.csv', index_col="ID")
    region_mask =  (df_r['Region'] == reigon)
    df_reigon = df_r.loc[region_mask]
    
    df_r = df_r.T[3:]

    df_r.reset_index(inplace=True)

    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')

    date1 = pd.to_datetime(s_date, format='%d/%m/%Y')
    date2 = pd.to_datetime(e_date, format='%d/%m/%Y')

    dt_mask = (df_r['ID1'] >= s_date) & (df_r['ID1'] <= e_date)
    

def highest_sales_employee(s_date, e_date):
    print("In employee highest sales")

    df_r  = pd.read_csv('Task_4a_data.csv', index_col="ID")



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

value = []
x= 0
for item in df.column[id]:
    value[x] = value[x] + item
    x+=1

y = menu()
while y == 1 or y == 2 or y == 3:
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
                reigon = input("Enter the Reigon : ")
                s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                day, month, year = s_date.split("/")
                s_date = datetime.date(int(year), int(month), int(day))

                e_date = input("Enter Date in dd/mm/yyyy: ")
                day, month, year = e_date.split("/")
                e_date = datetime.date(int(year), int(month), int(day))

                s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            except:
                print("\n\nError Occurred Please try again\n\n")
                x = menu2()
            sales_by_region(reigon, s_date,e_date)
        elif x == 3:
             s_date = input("Enter Starting Date in dd/mm/yyyy: ")
             day, month, year = s_date.split("/")
             s_date = datetime.date(int(year), int(month), int(day))

             e_date = input("Enter Date in dd/mm/yyyy: ")
             day, month, year = e_date.split("/")
             e_date = datetime.date(int(year), int(month), int(day))
             s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
             e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y') 
             highest_sales_employee(s_date, e_date)
        else:
            x = menu2()
    else:
        x = menu()
    x = menu()