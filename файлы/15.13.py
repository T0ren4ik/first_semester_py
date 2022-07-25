with open('13.txt') as f:
    L = f.readlines()

print(L)
with open('13.txt', 'w+') as f1:

    n = 3
    if n <= len(L):
        L[n-1:n] = []
        print(L)
        f1.writelines(L)
    else:
        f1.write(L)
        print('Такой строки нет')
