import math

def getAverage(sequence):
    sequenceSum = 0
    for x in sequence:
        sequenceSum+=x
    return sequenceSum / len(sequence)

def getVariance(sequence):
    avg = getAverage(sequence)
    variance = 0
    for x in sequence:
        variance += pow(x - avg, 2)

    return variance / len(sequence)

def getStandardDeviation(sequence):
    return math.sqrt(getVariance(sequence))


sequence = [1, 2, 3 ,4 ,5]

print(f"Średnia arytmetyczna ciągu = {getAverage(sequence)}")
print(f"Wariancja ciągu = {getVariance(sequence)}")
print(f"Odchylenie standardowe ciągu = {getStandardDeviation(sequence)}")