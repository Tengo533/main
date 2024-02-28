import time
import random

words = ["feminine","tumour","assume","wheel","white","space","ride","commemorate","miner","ignite","satisfied","penny","extort","convenience","helicopter"]

player_data = {
    'name': None,
    'best_time': float('inf') 
}

def game():
    typed = False
    word = words[random.randint(0,14)]
    print(f"Type the word:\n\n{word}")
    start_time = time.time()
    while typed != True:
        user_word = input("\nInput: ")
        if user_word == word:
            break
        else:
            print("Wrong spelling, try again!\n")
    end_time = time.time()
    total_time = end_time - start_time
    return round(total_time, 2)

def start():
    while True:
        choice = input("1. Play game\n2. Exit")
        if choice == "1":
            game_time = game()
            print(f"It took you {game_time} seconds to complete the word!\n")
            if game_time < player_data['best_time']:
                player_data['name'] = input("Enter your name: ")
                player_data['best_time'] = game_time
                print("Your name and time have been recorded as the best!\n")
        elif choice == "2":
            break
        else:
            print("Use 1 or 2.")
start()

if player_data['name'] is not None:
    print(f"The best player is {player_data['name']} with a time of {player_data['best_time']} seconds.")
else:
    print("No player data recorded.")