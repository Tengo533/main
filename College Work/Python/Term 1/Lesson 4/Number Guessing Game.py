import random as rand # importing the random library for randint


def run_game():
    while True:

        # Ask the user the min and max random number range

        min = int(input("Set the min number range: "))
        max = int(input("Set the max number range: "))

        # Get the random number

        random_number = rand.randint(min, max)

        guess_ammount = 1
        
        # While loop ask the user to guess, then outputs whether they were high, low or exactly right.

        print(f"Guess the number between {min}-{max}")

        while True:
            user_guess = int(input("Guess: "))
            if user_guess > random_number:
                print("Guess too high!")
                guess_ammount = guess_ammount + 1

            elif user_guess < random_number:
                print("Guess too low!")
                guess_ammount = guess_ammount + 1

            elif user_guess == random_number:
                print("You win!")
                print("It took you",guess_ammount,"tries!")
                break
        
        # Asks the user if they would like to play again
        while True:
            play_again = input("Do you want to play again (y/n)?")
            if play_again == "n":
                print("Closing game...\n\n")
                game_menu()
            if play_again == "y":
                break
            else:
                print("Please use y or n.")


while True:
    def game_menu():
        menu = 0
        choice = input("1. Number Guessing Game\n2. Quit\nChoice: ")
        if choice == "1":
            run_game()
        if choice == "2":
            print("Quitting...")
            exit()
        else:
            print("Please use 1, 2 or 3.")
    game_menu()