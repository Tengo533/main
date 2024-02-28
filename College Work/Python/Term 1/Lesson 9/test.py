loopcount = 0
while True:
    stop = input("Stop the loop? (y/n): ")
    if stop == "y":
        print(f"You looped a total of {loopcount} times!")
        break
    elif stop == "n":
        loopcount += 1
    else:
        print("Use y or n.")