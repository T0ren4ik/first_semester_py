from sympy import *
from math import log
eps = 1e-10
print("eps = 1e-10 ,n - нет, enter = да >>>")
F = bool(input())

if F:
    c = int(input("Введите количество цифр после запятой "))
    eps = 10 ** (- c)
else:
    eps = 1e-10
x = float(input("Введите x "))


def SUM(x, eps):
    n = 0
    i = 3
    s = 0
    y = x
    while abs(y) >= eps:
       s += y
       n += 1
       y *= x * x / i
       i += 2

    i = Symbol("i")
    SS = Sum((x ** (2 * i - 1)) / (2 * i - 1), (i, 1, oo)).evalf()

    S = 0.5 * log((1 + x) / (1 - x))
    return s, n, SS, S, eps


s, n, SS, S, eps = SUM(x, eps)

print("x >>> ", x)
print("eps >>> ", eps)
print("sum = ", s)
print("n = ", n)
print("Проверка")
print("sympy:", SS)
print("F(x) = ", S)
