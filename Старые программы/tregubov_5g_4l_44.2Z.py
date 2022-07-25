from sympy import *
n = int(input("n = "))
s = 0

for i in range(1, n + 1):
    y = (-1)**(i + 1) / (i*(i + 1))
    s += y
print("s = %.15f" % s)

i = Symbol("i")
S = Sum((-1)**(i + 1) / (i*(i + 1)), (i, 1, n)).evalf()
print("S = ", S)
