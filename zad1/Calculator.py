def getGreatestCommonDivisor(a, b):
    throwIfBothZeros(a, b)
    gcd = b if a % b == 0 else getGreatestCommonDivisor(b, a % b)
    return gcd if int(gcd) == gcd else 1

def getLeastCommonMultiple(a, b):
    throwIfNonUniqueInput(a, b)
    return abs(a * b) / getGreatestCommonDivisor(a, b)


def throwIfBothZeros(a, b):
    if a == 0 and b == 0:
        raise ValueError("Provided numbers can't be both zeros!")

def throwIfNonUniqueInput(a, b):
    if a == b:
        raise ValueError("Enter two unique numbers")
