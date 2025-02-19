from math import ceil

# Lesson 4


# inputs
fence1 = input("enter the amount of fences in row 1: ")
fence2 = input("enter the amount of fences in row 2: ")
fence3 = input("enter the amount of fences in row 3: ")

# calculations
total = len(fence1) + len(fence2) + len(fence3)

dozen_box = ceil(total / 12)
extras = 12*dozen_box - total

total_cost = 14.95*dozen_box

# outputs
print(f"Total cost of your {total} cans and {extras} leftovers is ${total_cost}")