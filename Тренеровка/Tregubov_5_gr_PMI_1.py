import random


def menu():
    print("Выберете пункт меню (начните с заполнения матрицы)")
    print("1) получение элементов матрицы случайным образом")
    print("2) вывод матрицы")
    print("3) проверка строки вывод изменеенного(при необходимости)")
    print("4) проверка столбца и вывод измененного списка (при необходимости)")
    print("5) выход")
    print()


def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def create_mat(n, m):
    a = [0] * n
    for i in range(len(a)):
        a[i] = [0] * m
        for j in range(len(a[i])):
            a[i][j] = random.randint(-9, 9)

    return a


def ot_str(a):
    i = 0
    flag = True
    ind = -1
    while i < len(a) and flag:
        p = 0
        j = 0
        while j < len(a[i]) and flag:
            if a[i][j] < 0:
                p += 1
            j += 1
        if p == len(a[i]):
            flag = False
            ind = i
        i += 1

    if not flag:
        if ind != len(a) - 1:
            a.append([0] * len(a[0]))

            for i in range(len(a) - 1, ind + 1, -1):
                a[i] = a[i - 1]

            a[ind + 1] = a[-1]
        else:
            a.append(a[-1])

    return not flag


def stolb_pos(a):
    i = 0
    j = 0
    flag = False
    while j < len(a[i]) and not flag:
        i = 0
        ind = j
        P = 0
        while i < len(a) - 1 and not flag:
            if a[i][j] <= a[i + 1][j]:
                P += 1
            i += 1

        flag = P == len(a) - 1
        j += 1

    if flag:
        return flag, ind
    else:
        return flag, -1


def izm_stolb(a, k, ind):
    for i in range(len(a[0])):
        a[i][k], a[i][ind] = a[i][ind], a[i][k]
    return a


vv = 0

while vv != 5:
    if vv == 1:
        n = int(input("n >>> "))
        m = int(input("m >>> "))
        a = create_mat(n, m)

    elif vv == 2:
        print("Итоговая матрица:")
        print_mat(a)
    elif vv == 3:
        bo = ot_str(a)
        if bo:
            print("В матрице ест строка, состоящая только из отрицательных чисел.")
            print()
            print("Итоговая матрица:")
            print_mat(a)
        else:
            print()
            print("В матрице нет строки, состояще только из отрицательных чисел.")
    elif vv == 4:
        b = stolb_pos(a)
        if b[0]:
            print("В матрице есть столбец, элементы которого образует неубывающую последовательность, его немер:", b[1])
            zn = int(input("Введите номер столбца, с которым нужно поменять: "))
            a = izm_stolb(a, zn, b[1])
            print()
            print("Итоговая матрица:")
            print_mat(a)
        else:
            print()
            print("В матрице нет столбца, элементы которого образует неубывающую последовательность.")
    elif vv == 0:
        menu()
    else:
        print("такого пункта нет!")

    print("--" * 45)
    vv = int(input("Введите пункт меню(0 для вызова меню) ---> "))

print()
print("До встречи!")
print("--" * 45)
