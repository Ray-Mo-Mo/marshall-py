# Lesson 27

def string_cleaner(text):
    result = ''
    for character in text:
        if character.isalpha():
            result += character.lower()
    return result

value = string_cleaner('HeLLo, wORLd!')
print(f"The value is: {value}")
