def print_mat(a):
    for row in a:
        for el in row:
            print('%4d' % el, end=" ")
        print()
    print()


n = 6
a = [0] * n
for i in range(n):
    a[i] = [0] * n
    for j in range(n):
        a[i][j] = abs(j - i) + 1


print_mat(a)
