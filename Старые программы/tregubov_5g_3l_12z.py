a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
c = float(input("Введите третье число "))
x = (a + b + c)
y = (a*b*c)
print(x if x > y else y)
print((max(x, y)))

n = a**2 + b
m = b**2 + c
print(n if n < m else m)
print(min(m, n))

k = a + b
j = a*b
k1 = b + c
j1 = b*c
r = k if k < j else j
r1 = k1 if k1 < j1 else j1
print(r if r > r1 else r1)
print(max(min(k, j), min(k1, j1)))
