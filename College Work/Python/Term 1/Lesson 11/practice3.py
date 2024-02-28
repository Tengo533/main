def get_name():
    name = input("Name: ")

def get_address():
    address = input("Address: ")

def get_phone_number():
    while True:
        try:
            phone = int(input("Enter phone number: "))
            length = len(str(phone))
            if length != 8:
                print("Please use 8 numbers.")
            else:
                int(phone)
                break

        except ValueError:
            print("Please use numbers.")
            phone = 0
    

                

get_phone_number()