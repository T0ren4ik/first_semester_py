import random


def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def creat_mat():
    n = 3
    a = [0] * n
    for i in range(n):
        a[i] = [0] * n
        for j in range(n):
            a[i][j] = random.randint(0, 9)

    return a


def min_zn_str(a):
    MIN = a[0]
    for i in a:
        if i < MIN:
            MIN = i
    return MIN


def remove_mat(a):
    n = 3
    for i in range(n):
        min_zn = min_zn_str(a[i])
        for j in range(n):
            a[i][j] *= min_zn

    return a


p_res = creat_mat()
print_mat(p_res)

res = remove_mat(p_res)
print_mat(res)
