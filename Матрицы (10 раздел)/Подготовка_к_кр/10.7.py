import random


def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def creat_mat():
    n = 3
    a = [0] * n
    for i in range(n):
        a[i] = [0] * n
        for j in range(n):
            a[i][j] = random.randint(0, 9)

    return a


p_res = creat_mat()
print_mat(p_res)

n = 3
for i in range(n):
    for j in range(n):
        p_res[i][j] = -1 if p_res[i][j] == 0 else p_res[i][j]

print_mat(p_res)
