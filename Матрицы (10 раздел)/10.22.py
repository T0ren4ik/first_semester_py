from random import randint


def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-.1f" % el, end="  ")
        print()


def creat_mat(m, n, el):
    a = [0] * m
    for i in range(len(a)):
        a[i] = [0] * n
        for j in range(len(a[i])):
            a[i][j] = randint(-el, el)
    return a


m_ = 5
n_ = 4
el_ = 10
a = creat_mat(m_, n_, el_)

PrintMat(a)
print()

k = 2
for i in range(k, len(a) - 1):
    a[i] = a[i + 1]

a = a[: -1]

PrintMat(a)
