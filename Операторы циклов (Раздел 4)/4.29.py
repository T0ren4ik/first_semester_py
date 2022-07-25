from sympy import *
from math import cosh

x = int(input('x >>> '))

y = 1
i = 0
SyM = 0
count = 0
EPS = 1e-5

while abs(y) >= EPS:
    SyM += y
    count += 1
    i += 1
    y = x * x / (2*i - 1) / 2 / i * y

fx = cosh(x)

var('i')
S = Sum(x**(2 * i) / factorial(2 * i), (i, 0, oo)).evalf()

print('Count = %d')
print("S_Sym = %.5f,  S_wh = %.5f,  fx = %.5f" % (S, SyM, fx))
