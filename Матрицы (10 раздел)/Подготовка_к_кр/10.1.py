def print_mat(a):
    for row in a:
        for el in row:
            print(el, end=" ")
        print()
    print()


# 1
n = 3
a = [0] * n
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = i * 2 + j + 1 + i

print_mat(a)

# 2
n = 3
a = [0] * 3
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = 9 - j - i * n

print_mat(a)

# 3

n = 3
a = [0] * 3
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = i + 1 + j * n

print_mat(a)

# 4

n = 3
a = [0] * 3
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = 9 - i - j * n

print_mat(a)

# 5

n = 3
a = [0] * 3
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = (i * n + j + 1) * (i // 2 or i == 0) + (n * n - j - n * i) * (i % 2)

print_mat(a)
