import random

def roll_dice(num_dice):
    # Roll the dice
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, 6)
        rolls.append(roll)
    return rolls

num_dice = 2
results = roll_dice(num_dice)
print("Results:", results)
