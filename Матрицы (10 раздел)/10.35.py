def PrintMat(a):
    for el in a:
        print("%+-4d" % el, end="")
    print()

def a_b(A, b):
    A_b = []

    for i in range(len(A)):
        p_res = 0
        for j in range(len(A[i])):
            p_res += A[i][j] * b[j]

        A_b += [p_res]

    return A_b


A_ = [[5, 6, 7],
      [1, 0, 4],
      ]

b_ = [1, 2, 3]

a_ym_b = a_b(A_, b_)

PrintMat(a_ym_b)

print(max(a_ym_b))
