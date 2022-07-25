from math import sin, sqrt, cos

x = float(input("x >>> "))
y = float(input("y >>> "))
z = float(input("z >>> "))

T = z*z + x*x/4
v = cos(T)
u = sin(abs(y - sqrt(abs(x))) * (x - y / T))

print("V = %.2f, U = %.2f" % (v, u))
