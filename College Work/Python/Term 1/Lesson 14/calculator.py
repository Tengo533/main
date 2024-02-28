def add(num1, num2):
    value = num1 + num2
    return value

def sub(num1, num2):
    value = num1 - num2
    return value

def div(num1, num2):
    value = num1 / num2
    return value

def multiply(num1, num2):
    value = num1 * num2
    return value

def modulo(num1, num2):
    value = num1 % num2
    return value

def power(num1, num2):
    value = num1 ** num2
    return value

def int_division(num1, num2):
    value = num1 // num2
    return value

def run_again():
    while True:
        choice = input("Run again? (y/n) \nChoice: ")
        if choice == "y":
            calc_menu()
        elif choice == "n":
            break
        else:
            print("Please use y or n.")

def get_num():
    while True:
        try:
            num1 = int(input("Num1: "))
            num2 = int(input("Num2: "))
            break
        except ValueError:
            print("Please use numbers.\n")
            num1 = 0
            num2 = 0
        except:
            print("Unknown Error.\n")
            num1 = 0
            num2 = 0
    return num1, num2

def calc_menu():
    while True:
        print("1. +\n2. -\n3. /\n4.* \n5. %\n6. **\n7.//")
        operator = input("Choice: ")
        if ("1" in operator) or ("2" in operator) or ("3" in operator) or ("4" in operator) or ("5" in operator) or ("6" in operator) or ("7" in operator):
            break
        
        else:
            print("Please use 1, 2, 3 or 4.")
    numbers = get_num()
    if operator == "1":
        result = add(numbers[0], numbers[1])
        print(f"{numbers[0]} + {numbers[1]} = {result}")
    
    elif operator == "2":
        result = sub(numbers[0], numbers[1])
        print(f"{numbers[0]} - {numbers[1]} = {result}")
    
    elif operator == "3":
        result = div(numbers[0], numbers[1])
        print(f"{numbers[0]} / {numbers[1]} = {result}")
    
    elif operator == "4":
        result = multiply(numbers[0], numbers[1])
        print(f"{numbers[0]} * {numbers[1]} = {result}")
    
    elif operator == "5":
        result = modulo(numbers[0], numbers[1])
        print(f"{numbers[0]} % {numbers[1]} = {result}")

    elif operator == "6":
        result = power(numbers[0], numbers[1])
        print(f"{numbers[0]} ** {numbers[1]} = {result}")

    elif operator == "7":
        result = int_division(numbers[0], numbers[1])
        print(f"{numbers[0]} // {numbers[1]} = {result}")
    run_again()
calc_menu()