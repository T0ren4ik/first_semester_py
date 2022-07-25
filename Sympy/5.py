from sympy import Matrix, ask, Q, Integer


def mm(n, m):
    print('Ведите все элементы')
    L = [i for i in input('>>> ').split()]
    res = Matrix(n, m, L)

    return res


def s_v_p(MAT):
    zn = MAT[:]
    SUM = 0
    for el in zn:
        if ask(Q.real(el) & Q.positive(el)):
            SUM += el

    return SUM


# n = int(input('n >>> '))
# n = int(input('m >>> '))

n = 2
m = 2
M = mm(n, m)

print(M)

res = s_v_p(M)
if ask(Q.integer(res)):
    print(f'Сумма положительных и вещественных чисел: {res}')
else:
    print(f'Сумма положительных и вещественных чисел: {res : .4}')

# 1 2 3 f g h 0.5 -0.6 0.5
# 1 2 3 True False r 0.6 0.6 -0.6
# 1 2 3 g t h -0.6 -0.5 -0.6
