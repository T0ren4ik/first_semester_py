def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def ed_mat_n(n):
    a = [0] * n
    for i in range(n):
        a[i] = [0] * n
        for j in range(n):
            a[i][j] = 1 if i == j else 0

    return a


n = int(input("n >>> "))
res_mat = ed_mat_n(n)
print_mat(res_mat)
