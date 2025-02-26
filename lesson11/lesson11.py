# Lesson 11

x_input = int(input(f"Enter the x value: "))
y_input = int(input(f"Enter the y value: "))

if x_input >= 0 and y_input >= 0:
    print(f"quadrant 1")
elif x_input <= 0 and y_input >= 0:
    print(f"quadrant 2")
elif x_input >= 0 and y_input <= 0:
    print(f"quadrant 4")
elif x_input <= 0 and y_input <= 0:
    print(f"quadrant 3")