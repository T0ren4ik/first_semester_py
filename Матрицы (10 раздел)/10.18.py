from random import randint

def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-4d" % el, end="  ")
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

str_dl_zam = [0] * n_
k = 2
a.append([0] * n_)
PrintMat(a)
print()

for i in range(len(a) - 1, k + 1, -1):
    a[i] = a[i - 1]

a[ind + 1] =

PrintMat(a)
