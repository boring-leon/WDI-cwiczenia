from Calculator import Calculator

while True:
    try:
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        print("NWD " + str(Calculator.getGreatestCommonDivisor(a, b)))
        print("NWW " + str(Calculator.getLeastCommonMultiple(a, b)))

    except ValueError as exception:
        print(str(exception))