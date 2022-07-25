a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
c = float(input("Введите третье число "))
# 1
if a != 0:
    Max = a
    if b > Max:    Max = b
    if c > Max:    Max = c
    Min = 5
    if a < Min:    Min = a
    print(Max/Min)
else:
    print("Вы ввели а = 0. Ошибка вычисления")
# 2
if a != 0:
    if a > b:   Max1 = a
    else:       Max1 = b
    if c > Max1:    Max1 = c
    if a < 5:   Min1 = a
    else:   Min1 = 5
    R = Max1 / Min1
    print("%+.1f" % R)
else:
    print("Вы введи а = 0. Ошибка вычисления")

