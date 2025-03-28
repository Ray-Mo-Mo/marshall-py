# Lesson 28
def anagram_checker(t, s):

    arrT = list(t) 
    arrS = list(s)

    arrT.sort()
    arrS.sort()

    if(arrT == arrS):
        return True

    return False


print(anagram_checker("racecar", "carrace"))