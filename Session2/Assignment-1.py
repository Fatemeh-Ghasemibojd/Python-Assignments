a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c: "))

if a+b<c :
    print("No")
else:
    if a+c<b :
        print("No")
    else:
        if b+c<a :
            print("No")
        else:
            print("Yes")
