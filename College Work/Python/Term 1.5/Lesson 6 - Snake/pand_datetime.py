import datetime as dt
import pandas as pd
from dateutil import parser

def no_split():
    my_date = dt.date(2023, 11, 27)

    user_year = int(input("Please input the year: "))
    user_month = int(input("Please input the month: "))
    user_day = int(input("Please input the day: "))

    user_date = dt.date(user_year,user_month,user_day)

    if user_date < my_date:
        print("Your time is set back too far!")
    elif user_date > my_date:
        print("Your time is set forwards too far!")
    else:
        print("Your time is correct!")

    print(my_date)


def with_split():
    start_time = dt.datetime.now()
    start_time = start_time.second()
    print(start_time)
    date = input("Date (DD/MM/YYYY): ")
    date = date.split("/")
    year, month, day = date[2],date[1],date[0]
    
    date = dt.date(int(year), int(month), int(day))
    print(date)
    end_time = dt.datetime.now()
    end_time = end_time.second()
    total_time = end_time - start_time
    print(f"The function took {total_time} to complete.")


def task_1():
    dates = ["2010 Jan 1" ,'31-1-2000'  ,"October10, 1996, 10:40pm"]
    
    for text in dates:
        print(parser.parse(text))

def task_2():
    bday = "Aug 24, 2006"
    print(parser.parse(bday))

def task_3():
    d1 = dt.date(1869, 1, 2)
    d2 = dt.date(1869, 10, 2)

    td = d1 - d2
