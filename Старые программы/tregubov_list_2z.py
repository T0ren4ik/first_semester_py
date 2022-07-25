t = float(input(">>>"))
n = int(input(">>>"))

a = [int(s) for s in (input(">>>")).split()]
Fx = 0
F_x = 0

for i in range(n):
    Fx += a[i]*t**n
    F_x += n*a[i]*t**(n-1)
    n -= 1
Fx += a[-1]

print("Значение функции = %d и значение производной = %d,в точке %d " % (Fx, F_x, t))
