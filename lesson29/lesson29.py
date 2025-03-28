# Lesson 29

counter = 0

def consonant(text):
    word = input("what word: ")
    if word in text:
        for i in range(word):
            if word.isalpha() and word in {'a', 'e', 'i', 'o', 'u'}
                counter += 1

print(f"your word have {counter} consanats")