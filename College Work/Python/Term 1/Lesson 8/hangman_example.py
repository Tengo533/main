import random
# Lists of words to guess at
word_list = ["equality", "democracy", "liberty", "respect", "tolerance"]
max_guesses = 10 # max guesses a user is allowed

def play_one_game():

    # pick a word randomly for player to guess
    rnd_pos = random.randint(0, len(word_list) -1)
    choosen_word = word_list[rnd_pos] # choose word for game

    good_guesses = ["-"] * len( choosen_word )

    bad_guesses = [] # lists of users bad letter guesses
    num_bad_guesses = 0 # number of user bad guesses

    # Loop for max number of allowed guesses
    while num_bad_guesses < max_guesses:

        # Ask user to type in letter
        guess = input("Enter your leter guess (a-z): ")
        

play_one_game()