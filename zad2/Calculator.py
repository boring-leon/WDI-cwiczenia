class Calculator:
    @staticmethod
    def getDigitsSum(number):
        return sum(int(digit) for digit in str(number))

    @staticmethod
    def getStability(number):
        counter = 1
        digitsSum = Calculator.getDigitsSum(number)

        while Calculator.strLen(digitsSum) > 1:
            digitsSum = Calculator.getDigitsSum(digitsSum)
            counter += 1

        return counter

    @staticmethod
    def getDigitalRoot(number):
        sum = Calculator.getDigitsSum(number)
        return sum if Calculator.strLen(sum) == 1 else Calculator.getDigitalRoot(sum)

    @staticmethod
    def strLen(n):
        return len(str(n))