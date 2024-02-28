import random as r
from random import randint

my_questions = (("How do you create an exponent?\n1. *\n2. %\n3. ^\n4. **", "4"),
                ("Which Python library is used to create a Graphical Interface?\n1. Tkinter\n2. Math\n3. Pandas\n4. Newspaper", "1"),
                ("Which type only takes two values?\n1. Integer\n2. Boolean\n3. String\n4. Float", "2"))

def play_again():
    while True:
        choice = input("Play again? (y/n) ")
        if choice == "y":
            game()
        elif choice == "n":
            exit()
        else:
            print("Please use y or n.")

def game():
    while True:
        def get_random():
            random_int = r.randint(0,2)
            return  random_int

        def play_quiz(qnum):
            if qnum == 0:
                answer = "4"
            if qnum == 1:
                answer = "1"
            if qnum == 2:
                answer = "2"
            print (my_questions[qnum][0])
            choice = input("Guess: ")
            if choice == my_questions [qnum][1]:
                print("Correct!")
            else:
                print("Incorrect")

        question = get_random()
        play_quiz(question)
        play_again()
game()



