STANDARD_CHARGE = 6
charge = 0

while True:
    ppl_ammount = int(input("How many people are travelling together? "))
    miles = int(input("How many miles are you travelling? "))

    if ppl_ammount >= 4 and miles > 5:
        charge = (miles*STANDARD_CHARGE)*0.90
    elif (ppl_ammount == 2 or ppl_ammount == 3) and miles > 5:
        charge = (miles*STANDARD_CHARGE)*0.95
    else:
        charge = miles*STANDARD_CHARGE
    
    print(f"The {miles} journey will cost £{charge}")

    