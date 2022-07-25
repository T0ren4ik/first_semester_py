from sympy import primerange


def Prostota(n):
    if n != 1:
        d = 2
        flag = True
        while n >= d*d and flag:
            flag = n % d != 0
            d += 1
        return flag
    else:
        return False


n = int(input("n >>> "))
m = int(input("m >>> "))

L = []
for i in range(n, m + 1):
    if Prostota(i):
        L += [i]


LS = primerange(n, m+1)

print(f'Простые числа в диапазоне[{n},{m}]: {str(L)[1: -1]} \n')

print(f'Простые числа в диапазоне[{n},{m}]:', str(list(LS))[1:-1], '\n')

print('совпадают с проверкой в sympy')
