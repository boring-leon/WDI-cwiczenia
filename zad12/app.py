#dwa ciągi tekstu są anagramami 
def getLetterDictionary(word):
    dictionary = {}
    for letter in word:
        if dictionary.get(letter) == None:
            dictionary.update({letter: 1})
        else:
            dictionary.update({letter: dictionary.get(letter) + 1})
    return dictionary

def compareDictionaries(dict1, dict2):
    for key in dict1.keys():
        if dict1.get(key) != dict2.get(key):
            return False
    return True

def areAnagrams(word1, word2):
    return compareDictionaries(getLetterDictionary(a), getLetterDictionary(b))

while True:
    a = str(input("Podaj pierwszy wyraz: "))
    b = str(input("Podaj drugi wyraz: "))
    if areAnagrams(a, b):
        print("Podane słowa są anagramami")
    else:
        print("Podane słowa nie są anagramami")
    
