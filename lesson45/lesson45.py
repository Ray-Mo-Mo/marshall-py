# Lesson 45

fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
user_input = str(input("What fruit: "))

counter = 0

if user_input in fruits:
    for i in range(1, len(user_input) + 1):
        counter += 1
    print(f"fruit found, it has {counter} amount of characters")
else:
    print("fruit not found")