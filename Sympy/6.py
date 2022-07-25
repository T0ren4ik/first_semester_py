from sympy import Matrix, randprime, det, eye
from random import randint


def PrintMat(a):
    a = a[:]
    for i in range(3):
        print(a[(0+i) * 3: (i+1)*3])


def mm():
    L = []
    for i in range(9):
        L += [randint(1, 5)]
        # L += [randprime(0, 30)]

    res = Matrix(3, 3, L)

    return res


def remove(m):
    for i in range(3):
        m[(0+i), (0+i)] = 1

    return m


def mm_1():
    res = eye(3)

    return res


M_0 = mm()
PrintMat(M_0)
opr_1 = det(M_0)
print()

M_r = remove(M_0)
opr_2 = det(M_r)
PrintMat(M_r)

print()
print(opr_1, opr_2)

M_1 = mm_1()
PrintMat(M_1)
print()

for i in range(3):
    rr = opr_1 - opr_2
    M_1[i, (2-i)] = rr

PrintMat(M_1)
