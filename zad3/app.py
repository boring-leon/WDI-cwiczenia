from LinearSolver import LinearSolver
from QuadraticSolver import QuadraticSolver

LS = LinearSolver
QS = QuadraticSolver

while True:
    try:
        a = float(input("Input a in ax + b: "))
        b = float(input("Input b in ax + b: "))
        print(str(LS.parseIntOrReturn(a)) + "x " + LS.getSign(b) + str(LS.parseIntOrReturn(b)) + " = 0")
        print(LS.getSolution({"a": a, "b": b }) )

        a = float(input("Input a in ax^ + bx + c: "))
        b = float(input("Input b in ax^ + bx + c: "))
        c = float(input("Input c in ax^ + bx + c: "))

        print(str(QS.parseIntOrReturn(a)) + "x^ " + QS.getSign(b) + str(QS.parseIntOrReturn(b)) + "x " +  
        QS.getSign(c) + str(QS.parseIntOrReturn(c)) + " = 0")
        print(QS.getSolution({"a": a, "b": b, "c": c }))
    
    except ValueError as exception:
        print(str(exception))

    