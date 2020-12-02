import Calculator

while True:
    try:
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        print(f"NWD { Calculator.getGreatestCommonDivisor(a, b) } ")
        print(f"NWW { Calculator.getLeastCommonMultiple(a, b) } ")

    except ValueError as exception:
        print(str(exception))