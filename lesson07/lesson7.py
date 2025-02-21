# Lesson 7

from random import randrange
difficulty = int(input("Enter the DC: "))

player_roll = randrange(1, 21)

print(f"the playes has rolled {player_roll} on their D20.")


if player_roll >= difficulty:
    print(f"the player was successful at {player_roll} >= {difficulty}")
else:
        print(f"the player was not successful at {player_roll} < {difficulty}")