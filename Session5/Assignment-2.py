# ax*x + b*x + c = 0

import math

def equation(a, b, c):
    Delta = b*b-4*a*c
    if Delta < 0:
        print("No answer")
    elif Delta == 0:
        x = -b / (2*a)
        print("answer is ",x)
    elif Delta > 0:
        x1 = (-b + math.sqrt(Delta))/(2*a)
        x2 = (-b - math.sqrt(Delta))/(2*a)
        print("answers are ",x1, "and",x2)

equation (2,4,1)

