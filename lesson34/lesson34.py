# Lesson 34

def csv2list(text):
    csv = text.split()
    print(csv)
    a_list = []

    for item in csv:
        a_list.append(int(item))

    return a_list

from random import randrange
def rand_list(start, end, frequency):
    if start < end and frequency > 0: 
        new_value = randrange(start, end+1)
        a_list.append(new_value)
    return a_list
    else:
        return []


print(csv2list("1, 2, 3, 4, 5, 6"))
print(randlist(1, 1000, 30))