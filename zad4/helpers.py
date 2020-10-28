import random


def getRandomSequenceOf(length, sequenceItemRange):
    sequence = []
    for x in range(length):
        sequence.append(random.randrange(sequenceItemRange))

    return sequence


def printMostCommonElementMessage(sequence):
    counter = {}
    for el in sequence:
        if counter.get(el) == None:
            counter.update({el: 1})
        else:
            counter.update({el: counter.get(el) + 1})

    firstKey = next(iter(counter))
    maxKey = firstKey
    alternativeMaxItems = []

    for key in counter.keys():
        if counter.get(key) > counter.get(maxKey):
            maxKey = key

    for key in counter.keys():
        if counter.get(key) == counter.get(maxKey) and maxKey != key:
            alternativeMaxItems.append(key)

    print("Ciąg -> " + str(sequence))
    print("Najczęściej (" + str(counter.get(maxKey)) + "x) występuje w ciągu liczba " + str(maxKey))
    if len(alternativeMaxItems) > 0:
        print("Wykryto inne wartości występujące w ciągu " + str(counter.get(maxKey)) + "x : " + str(alternativeMaxItems))
