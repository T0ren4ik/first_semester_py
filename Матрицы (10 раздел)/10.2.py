def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4d" % el, end="")
        print()


N = 6

A = [0] * N
for i in range(N):
    A[i] = [0] * N
    for j in range(N):
        A[i][j] = abs(j - i) + 1

PrintMat(A)

