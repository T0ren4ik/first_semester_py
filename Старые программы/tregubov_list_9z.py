def Input(s):
    A = s.split()
    return A


s = input('Введите числа через пробел:')
A = Input(s)


def Print(A):
    count = 0
    Product = 1
    for i in A:
        if int(i) % 2 == 0:
            count += 1
            Product *= int(i)
    return count, Product


C, P = Print(A)
print("Количество четных элементо = %d, произведение = %d" % (C, P))
