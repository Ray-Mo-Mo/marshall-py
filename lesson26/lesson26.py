# Lesson 26

def divisible(num1, num2): # define the variable for if a number is divisible
    return num1 % num2 == 0

def factor(number): # function for if a number is factor
    counter = 0
    for i in range(1, number + 1):
        if divisible(number, i):
            counter += 1
    return counter

upper_limit = int(input("Enter a number: "))

for num in range(1, upper_limit+1):
    factor_size = factor(num)
        
    print(f"The number {num} has {factor_size} factors")

