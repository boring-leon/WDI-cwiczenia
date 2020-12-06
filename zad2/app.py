import Calculator

#sumę cyfr dziesiętnej liczby całkowitej oraz pierwiastek cyfrowy

#7898->32->5 trwałość 2, pierwiastek 5
#12->3 trwałość 1 pierwiastek 3
#97985->38->11->2 trwałość 3 pierwiastek 2

while True:
    a = int(input("Input your number: "))
    print(f"Pierwiastek cyfrowy -> { Calculator.getDigitalRoot(a) }")
    print(f"Trwałość -> { Calculator.getStability(a) }")