user_input = int(input("What is the current temperature: "))

if user_input <= 0:
    print("Its very cold out!")
elif user_input <= 25 and user_input > 0:
    print("Its a normal outside!")
else:
    print("Its very hot outside!")