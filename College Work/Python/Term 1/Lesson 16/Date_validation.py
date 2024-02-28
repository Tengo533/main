def enter_date():
    def validation(date):
        if len(date) != 8: # check date length (8)
            print("Please use the format DDMMYYYY.")
        else:
            day = date[:2] # Slices Day from date
            month = date[2:4] # Slices Month from date
            year = date[4:] # slices year from date
            if day.isdigit() and month.isdigit() and year.isdigit(): # check if the date entered can be casted to integers
                day = int(day)
                month = int(month)
                year = int(year)

                if (day >= 1 and day <= 31) and (month >= 1 and month <= 12): # if day range is not 1-31 and month range is not 1-12
                    return True
                else:
                    print("Invaid Date.")
            else:
                print("Invaid Date.")
    while True:
        date = input("Date (DDMMYYYY): ") # Inital input
        if validation(date) == True:
            print("Valid.") # Once validation checks have been performed, print valid.
            break
        else:
            continue # Next itteration if validation checks failed.
enter_date()

