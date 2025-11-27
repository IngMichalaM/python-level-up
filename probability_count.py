# Write a python function to determine the probability of certain outcome when rolling dice
# Input - variable number of arguments for sides of dice
# output table of probability for each possible outcome
# example: roll_dice(4, 6, 6) for one 4-sided dice and two 6-sided dice


import random
from collections import Counter

def roll_dice(*dice, num_throw: int = 1000000):
    """ dice - numbers of sides of each dice """
    dice_throw_count = {f"{i}": 0 for i in range(3, sum(dice) + 1)}
    # dice_throw_count = Counter()

    for i in range(num_throw):
        round_total = 0
        for d in dice:
            round_total = round_total + random.randint(1, d)

        dice_throw_count[str(round_total)] += 1

    dice_throw_probability = {key: value * 100 / num_throw for key, value in dice_throw_count.items()}

    number_of_throws = 0
    for key, value in dice_throw_count.items():
        number_of_throws += value

    return dice_throw_probability, number_of_throws


def dice_throw_probability_pretty_print(dice_probability_dict):
    print("Outcome\tProbability")
    for key, value in dice_probability_dict.items():
        print(f"{key}\t{value:.2f}%")

result = roll_dice(6, 6, 6, 6, 6, 6)
dice_throw_probability_pretty_print(result[0])

print(f"The total number of throws is: {result[1]}")
