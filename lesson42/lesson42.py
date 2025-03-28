# Lesson 42

def possible_sums(a_list, target):
    for i, value in enumerate(a_list):
        new_target = target - value
        if new_target in a_list[i+1:]:
            return True
    return false

test = [1, 3, 5, 8, 12, 13, 22]
target = 16

print(f"can {target} be made from {test}?")
print(possible_sums(test, target))