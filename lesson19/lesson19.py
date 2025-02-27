# Lesson 19
num = int(input(f"Enter a number: "))
counter = 0

for divider in range(1, num+1):
    if num % divider == 0:
        counter += 1

if counter == 2:
    print(f"prime")
else:
    print(f"composite")
