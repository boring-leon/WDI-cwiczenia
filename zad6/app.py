import fib

try:
    for i in range(10):
        val = fib.getByRecursion(i + 1)
        if fib.getByIteration(i + 1) == val:
            print(f"#{i + 1} = {val}")

except ValueError as e:
    print(str(e))

