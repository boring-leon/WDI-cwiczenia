def getDigitsSum(number):
    return sum(int(digit) for digit in str(number))

def getStability(number):
    counter = 1
    digitsSum = getDigitsSum(number)

    while strLen(digitsSum) > 1:
        digitsSum = getDigitsSum(digitsSum)
        counter += 1

    return counter

def getDigitalRoot(number):
    sum = getDigitsSum(number)
    return sum if strLen(sum) == 1 else getDigitalRoot(sum)


def strLen(n):
    return len(str(n))