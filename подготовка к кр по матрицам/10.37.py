def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-4d" % el, end="")
        print()


def A_B(a, b):
    if len(a[0]) == len(b):
        res_m = [0] * len(a)

        for s in range(len(a)):
            res_m[s] = [0] * len(b[0])

            p_res = 0
            for i in range(len(a[0])):

                for j in range(len(b)):
                    p_res += a[i][s] * b[s][i]
                res_m[s][i] = p_res

    else:
        res_m = "Error"
    return res_m


A_ = [[5, 6, 6],
      [1, 0, 4],
      ]

b_ = [[1, 3, 3],
      [1, 2, 3],
      [1, 2, 3]
      ]


res = A_B(A_, b_)

print(res)
PrintMat(res)
