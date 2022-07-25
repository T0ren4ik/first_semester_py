import random


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

