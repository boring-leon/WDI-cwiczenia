class Calculator:
    @staticmethod
    def getGreatestCommonDivisor(a, b):
        Calculator.throwIfBothZeros(a, b)
        return b if a % b == 0 else Calculator.getGreatestCommonDivisor(
            b, a % b)

    @staticmethod
    def getLeastCommonMultiple(a, b):
        Calculator.throwIfNonUniqueInput(a, b)
        return abs(a * b) / Calculator.getGreatestCommonDivisor(a, b)

    @staticmethod
    def throwIfBothZeros(a, b):
        if a == 0 and b == 0:
            raise ValueError("Provided numbers can't be both zeros!")

    @staticmethod
    def throwIfNonUniqueInput(a, b):
        if a == b:
            raise ValueError("Enter two unique numbers")
