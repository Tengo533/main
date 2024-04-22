import pandas as pd
import matplotlib.pyplot as plt
import datetime

menu_item = ""
date_range = []
choice = ""

def Menu():
    user_choice = ""
    Menu_items = pd.read_csv("Term 3\ESP Task 3\Task3_data.csv")
    items = []

    for item in Menu_items["Menu Item"]:
        if item not in items:
            items.append(item)


    while True:
        print("Menu:\n")
        for item in items:
            print(item)
        user_choice = input("\nPlease select an item from the menu: ")

        if user_choice in items:
            menu_item = user_choice
            return menu_item
        else:
            print("Please select a valid menu item.")


menu_item = Menu()

def GetDateRange():
    df = pd.read_csv("Term 3\ESP Task 3\Task3_data.csv")
    df.columns = pd.to_datetime(df.columns)

    date_min = df.columns.min()
    date_max = df.columns.max()
    while True:

        start_date = pd.to_datetime(input(f"Please select a start date (DD/MM/YYYY) in the range {date_min} to {date_max}:"))

        if start_date >= date_min and start_date <= date_max:
            break
        else:
            print("Please input a date within the range.")
    
    while True:

        end_date = pd.to_datetime(input(f"Please select a end date (DD/MM/YYYY) in the range {date_min} to {date_max}:"))

        if end_date >= date_min and end_date <= date_max:
            break
        else:
            print("Please input a date within the range.")