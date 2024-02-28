import random as r

def rps_game():
    while True:
        choice = input("Rock, Paper or Scissors (r/p/s): ")
        
        if choice == "r" or choice == "p" or choice == "s": # Checks to see if they put something else instead of r,p,s
            break
        
        else:
            print("Please use r, p or s.")
    
    comp_choice = r.randint(0,2) # get a random number between 0 and 2
    
    # Tells the user what the computer got
    if comp_choice == 0:
        print("Rock!")
    
    if comp_choice == 1:
        print("Paper!")
    
    if comp_choice == 2:
        print("Scissors!")

    # Compares choice to comp_choice to see who won
    if choice == "r":
        if comp_choice == 0:
            print("Draw!")
        if comp_choice == 1:
            print("You Lose!")
        if comp_choice == 2:
            print("You Win!")
    
    if choice == "p":
        if comp_choice == 1:
            print("Draw!")
        if comp_choice == 2:
            print("You Lose!")
        if comp_choice == 0:
            print("You Win!")
    
    if choice == "s":
        if comp_choice == 2:
            print("Draw!")
        if comp_choice == 0:
            print("You Lose!")
        if comp_choice == 1:
            print("You Win!")

rps_game()

# Play again loop

while True:
    choice = input("Play again? (y/n): ")
    if choice == "y":
        rps_game()
    if choice == "n":
        exit()
    else:
        print("Please use y or n.")

