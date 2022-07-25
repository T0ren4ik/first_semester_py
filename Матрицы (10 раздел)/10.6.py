def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4d" % el, end="")
        print()


n = 4

a = [0] * 2 * n
for i in range(2 * n):
    a[i] = [0] * 2 * n
    for j in range(2 * n):
        a[i][j] = i + j

PrintMat(a)
print()
'''
for i in range(N):
    for j in range(N):
        if i < N and j < N:
'''

# I блок с III
for i in range(n):
    for j in range(n):
        a[i][j], a[n+i][n+j] = a[n+i][n+j], a[i][j]


# 2 блок
for i in range(n):
    for j in range(n):
        a[i][n+j], a[n+i][j] = a[n+i][j], a[i][n+j]

PrintMat(a)
