import random as rand
from random import randint

def dice():

    while True:
        dice1 = rand.randint(1, 6)
        input("Roll?")
        print(f"You rolled a {dice1}.")
        dice2 = rand.randint(1, 6)
        input("Roll?")
        print(f"You rolled a {dice2}")
        
        if dice1 == dice2:
            print("You lose!")
            exit()


dice()