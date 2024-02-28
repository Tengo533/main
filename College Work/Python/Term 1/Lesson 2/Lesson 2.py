passcode = 1234
x=0
while True:
    inputted_code = int(input("Please input the code: "))
    if inputted_code == passcode:
        print("Correct code.")
        break
    else:
        x=x+1
        if x == 3:
            print("Too many attempts.")
            break
        print("Incorrect Code, please try again.")
