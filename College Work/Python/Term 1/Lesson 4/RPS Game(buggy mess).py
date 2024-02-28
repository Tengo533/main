def rps_game():
    while True:

        # Asks players for rock, paper or scissors then stores their answer
        while True:
            player1 = input("Player 1: Rock, paper or scissors? (r/p/s)")
            player2 = input("Player 2: Rock, paper or scissors? (r/p/s)")

            if player1 == "r": # Rock
                if player2 == "r":
                    print("Draw!")
                    break
                if player2 == "p":
                    print("Player 2 wins!")
                    break
                if player2 == "s":
                    print("Player 1 wins!")
                    break
            
            if player1 == "p": # Paper
                if player2 == "p":
                    print("Draw!")
                    break
                if player2 == "r":
                    print("Player 1 wins!")
                    break
                if player2 == "s":
                    print("Player 2 wins!")
                    break

            
            if player1 == "s": # Scissors
                if player2 == "s":
                    print("Draw!")
                    break
                if player2 == "r":
                    print("Player 2 wins!")
                    break
                if player2 == "p":
                    print("Player 1 wins!")
                    break

        # If they didnt type r, p or s, it will ask again and tell them the right parameters

            else:
                print("Please choose r, p or s.")
                continue

        # Asks users if they would like to play again
        
        while True:
            play_again = input("Play again? (y/n) ")
            if play_again == "y":
                break
            if play_again == "n":
                exit()
            else:
                print("Please use y or n.")
rps_game()
    
def rps_game():
    while True:
        # Asks players for rock, paper or scissors then stores their answer
        while True:
            def play_againrps():
                while True:
                    play_again = input("Play again? (y/n) ")
                    if play_again == "y":
                        break
                    if play_again == "n":
                        print("Closing game...\n\n")
                        game_menu()
                    else:
                        print("Please use y or n.") 
       
            player1 = input("Player 1: Rock, paper or scissors? (r/p/s) ")
            player2 = rand.randint(0, 2)

            if player2 == 0:
                player2 == "r"
                print("Rock!")
            if player2 == 1:
                player2 == "p"
                print("Paper!")
            if player2 == 2:
                player2 == "s"
                print("Scissors!")

            if player1 == "r": # Rock
                if player2 == "r":
                    print("Draw!")
                    play_againrps()
                if player2 == "p":
                    print("Player 2 wins!")
                    play_againrps()
                if player2 == "s":
                    print("Player 1 wins!")
                    play_againrps()
            
            if player1 == "p": # Paper
                if player2 == "p":
                    print("Draw!")
                    play_againrps()
                if player2 == "r":
                    print("Player 1 wins!")
                    play_againrps()
                if player2 == "s":
                    print("Player 2 wins!")
                    play_againrps()

            
            if player1 == "s": # Scissors
                if player2 == "s":
                    print("Draw!")
                    play_againrps()
                if player2 == "r":
                    print("Player 2 wins!")
                    play_againrps()
                if player2 == "p":
                    print("Player 1 wins!")
                    play_againrps()

        # If they didnt type r, p or s, it will ask again and tell them the right parameters



        # Asks users if they would like to play again