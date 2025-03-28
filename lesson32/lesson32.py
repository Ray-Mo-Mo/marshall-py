# Lesson 32

# word = []

# def sort(text):
#     for word in range(1, len(text)):
#         if word in text:
#             word.append(text)
#     return word

# text = 'eerrddffss'
# print(sort(text))

def duplicated(word1, word2):
    if  not word1 or not word2:
        return []
    else:
        set_word2 = set(word2)
        result = []
        for character in word1:
            result.append(character)
        return sorted(result)

print(duplicated("hello world", "goodbye world"))