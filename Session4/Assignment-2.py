import random

array = []
n = int(input("Enter n: "))

while len(array) < n:
    number = random.randint(1,1000)
    if number not in array:
        array.append(number)

print(array)