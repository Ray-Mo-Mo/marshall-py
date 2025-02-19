# Lesson 5

# inputs
initial_money = float(input("Enter the total money you started with: "))
cookies_sold = input("Enter the total amount of cookies sold: ")

# define variables
normal_cookies = 0
big_cookies = 0

# processes
for cookies in cookies_sold:
    if cookies == "c":
     normal_cookies = normal_cookies + 1
    elif cookies == "b":
     big_cookies = big_cookies + 1
    else:
     print(f"{cookies} is not a value sales option")


total_money = (normal_cookies * 1.25) + (big_cookies * 2)
print(f"the total money made from your sale is ${total_money}")