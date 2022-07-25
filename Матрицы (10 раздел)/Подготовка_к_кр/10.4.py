def print_mat(a):
    for row in a:
        for el in row:
            print("%2s" % el, end=" ")
        print()
    print()


# n = int(input("n >>> "))
n = 3
i_j = 2 * n + 1

# c
a = [""] * i_j
for i in range(i_j):
    a[i] = [""] * i_j
    for j in range(i_j):
        a[i][j] = "*" if (i - j == 0) or (j + i + 1 == i_j) or n in (i, j) else ""

print_mat(a)


# b
a = [""] * i_j
for i in range(i_j):
    a[i] = [""] * i_j
    for j in range(i_j):
        a[i][j] = "*" if (i - j == 0) or (j + i + 1 == i_j) else ""

print_mat(a)


# a
a = [""] * i_j
for i in range(i_j):
    a[i] = [""] * i_j
    for j in range(i_j):
        a[i][j] = "*" if j in (0, n, 2*n) or i in (0, n, 2*n) else ""


print_mat(a)
