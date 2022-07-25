def PrintMat(a):
    for el in a:
        print("%+-4d" % el, end="")


A = [[1, 5],
     [0, 6],
     [4, 7]
     ]
b = [1, 2, 3]

A_b = []

i = 0
for j in range(len(A[i])):
    p_res = 0
    for i in range(len(A)):
        p_res += A[i][j] * b[i]

    A_b += [p_res]

PrintMat(A_b)
