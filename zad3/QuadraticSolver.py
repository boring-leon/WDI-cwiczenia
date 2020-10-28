from Solver import Solver
import math

class QuadraticSolver(Solver):
    @staticmethod
    def getSolution(equation):
        Solver.throwIfAIsZero(equation)

        a = equation.get("a")
        b = equation.get("b")
        c = equation.get("c")

        delta = pow(b, 2) - (4 * a * c)

        if delta > 0:
            x1 = Solver.parseFraction(-b + math.sqrt(delta), 2 * a)
            x2 = Solver.parseFraction(-b - math.sqrt(delta), 2 * a)

            return f"x1 = {x1}, x2 = {x2}"

        elif delta == 0:
            x = Solver.parseFraction(-b, 2 * a)
            print("Your function is equivalent to " +
                  QuadraticSolver.getShortMultiplicationFormulaString({
                      "a": a,
                      "p": -x
                  }))
            return f"x = {x}"

        else:
            return f"Rozwiązanie nie istnieje, ponieważ delta = {Solver.parseIntOrReturn(delta)}"
        #return Solver.parseFraction(-b, a)

    @staticmethod
    def getShortMultiplicationFormulaString(equation):
        p = equation.get("p")
        a = Solver.parseIntOrReturn(equation.get("a")) if equation.get("a") != 1 else ""

        return f"{a}(x {Solver.getSign(p)}{p})^"
