import fib

fibCount = int (input("Ile wyrazów ciągu wyznaczyć: "))

try:
    for i in range(fibCount):
        val = fib.getByRecursion(i + 1)
        if fib.getByIteration(i + 1) == val:
            print(f"#{i + 1} = {val}")

except ValueError as e:
    print(str(e))

