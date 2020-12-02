import sys
sys.path.append('C:/Users/Lenovo/Desktop/studia/wstęp do informatyki/zadania')
from zad1 import Calculator

class Solver:
    @staticmethod
    def getSolution(equation):
        pass

    @staticmethod
    def getSign(x):
        return "+ " if x >= 0 else ""

    @staticmethod
    def parseFraction(x, y):
        gcd = Calculator.getGreatestCommonDivisor(x, y)
        x = Solver.parseIntOrReturn(x / gcd)
        y = Solver.parseIntOrReturn(y / gcd)

        numericSolution = x / y

        if numericSolution == int(numericSolution):
            return int(numericSolution)

        elif x < 0 and y < 0:
            return Solver.parseSameSignFraction(x, y)

        elif x > 0 and y < 0:
            return Solver.parseOneNegativeFraction(x, y)

        elif abs(y) == 1:
            return x

        else:
            return str(x) + "/" + str(y)

    @staticmethod
    def parseIntOrReturn(x):
        return int(x) if x == int(x) else x

    @staticmethod
    def parseSameSignFraction(x, y):
        return str(abs(x)) + "/" + str(abs(y))

    @staticmethod
    def parseOneNegativeFraction(x, y):
        return str(-x) + "/" + str(abs(y))

    @staticmethod
    def throwIfAIsZero(equation):
        if equation.get("a") == 0:
            raise ValueError("'a' has to be different from zero!")