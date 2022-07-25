def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4s" % el, end="")
        print()


n = int(input("N >>> "))


a = [""] * (2*n + 1)
for i in range(2*n + 1):
    a[i] = [""] * (2*n + 1)
    for j in range(2*n + 1):
        if len(a) // 2 == i or len(a) // 2 == j or i == 0 or j == 0 or j == 2 * n or i == 2 * n:
            a[i][j] = "*"
PrintMat(a)
print()


a = [""] * (2*n + 1)
for i in range(2*n + 1):
    a[i] = [""] * (2*n + 1)
    for j in range(2*n + 1):
        if i == j or i + j == 2 * n:
            a[i][j] = "*"

PrintMat(a)
print()



a = [""] * (2*n + 1)
for i in range(2*n + 1):
    a[i] = [""] * (2*n + 1)
    for j in range(2*n + 1):
        if i == j or i + j == 2 * n or len(a) // 2 == i or len(a) // 2 == j:
            a[i][j] = "*"

PrintMat(a)
print()