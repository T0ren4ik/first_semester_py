from sympy import *

i = 1
a = 1 / i / (i + 1)
EPS = 1e-5
sum_ = 0

while a >= EPS:
    sum_ += a
    i += 1
    a = 1 / i / (i + 1)

var('i')
S = Sum(1 / i / (i + 1), (i, 1, oo)).evalf()

print('s = %.2f \nS = %.2f' % (sum_, S))


