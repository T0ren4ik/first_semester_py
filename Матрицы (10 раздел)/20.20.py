def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4s" % el, end="")
        print()


def A_0(a):
    i = 1
    while i < len(a):
#        print(i, a[i], (0 in a[i]))

        if 0 in a[i]:
            a[i: i] = [a[0]]
            i += 1
        i += 1

    return a


A = [[1, 1, 1, 1],
     [1, 4, 0, 1],
     [0, 7, 1, 6],
     [1, 2, 4, 5]
     ]

PrintMat(A)
print()

res = A_0(A)

PrintMat(res)
