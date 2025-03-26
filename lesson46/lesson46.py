# Lesson 46

num = int(input("enter a number: "))

counter = 0

while num != 1:
    if num % 2 == 1:
        num = 3*num+1
        print(num)
    else:
        num = num / 2
        print(num)
