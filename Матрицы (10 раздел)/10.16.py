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

# поменять строки

# st_i = int(input("1st >>> "))
# st_i1 = int(input("2st >>> "))
st_i = 0
st_i1 = 2

a[st_i1], a[st_i] = a[st_i], a[st_i1]
PrintMat(a)
print()

# поменять столбцы

# stol_p = int(input("1solb >>> "))
# stol_p1 = int(input("1stlb >>> "))
stol_p = 0
stol_p1 = 1

for i in range(len(a)):
    a[i][stol_p], a[i][stol_p1] = a[i][stol_p1], a[i][stol_p]

PrintMat(a)
