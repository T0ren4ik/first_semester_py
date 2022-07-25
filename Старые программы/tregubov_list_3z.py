def Input(s):
    A = s.split()
    return A


s = input('Введите числа через пробел:')
A = Input(s)


def Print(A):
    count = 0
    for i in A:
        if int(i) % 2 == 0:
            count += 1
    return count


res = Print(A)
print(res)



