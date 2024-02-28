name = input("Name: ")
address = input("Address: ")

def get_phone():
    while True:
        try:
            phone_number = int(input("Phone number: "))
            if type(phone_number) != int:
                print("Invalid phone number.")
            else:
                return phone_number
        except ValueError:
            print("Invalid phone number.")
get_phone()
