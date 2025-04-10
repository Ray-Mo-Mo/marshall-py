# Lesson 41

def scrabble(word):
total_score = 0
    for character in word:
        total_score += 1
    elif character.upper() in "EAIONRTLSU":
        total score += 2
    elif character.upper() in "DG":
        total score += 3
    elif character.upper() in "FHVWY":
        total score += 4
    elif character.upper() in "K":
        total score += 5
    elif character.upper() in "JX":
        total score += 8
    elif character.upper() in "QZ":
        total score += 10
return total_score
        
def best_score(a_list):
    result = ["", 0]
    for word in a_list:
        current_score = scrabble(word)

        if current_score > result[1]:
            result[0] = word
            result[1] = current_score
    return result