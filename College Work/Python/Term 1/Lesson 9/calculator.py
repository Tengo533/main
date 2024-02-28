import random as r
import math as m

# Calculator with all the operators, including ones that only use one int/float.

def calc():
    while True:
        def double_int():
            while True:
                num1 = float(input("Input num 1: "))
                num2 = float(input("Input num 2: "))
                break
            while True:
                choice = input("1. +\n2. -\n3. *\n4. /\n5. **\n6. %\nInput: ")
                print("\n")
                if choice == "1":
                    value = num1 + num2
                    print(f"{num1} + {num2} = {value}")
                    break
                elif choice == "2":
                    value = num1 - num2
                    print(f"{num1} - {num2} = {value}")
                    break
                elif choice == "3":
                    value = num1 * num2
                    print(f"{num1} * {num2} = {value}")
                    break
                elif choice == "4":
                    value = num1 / num2
                    print(f"{num1} / {num2} = {value}")
                    break
                elif choice == "5":
                    value = num1 ** num2
                    print(f"{num1} ** {num2} = {value}")
                    break
                elif choice == "6":
                    value = num1 % num2
                    print(f"{num1} % {num2} = {value}")
                    break
                else:
                    print("Please chose one of the operators 1-5.")
        def single_int():
            x=0
            while True:
                if x != 0:
                    while True:
                        choice = input("Run again? ")
                        if choice == "y":
                            break
                        elif choice == "n":
                            exit()
                        else:
                            print("Please use y or n.")
                num1 = float(input("Input num 1: "))
                break
            while True:
                x = x+1
                choice = input("1. Round\n2.Absolute\n3. Ceil\n4. Floor\n5. Trunc\n")
                if choice == "1":
                    value = round(num1)
                    print(f"{num1} rounded to {value}")
                    break
                if choice == "2":
                    value = abs(num1)
                    print(f"{num1} is the absolute value {value}")
                    break
                if choice == "3":
                    value = m.ceil(num1)
                    print(f"{num1} rounds up to {value}")
                    break
                if choice == "4":
                    value = m.floor(num1)
                    print(f"{num1} rounds down to {value}")
                    break
                if choice == "5":
                    value = m.trunc(num1)
                    print(f"{num1} = {value}")
                    break
        while True:
            choice = input("Single number or Double (S/D): ")
            choice = choice.upper()
            if choice == "S":
                single_int()
                break
            elif choice =="D":
                double_int()
                break
            else:
                print("Please use S or D.")
            
        while True:
            run_again = input("Run again? (y/n): ")
            if run_again == "y":
                print("\nRunning again.")
                break
            elif run_again == "n":
                print("\nClosing...")
                exit()
            else:
                print("Please use y or n.")


# Question game, gets random ints and asks the user the result of the two combined with a random operator.

def q_game():
    points = 0
    while True:
        num1 = r.randint(1,100)
        num2 = r.randint(1,100)
        operator = r.randint(0,3)

        if operator == 0:
            value = num1 + num2
            guess = float(input(f"Whats {num1} + {num2}? "))
            if guess == value:
                print("Correct!")
                points += 1
            elif guess != value:
                print("Wrong!")
                print(f"The answer was {value}")
        
        elif operator == 1:
            value = num1 - num2
            guess = float(input(f"Whats {num1} - {num2}? "))
            if guess == value:
                print("Correct!")
                points += 1
            elif guess != value:
                print("Wrong!")
                print(f"The answer was {value}")       
        
        elif operator == 2:
            value = num1 * num2
            guess = float(input(f"Whats {num1} * {num2}? "))
            if guess == value:
                print("Correct!")
                points += 1
            elif guess != value:
                print("Wrong!")
                print(f"The answer was {value}")
        
        elif operator == 3:
            value = num1 / num2
            value = round(value)
            guess = float(input(f"Whats {num1} / {num2}? (Rounded to the nearest integer.): "))
            if guess == value:
                print("Correct!")
                points += 1
            elif guess != value:
                print("Wrong!")
                print(f"The answer was {value}")
        while True:
            print(f"You have {points} points!")
            choice = input("Play again? ")
            if choice == "n":
                print("Stopping...")
                exit()
            elif choice == "y":
                break
            else:
                print("Please use y or n")

# Lets the user choose whether they want to play the question game or use the calculator.

while True:
    choice = input("Question game or calculator (q/c): ")
    if choice == "q":
        q_game()
        break
    elif choice == "c":
        calc()
        break
    else:
        print("Please use q or c.")
