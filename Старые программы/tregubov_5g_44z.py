from sympy import *
n = int(input("n = "))
x = float(input("x = "))
p = 1

for i in range(1, n+1):
    y = i / (i + 1) - cos(abs(x)) ** i
    p *= y
print("for p = ", p)

i = Symbol("i")
P = Product((i / (i + 1) - cos(abs(x)) ** i), (i, 1, n)).evalf()
print("sympy P = ", P)
