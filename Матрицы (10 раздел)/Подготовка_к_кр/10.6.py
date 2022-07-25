def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def form_mat(n, nam):
    h_w = 2 * n
    a = [0] * h_w
    if nam == 2:
        for i in range(h_w):
            a[i] = [0] * h_w
            for j in range(h_w):
                A = i < n
                B = j < n
                a[i][j] = 1 if A and B else 4
                if not A and B:
                    a[i][j] = 3
                if A and not B:
                    a[i][j] = 2
    else:
        for i in range(h_w):
            a[i] = [0] * h_w
            for j in range(h_w):
                A = i < n
                B = j < n
                a[i][j] = 1 if A and B else 3
                if not A and B:
                    a[i][j] = 4
                if A and not B:
                    a[i][j] = 2

    return a


pres_mat = form_mat(2, 1)
print_mat(pres_mat)


def return_mat(a):
    n = len(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            A = i < n // 2
            B = j < n // 2
            if A and B:
                a[i][j], a[n + i - 2][n + j - 2] = a[n + i - 2][n + j - 2], a[i][j]
    return a


res_mat = return_mat(pres_mat)
print_mat(res_mat)
