def inputArr():
    n = int(input("Введите n:"))
    k = (2 * n + 1)
    a = [0] * k
    for i in range(k):
        a[i] = [0] * k
    return a


def printArr(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


a = inputArr()
printArr(a)
print("__"*10)

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j :
            a[i][j] = "*"
        if i + j == 6:
            a[i][j] = "*"
        if (i == len(a) // 2) or (j == len(a) // 2):
            a[i][j] ="*"
        if a[i][j] == 0:
            a[i][j] = " "

printArr(a)
