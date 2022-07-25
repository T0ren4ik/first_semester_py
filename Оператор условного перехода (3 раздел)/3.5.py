from math import sqrt

a = float(input("a >>> "))
b = float(input("b >>> "))
c = float(input("c >>> "))

D = b*b - 4*a*c

if D >= 0:
    t1 = (-b + sqrt(D)) / 2 / a
    t2 = (-b - sqrt(D)) / 2 / a
    if t1 >= 0:
        x1, x2 = sqrt(t1), -sqrt(t1)
        print(x1, x2)
    if t2 >= 0 and sqrt(t2) != sqrt(t1) and qrt(t2) != - sqrt(t1):
        x3, x4 = sqrt(t2), -sqrt(t2)
        print(x3, x4)
else:
    print("Корней нет")
