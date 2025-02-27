# Lesson 23

x = input("enter number, done to stop: ")
counter = 0
total = 0

while True:
    if x == "done":
        break
    else:
        total += int(x)
        counter += 1
        x = input()

average = total / counter
print(average)
        