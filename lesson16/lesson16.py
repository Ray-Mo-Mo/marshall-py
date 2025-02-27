# Lesson 16

num = int(input("Enter a number between 1 - 50: "))

r1 = num % 5
r2 = num % 3

if r1 == 0 and r2 == 0:
    print("Number is a multiple of 5 and 3")
elif r1 == 0:
    print("Number is a multiple of 5")
elif r2 == 0:
    print("Number is a multiple of 3")
else:
    print("Number is not a multiple of 5 or 3")