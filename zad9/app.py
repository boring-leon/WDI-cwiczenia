#ile elementów w ciągu jest większych od średniej
def getAverage(arr):
    arrSum = 0
    for x in arr:
        arrSum +=x
    return arrSum / len(arr)

def getGreaterThanAverageCount(arr):
    average = getAverage(arr)
    count = 0
    for x in arr:
        if x > average: 
            count+=1
    return count


while True:
    stringSequence = str(input("Input your sequence number: "))
    numSequence = [int(n) for n in stringSequence.split()]
    print(getGreaterThanAverageCount(numSequence))
