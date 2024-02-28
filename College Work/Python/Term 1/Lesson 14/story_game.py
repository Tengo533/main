import random as r
from random import randint


class Character:
    def __init__(self, health, speed, attack_range, damage):
        self.health = health
        self.speed = speed
        self.range = attack_range
        self.damage = damage



def intersection_left():
    choice = input("You find a chest, do you open it?\n1. Open it\n2. Leave it\nSelection:").upper()
    if choice == "1":
        loot = r.randint(0,2)
        if  class_selected == "ARCHER":
            if loot == 0:
                print("You found a Common Longbow!\nDamage boost: 1.1x")
                Archer.damage = Archer.damage * 1.1
                print(Archer.damage)
            elif loot == 1:
                print("You found a Rare Longbow!\nDamage boost: 1.2x")
                Archer.damage = Archer.damage * 1.2
                print()
            elif loot == 2:
                print("You found a LEGENDARY Longbow!\nDamage boost: 1.35x")
                Archer.damage = Archer.damage * 1.35
                print(Archer.damage)       

def start():
    while True:
        choice = input("You come across a three way intersection, which way do you go?\n1. Left\n2. Middle\n3. Right\nSelection:").upper()

        if choice == "1":
            intersection_left()
        #elif choice == "RIGHT":
            #intersection_right()
        #elif choice == "MIDDLE":
            #intersection_middle()
        else:
            print("You may only go left, middle or right.")
    
def class_select():
    while True:
        class_select = input("Please choose your class:\n1. Archer\n2. Rogue\n3. Brute\nSelection: ").upper()
        class_select.strip()
        if class_select == "1":
            class_select = Archer
            class_select_name = "ARCHER"
            break
        elif class_select == "2":
            class_select = Rogue
            class_select_name = "ROGUE"
            break
        elif class_select == "3":
            class_select = Brute
            class_select_name = "BRUTE"
            
            break
        else:
            print("Please choose Archer, Rogue or Brute.")
    return class_select_name

class_selected = class_select()
start()