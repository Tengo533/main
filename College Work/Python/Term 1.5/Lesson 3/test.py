def charge():

    while True:
        days_hired = int(input("Days Hired (>=1): "))
        if days_hired >= 1:
            break
        else:
            print("Days hired must be at least 1.")

    while True:
        mileageStart = input("Milage at start period: ")
        if mileageStart.isalpha() == True:
            print("Please enter a number.")
        else:
            mileageStart = int(mileageStart)
            break

    while True:
        mileageEnd = input("Milage at end period: ")
        if mileageEnd.isalpha() == True:
            print("Please enter a number.")
        else:
            mileageEnd = int(mileageEnd)
            break

    miles_driven = mileageEnd - mileageStart

    charge = (days_hired*20) + (miles_driven*0.05)

    print(charge)

charge()