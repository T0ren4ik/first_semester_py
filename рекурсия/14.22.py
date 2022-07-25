def Prostota(n):
    d = 2
    flag = n != 1
    while n >= d*d and flag:
        flag = n % d != 0
        d += 1
    return flag



def rec(L):
    if len(L) == 0:
        print(False)
    elif Prostota(L[0]):
        print(True)
    else:
        rec(L[1:])


L = [1, 6, 12, 9, 8, 55, 48]
rec(L)
