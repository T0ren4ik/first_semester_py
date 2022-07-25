from math import sin

a = float(input('a >>> '))
h = float(input('h >>> '))
xn = float(input('xn >>> '))
xk = float(input('xk >>> '))

x = xn
sum_ = 0
product = 1
count = 0

while x <= xk:
    fx = sin(x - a * a * a) / (a * a + a + 7.3)
    count += 1
    if fx > 0:
        sum_ += fx
    if fx < 0:
        product *= fx

    x += h

print(count, sum_, product)
