# Lesson 30

def n_create(n):
    text = ''
    for i in range(1, n + 1):
        if i % 2 == 0:
            n += '1'
        else:
            n += '0'

def n_output(n):
    for i in range(1, n+1):
        print(n_create(i))

v = n_output(5)
print(v)