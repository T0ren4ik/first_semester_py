from sympy import *

n = int(input("n >>> "))
z = -1
SuM = 0

for i in range(1, n + 1):
    a = z / (2 * i + 1)
    SuM += a
    z = -z

var('i')
S = Sum((-1)**i / (2 * i + 1), (i, 1, n)).evalf()

print('S_for = %.5f, S_sym = %.5f' % (SuM, S))
