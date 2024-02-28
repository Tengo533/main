import random as r

def hangman_game():
    word_list = ["python", "database", "developer", "psudocode", "unreal"]

    def play_game ():
        max_guesses = 10
        rand = r.randint(0, 4)
        word = word_list[rand]
        while True:
            guess = input("\nGuess: ")
            for char in word:
                if char in guess:
                    print (char,end="")
                else:
                    print("_",end="")
                    max_guesses -= 1
            if guess == word:
                print("\nYou win!")
                break
            if max_guesses == 0:
                print("You lose!")
                break

    play_game()


hangman_game()













def play_again():
    while True:
        choice = input("Would you like to play again? (y/n): ")
        if choice == "y":
            hangman_game()
        elif choice == "n":
            exit()
        else:
            print("Please use y or n.")
