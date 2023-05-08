import random

x = random.randint(1, 20)
n = 0
while True:
    number = int(input("Make a guess: "))
    n = n+1
    if number == x:
        print("winner", n)
        break
    if number < x:
        print("boro balatar")
    if number > x:
        print("boro paeentar")