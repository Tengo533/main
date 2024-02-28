import random as r
from random import randint
x = 1

rnd_counts = [0,0,0,0,0,0]

for range in range(0, 10000):
    dice = r.randint(0,5)
    rnd_counts[dice] += 1
for item in rnd_counts:
    print(f"Roll {x} = {item}")
    x = x+1