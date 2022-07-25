from sympy import *
a = 1
i = 1
znak = 1
EPS = 1e-5
S = 0

while abs(a) >= EPS:
    S += a
    i += 1
    znak = -znak
    a = 1 / i * znak


var('i')
s = Sum((-1)**(i + 1) * 1 / i, (i, 1, oo)).evalf()

print('s = %.5f \nS = %.5f' % (s, S))
