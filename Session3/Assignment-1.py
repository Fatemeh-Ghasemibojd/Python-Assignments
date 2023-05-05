import math

while True:
    a = float(input("Enter a: "))
    op = input("Enter op (+, -, *, /, radical, sin, cos, tan, cot, factorial, exit)")

    if op == "+":
        b = float(input("Enter b: "))
        r = a + b

    elif op == "-":
        b = float(input("Enter b: "))
        r = a - b

    elif op == "*":
        b = float(input("Enter b: "))
        r = a * b

    elif op == "/":
        b = float(input("Enter b: "))
        if b == 0:
            r = "#Div/0!"
        r = a / b

    elif op == "radical":
        if a < 0:
            r = "Error"
        else:
            r = math.sqre(a)

    elif op == "sin":
        r = math.sin(math.radians(a))

    elif op == "cos":
        r = math.cos(math.radinas(a))

    elif op == "tan":
        r = math.tan(math.radinas(a))

    elif op == "cot":
        r = math.cot(math.radinas(a))

    elif op == "factorial":
        if a < 0:
            r = "Error"
        else:
            r = math.factorial(int(a))
    
    elif op == "exit":
        break

    print(r)