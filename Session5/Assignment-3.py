def fibonacci(n):
    array = []
    a = 0
    b = 1
    for i in range(n):
        if i == 0:
            array.append(b)
        else:
            array.append(b + a)
            a = b
            b = array[i]
    array = array[::-1]
    string = ""
    for i in range(n):
        if i == 0:
            string += str(array[i])
        else:
            string += " ,"+str(array[i])
    print(string)

        
n = int(input("enter n : "))
fibonacci(n)