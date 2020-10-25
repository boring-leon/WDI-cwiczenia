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

#7898->32->5 trwałość 2, pierwiastek 5
#12->3 trwałość 1 pierwiastek 3
#97985->38->11->2 trwałość 3 pierwiastek 2

while True:
    a = int(input("Input your number: "))
    print("Pierwiastek cyfrowy -> " + str(Calculator.getDigitalRoot(a)))
    print("Trwałość -> " + str(Calculator.getStability(a)))