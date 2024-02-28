STANDARD_CHARGE = 20
charge = 0
while True:
    d_or_g = input("Are you booking in a dog or a cat? ").upper()
    d_or_g.upper()
        
    break


days_booked = int(input("How many days do you want to book the pet in for? "))



if d_or_g == "CAT":
    while True:
        package = input("Do you want a gold or silver package? ")
        package = package.upper()
        if package == "GOLD":
            charge = (days_booked * STANDARD_CHARGE)*1.25
            print(charge)
            break
        elif package == "SILVER":
            charge = days_booked*STANDARD_CHARGE
            print(charge)
            break
        else:
            print("Please type silver or gold.")

if d_or_g == "DOG":
    while True:
        package = input("Do you want a platinum or gold package? ")
        package = package.upper()
        if package == "PLATINUM":
            charge = (days_booked * STANDARD_CHARGE)*1.25
            break
        elif package == "GOLD":
            charge = days_booked*STANDARD_CHARGE
            break
        else:
            print("Please type platinum or gold.")

d_or_g.lower()

print(f"The {d_or_g} package will cost {charge}")
