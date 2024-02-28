import random


# Customer Order - simple ebay type market where can put it bid to buy an item
def co():
    co.name = input("Pls enter name: ")
    co.postcode = input("Pls enter postcode: ")
    co.item = input("Pls enter item you want: ")
    co.price = input("Pls enter what you will pay: ")


# Print order details. Must include name, postcode, item and price.
# Price must be shown to pence only.
def print_order():
    print(f"Order Details: name: {co.name}   item: {co.item}   price: {co.price}")


# Calculate how much vat to pay based on 20% vat rate
def vat():
    vat.fee = co.price * 2
    print(f"Vat = {vat.fee}")
    return vat.fee


# Decide how much is postage - 
def postage():
    postage.fee = 3.95


# Customers get a lucky dip prize
def prize():  
    prizes = ["CuddlyToy", "LollyPop", "XBox", "PS5"]


    # Print out possible prizes
    for i in range(3):
        print(f"Prize {i} = {prizes[i]}")


    # randint start and stop values are inclusive
    rnd_val = random.randint(0,2)
    prize.picked = prizes[rnd_val]


print("STARTING PROGRAM")
print("\n\n")


co()
print_order()


vat()
postage()


extra_costs = vat.fee + postage.fee 
print(f"Extra Costs = {extra_costs}")


prize()


print("STOPPING PROGRAM") #BM INDENT


