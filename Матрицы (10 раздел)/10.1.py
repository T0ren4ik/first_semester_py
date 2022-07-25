def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4d" % el, end="")
        print()


# ----------------------------------
N = 3
A = [[N * i + j + 1 for j in range(N)] for i in range(N)]

PrintMat(A)
print()


A1 = [[N * i - j for j in range(N)] for i in range(N, 0, -1)]
PrintMat(A1)
print()

A2 = [[i + j * N for j in range(N)] for i in range(1, N + 1)]
PrintMat(A2)
print()

A3 = [[N * j - i for j in range(N, 0, -1)] for i in range(N)]
PrintMat(A3)
print()

A4 = [0] * N
for i in range(N):
    A4[i] = [0] * N
    for j in range(N):
        F = int(i % 2 == 0)
        nF = int(not(i % 2 == 0))
        A4[i][j] = (N * i + j + 1) * F + (N * (i + 1) - j) * nF

PrintMat(A4)
print()
