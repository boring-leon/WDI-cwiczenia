def getByIteration(n):
    throwIfIsLessThanOne(n)
    elements = [0, 1]
    if n <=2:
        return elements[n - 1]
    else:
        for i in range(n):
            elements.append(elements[i] + elements[i+1])
        return elements[n - 1]

def getByRecursion(n):
    throwIfIsLessThanOne(n)
    return n - 1 if n <= 2 else getByRecursion(n -2) + getByRecursion(n -1)


def throwIfIsLessThanOne(n):
    if n < 1:
        raise ValueError("Please request an item with index greater than 0")