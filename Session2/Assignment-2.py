name = input("enter name:")
family = input("enter family:")
a = float(input("enter the first course grade:"))
b = float(input("enter the second course grade:"))
c = float(input("enter the third course grade:"))
x = (a+b+c)/3
if x >= 17:
    print(name, family+"average is Great")
else:
    if 12 <= x <17:
        print(name, family+"'s average is Normal")
    else:
        print(name, family+"'s average is Fail")