from random import randint

def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-.1f" % el, end="  ")
        print()


def creat_mat(m, n, el):
    a = [0] * m
    for i in range(len(a)):
        a[i] = [0] * n
        for j in range(len(a[i])):
            a[i][j] = randint(-el, el)
    return a


m_ = 3
n_ = 4
el_ = 10
a = creat_mat(m_, n_, el_)

PrintMat(a)
print()

# среднее для каждого столбца

cr_ct = []
j = 0
i = 0
for j in range(len(a[i])):
    pr_cr_zn = 0
    for i in range(len(a)):
        pr_cr_zn += a[i][j]

    cr_ct += [pr_cr_zn / m_]

print(cr_ct)



