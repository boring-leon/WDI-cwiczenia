from Solver import Solver

class LinearSolver(Solver):
    @staticmethod
    def getSolution(equation):
        Solver.throwIfAIsZero(equation)

        a = equation.get("a")
        b = equation.get("b")

        return f"x = {Solver.parseFraction(-b, a)}
