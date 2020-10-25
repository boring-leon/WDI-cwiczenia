class Calculator:  
    
    @staticmethod
    def getDigitsSum(number): 
        return sum(int(digit) for digit in str(number))

    @staticmethod
    def getStability(number):
        counter = 1
        while True:
            digitsSum = Calculator.getDigitsSum(number) 
            sumLength = Calculator.strLen(digitsSum)
            counter += 1

            if sumLength != 1: 
                break

        return counter

    @staticmethod
    def getDigitalRoot(number):
        sum = Calculator.getDigitsSum(number)
        return sum if Calculator.strLen(sum) == 1 else Calculator.getDigitalRoot(sum)

    @staticmethod
    def strLen(n):
        return len(str(n))


while True:
    try:
        a = int(input("Input your number: "))
        print("Pierwiastek cyfrowy -> " + str(Calculator.getDigitalRoot(a)))
        print("Trwałość -> " + str(Calculator.getStability(a)))
    except ValueError as exception:
        print(str(exception))