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


def max_sum(a):
    sum_str = []
    for i in range(len(a)):
        p_sum = 0
        for j in range(len(a[i])):
            p_sum += a[i][j]

        sum_str += [p_sum]

    res = max(sum_str)
    return res


a = creat_mat(4, 3)
print_mat(a)

res = max_sum(a)
print(res)
