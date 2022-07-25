from math import sqrt
a = float(input("Введите а "))
b = float(input("Введите b "))
c = float(input("Введите c "))
D = (b**2 - 4*a*c)

if D >= 0:
    k1 = ((-b) + sqrt(D)) / 2*a
    k2 = ((-b) - sqrt(D)) / 2*a

if a != 0:
    if D < 0:
        print("Корней нет")
    elif D == 0:
        if k1 >= 0:
            print(sqrt(k1), -sqrt(k1))
        else:
            print('Корней нет')
    elif D > 0:
        if k1 >= 0:
            print(sqrt(k1), -sqrt(k1))
        if k2 >= 0:
            print(sqrt(k2), -sqrt(k2))
    else:
        print("Коней нет")

else:
    print("а = 0 (Ошибка условия)")
