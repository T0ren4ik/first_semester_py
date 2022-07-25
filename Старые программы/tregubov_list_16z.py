def Input(s):
    A = s.split()
    return A


s = input('Введите числа через пробел:')
A = Input(s)


def Print(A):
    F = A[:]
    i = 0
    while i < len(F):
        if int(F[i]) % 2 == 0:
            F.pop(i)
        else:
            i += 1
    return F


print(Print(A))