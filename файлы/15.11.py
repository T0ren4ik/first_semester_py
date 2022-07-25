def PrintMat(a):
    for row in a:
        for el in row:
            print("%-4s" % el, end="")
        print()


with open('InputMatrix.txt') as f:
    n = int(f.readline(1))
    L = f.readlines()
    L = L[1:]
    for i in range(n):
        L[i] = L[i][:-1]
    print(L)

for j in range(len(L)):
    L[j] = L[j].split()

PrintMat(L)

alf = 2

for i in range(len(L)):
    for j in range(len(L[0])):
        L[i][j] = str(int(L[i][j]) * alf)

with open('OutputMatrix.txt', 'w') as f1:
    f1.write(str(len(L)) + '\n')
    for i in range(len(L)):
        for j in range(len(L[0])):
            f1.write(L[i][j] + ' ')
        f1.write('\n')
