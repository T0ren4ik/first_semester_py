from random import randint


def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-4d" % el, end="")
        print()


def creat_mat(m, n, el):
    a = [0] * m
    for i in range(len(a)):
        a[i] = [0] * n
        for j in range(len(a[i])):
            a[i][j] = randint(-el, el)
    return a


def norma_I(A):
    list_max = []
    for j in range(len(A)):
        SUM = 0
        for i in range(len(A)):
            SUM += abs(A[i][j])
        list_max += [SUM]

    return max(list_max)


def norma_II(A):
    list_max = []
    for i in range(len(A)):
        SUM = 0
        for j in range(len(A)):
            SUM += abs(A[i][j])
        list_max += [SUM]

    return max(list_max)


def norma_III(A):
    SUM = 0
    for i in range(len(A)):
        for j in range(len(A)):
            SUM += A[i][j] * A[j][i]

    return SUM ** 0.5


a = creat_mat(5, 5, 10)

A = [[1, -2],
     [3, 4]
     ]

PrintMat(A)
print()

res_a_I = norma_I(A)
res_a_II = norma_II(A)
res_a_III = norma_III(A)

print('I norm: %3d' % res_a_I)
print('II norm: %2d' % res_a_II)
print('III norm: %.3f' % res_a_III)
