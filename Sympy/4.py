from sympy import solve, im, re
import math


def x_i(A, D):
    p1 = str(-A[1] / 2 / A[0])
    p2 = str(math.sqrt(-D) / 2 / A[0])
    x1 = f'{p1} + {p2:.5}i'
    x2 = f'{p1} - {p2:.5}i'
    zn = [[p1, p1], [p2, '-'+p2]]

    return x1, x2, zn


def x_n(A):
    D = (A[1]*A[1] - 4 * A[0] * A[2])
    if D > 0:
        x1 = (-A[1] + math.sqrt(D)) / 2 * A[0]
        x2 = (-A[1] - math.sqrt(D)) / 2 * A[0]
        zn = [[x1, x2], 0]
        return x1, x2, zn
    elif D == 0:
        x1 = (-A[1] + math.sqrt(D)) / 2 * A[0]
        zn = [x1, 0]
        return x1, x1, zn
    else:
        x1, x2, zn = x_i(A, D)
        return x1, x2, zn


def D():
    try:
        print('Введите коэфициенты через пробел')
        a = [int(i) for i in input('>>> ').split()]
        assert a[0] != 0
    except (AssertionError, ValueError):
        print('Вы ввели 0 при x^2. Это не квадратный трехчлен')
        a = D()
    return a


a = D()
f = f'{a[0]}*x**2 + {a[1]}*x + {a[2]} \n'
print(f)

print('Вычисление по формулам:')
res_f = x_n(a)
print(f'{res_f[:2]} \n')
print(f'Вещественная часть:{res_f[2][0]} \nКомплексная часть:{res_f[2][1]} \n')
print('=='*30 + '\n')


print('Вычисление в Sympy:')
res_s = solve(f)
print(res_s)
print()
if len(res_s) == 1:
    vv = [re(res_s[0])]
    rr = [im(res_s[0])]
else:
    vv = [re(res_s[0]), re(res_s[1])]
    rr = [im(res_s[0]), im(res_s[1])]
print(f'Вещественная часть:{vv} \nКомплексная часть:{rr}')
