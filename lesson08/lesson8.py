# Lesson 8

wins = 0
for i in range(6):
    player_status = input(f"Enter the game {i+1} result: ")

    if player_status == "w":
        wins += 1

group = 0

if wins > 4:
    group = 1
elif wins > 2:
    group = 2
elif wins > 0:
    group = 3


if wins == 0:
    print(f"the player is eliminated")

print(f"the player is in group {group} with {wins} amount of wins")