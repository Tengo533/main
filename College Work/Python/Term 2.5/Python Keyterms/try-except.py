try:
    user_input = input("Enter depth (meters): ")
    float(user_input)
    print(f"You are {user_input} meters deep!")

except:
    print("ERROR: You did not input a number!")