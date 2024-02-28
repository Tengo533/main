import random as r
while True:
    p_or_c = input("Play against another player, or play against computer (p/c)?")
    if p_or_c == "c":
        mode = 0
        break
    if p_or_c == "p":
        mode = 1
        break
    else:
        print("Please use p or c.")


def rps_game():
    while True:
        choice = input("Rock, Paper or Scissors (r/p/s): ")
        
        if choice == "r" or choice == "p" or choice == "s": # Checks to see if they put something else instead of r,p,s
            break
        
        else:
            print("Please use r, p or s.")
    if mode == 1:
        choice2 = input("Rock, Paper or Scissors (r/p/s): ")
        
        if choice2 == "r" or choice2 == "p" or choice2 == "s": # Checks to see if they put something else instead of r,p,s
            break
        
        else:
            print("Please use r, p or s.")
    
    
    
    comp_choice = r.randint(0,2) # get a random number between 0 and 2
    
    # Tells the user what the computer got
    if comp_choice == 0:
        print("Rock!")
    
    elif comp_choice == 1:
        print("Paper!")
    
    elif comp_choice == 2:
        print("Scissors!")

    # Compares choice to comp_choice to see who won
    if choice == "r":
        if comp_choice == 0:
            print("Draw!")
        elif comp_choice == 1:
            print("You Lose!")
        elif comp_choice == 2:
            print("You Win!")
    
    elif choice == "p":
        if comp_choice == 1:
            print("Draw!")
        elif comp_choice == 2:
            print("You Lose!")
        elif comp_choice == 0:
            print("You Win!")
    
    elif choice == "s":
        if comp_choice == 2:
            print("Draw!")
        elif comp_choice == 0:
            print("You Lose!")
        elif comp_choice == 1:
            print("You Win!")

rps_game()

# Play again loop

while True:
    choice = input("Play again? (y/n): ")
    if choice == "y":
        rps_game()
    elif choice == "n":
        exit()
    else:
        print("Please use y or n.")
