import random

#print(random.randrange(1,10))
l = [10,20,34,21,23,"prodip",True,21.22]
print(random.choice(l))
def roll_dice():
    return random.randint(1,6)
print("You rolled a : ",roll_dice())
num_rolls=5
total=sum([roll_dice() for _ in range(num_rolls)])
print("Rolling {} dice...".format(num_rolls))
print("Total: ", total)
import math
angle = 30 # degrees
radius = 8 # units
c = math.cos(math.radians(angle))
s = math.sin(math.radians(angle))
x = radius * c
y = radius * s
print("Coordinates of point from origin:")
print("X:", x)
print("Y:", y)