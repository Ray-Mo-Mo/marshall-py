# Lesson 43
def duplicates(a_list):
    result = []

    for value in a_list:
        if value not in result:
            result.append(value)
    return result

print(duplicates([1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4]))