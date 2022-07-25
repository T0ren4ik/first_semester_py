def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-4d" % el, end="")
        print()



def A_B(A, B):
    res = []
    for s in range(len(A[0])):
        p_res = 0
        for i in range(len(A[0])):
            for j in range(len(B)):
                p_res += A[s][i] * B[j][s]
        res += [p_res]

    return res


A = [[5, 6],
     [1, 0],
     ]

B = [[1, 5],
     [0, 6],
     ]

print(A_B(A, B))
