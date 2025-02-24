# Lesson 9

import random

while True:
    choices = ['rock', 'paper', 'scissors']
    bot = choices[random.randrange(len(choices))]

    if player == 'done':
        break
        
    player = input(f"Rock/Scissor/Paper: ")

    if player == bot:
        print(f"tie.")

    if player == 'rock' and bot == 'scissors' or player == 'scissors' and bot == 'paper' or player == 'paper' and bot == 'rock':
        print(f"the bot picked {bot}, you win.")
    else:
        print(f"the bot picked {bot}, you lost.")

