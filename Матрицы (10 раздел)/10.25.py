def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4s" % el, end="")
        print()


def Del_stoldeu(a, j):
    for i in range(len(a)):
        a[i].pop(j)
#       del(a[j][i])
    return a


def C_0(a):
    j = 0
    i = 0
    while j < len(a[i]):
        flag = True
        while i < len(a) and flag:
            if a[i][j] == 0:
                a = Del_stoldeu(a, j)
                flag = False
            else:
                i += 1

        if flag:
            j += 1
        i = 0


    return a


A = [[1, 1, 0, 1],
     [0, 1, 1, 1],
     [1, 7, 1, 6],
     [0, 2, 4, 0]
     ]

PrintMat(A)
print()

A = C_0(A)

PrintMat(A)
