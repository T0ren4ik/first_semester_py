import random


def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def creat_mat(m, n):
    a = [0] * m
    for i in range(m):
        a[i] = [0] * n
        for j in range(n):
            a[i][j] = random.randint(-9, 9)

    return a


def max_sum_str(a):
    sum_str = []
    for i in range(len(a)):
        p_sum = 0
        for j in range(len(a[i])):
            p_sum += a[i][j]

        sum_str += [p_sum]

    MAX = sum_str[0]
    ind = 0
    for i in range(len(sum_str)):
        if MAX < sum_str[i]:
            MAX = sum_str[i]
            ind = i

    return ind


def min_sun_stolb(a):
    i = 0
    sum_stolb = []
    for j in range(len(a[i])):
        sum_j = 0
        for i in range(len(a)):
            sum_j += a[i][j]

        sum_stolb += [sum_j]



    MIN = sum_stolb[0]
    ind = 0
    for j in range(len(sum_stolb)):
        if MIN > sum_stolb[j]:
            MIN = sum_stolb[j]
            ind = j

    return ind


A = creat_mat(3, 4)
print_mat(A)

el_i = max_sum_str(A)
el_j = min_sun_stolb(A)


res = A[el_i][el_j]

print(res, el_i, el_j)

