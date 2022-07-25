import random


def print_mat(a):
    for row in a:
        for el in row:
            print("%4d" % el, end=" ")
        print()
    print()


def creat_mat():
    n = 2
    a = [0] * n
    for i in range(n):
        a[i] = [0] * n
        for j in range(n):
            a[i][j] = random.randint(0, 9)

    return a


a1 = creat_mat()
a2 = creat_mat()
print_mat(a1)
print_mat(a2)

n = 2
res_mat = a1[:]
for i in range(n):
    for j in range(n):
       res_mat[i][j] = a1[i][j] + a2[i][j]

print_mat(res_mat)

