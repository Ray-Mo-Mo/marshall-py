# lesson 10

user_input = input(f"Enter numbers: ")
first_digit = int(user_input[0])
last_digit = int(user_input[-1])
second_digit = int(user_input[1])
third_digit = int(user_input[2])

if first_digit in (8, 9) and second_digit == third_digit and last_digit in (8, 9):
    print(f"all three conditions are met, the phone number is a telemarketer")
else:
    print(f"the three conditions are not met, the phone number is not a telemarketer")