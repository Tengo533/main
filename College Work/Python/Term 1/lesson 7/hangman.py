import random
words = ["python", "developer", "overwatch", "hanzo", "youtube", "caltgay", "fortnite"]
def get_word():
    word = random.choice(words)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Hangman")
    print(f"tries remaining {tries}")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("Not a vaild guess.")
        print(f"tries remaining: {tries}")
        print(word_completion)
        print("\n")