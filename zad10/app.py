#ą arytmetyczną, warinację i odchylenie standardowego ciągu liczb
def getAverage(arr):
    arrSum = 0
    for x in arr:
        arrSum +=x
    return arrSum / len(arr)

import math

def getVariance(arr):
    average = getAverage(arr)
    variance = 0
    for x in arr:
        variance += pow(x - average, 2)

    return variance / len(arr)

def getStandardDeviation(arr):
    return math.sqrt(getVariance(arr))


while True:
    stringSequence = str(input("Input your sequence number: "))
    numSequence = [int(n) for n in stringSequence.split()]
    print(getStandardDeviation(numSequence))
