# Lesson 12

angles = input("Enter 3 angles: ")

angle_list = list(map(int, angles.split()))

total_angle = sum(angle_list)

if len(angle_list) != 3:
    print("please enter values with 3")
else: 
    a1, a2, a3 = map(int, angle_list)
    print(a1, a2, a3, total_angle)

if total_angle == 180:
    if a1 == a2 == a3:
        print("Equilateral")
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print("Isosleces")
    else:
        print("Scalene")
else:
    print("not a triangle")