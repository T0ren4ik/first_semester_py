def Input(s):
    A = s.split()
    return A


s = input('Введите числа через пробел:')
A = Input(s)


def Print(A):
    Zero = ["0"]
    i = 0
    while i < len(A):
        if int(A[i]) % 2 == 0:
            A = A[0:i+1] + Zero + A[i+1:]
            i += 2
        else:
            i += 1

    return A


print(Print(A))