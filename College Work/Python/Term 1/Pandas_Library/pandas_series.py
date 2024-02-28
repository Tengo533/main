import pandas as pd
def series():
    a = [1,7,5]

    myvar = pandas.Series(a)
    print(myvar)

def series_keyvalue():
    calories = {"day1": 420, "day2": 380, "day3": 390}
    myvar = pandas.Series(calories)
    print(myvar) #prints the entire series
    print(myvar["day1"]) # prints only the value stored in "day1"
