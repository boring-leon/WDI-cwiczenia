# element maksymalny oraz minimalny w ciągu liczb
def findMax(arr):
    throwIfEmpty(arr)
    max = arr[0]
    for el in arr:
        if el > max: 
            max = el
    
    return max

def throwIfEmpty(arr):
    if len(arr) == 0:
        raise ValueError("Provided sequence can't be empty")


while True:
    try:
        stringSequence = str(input("Input your sequence number: "))
        numSequence = [int(n) for n in stringSequence.split()]
        print(findMax(numSequence))
    except ValueError as exception:
        print(str(exception))
