def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


n = 3
a = [0] * n
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = i * n + j + 1

print_mat(a)


for i in range(n):
    for j in range(n):
        a[i][j] = n * n - j - i * n

print_mat(a)


for i in range(n):
    for j in range(n):
        a[i][j] = 1 + i + j * 3

print_mat(a)


for i in range(n):
    for j in range(n):
        a[i][j] = n * n - i - j * 3

print_mat(a)


for i in range(n):
    for j in range(n):
        a[i][j] = (n * n - j - i * n) if (i % 2) else 1 + j + i * n

print_mat(a)
