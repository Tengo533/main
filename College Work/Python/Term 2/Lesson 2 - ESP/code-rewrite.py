
products = [['Cheese', 1], ["Potatoes",1.70], ["Carrots", 1.50], 
["Peas",1.10], ["Lettuce",0.80], ["Onions",1], ["Apples",0.70]]


def input_user_info():

    first_name = input("First Name: ").capitalize()
    last_name = input("Last Name: ").capitalize()
    address = input("Address: ")
    post_code = input("Post Code: ")
    phone_number = number_format()

def sell_products():
    choice = input("Sell a product, or finish sale (y/done): ")
    if choice != 1:
        print("Please Input a choice in the range 1.")



def number_format():
    while True:
        try:
            number = input("Number: ")
            num_len = len(number)
            number = int(number)
            if num_len != 11:
                print("Error: Incorrect number format.")
            else:
                break
        except:
            print("Error: Please input a number.")


input_user_info()