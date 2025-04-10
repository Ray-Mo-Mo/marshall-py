# Lesson 38

def palindrone(text):
    return text == text[::-1]

p_num = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        current = num1, num2
        if palindrone(str(current)):
            p_num.append(current)