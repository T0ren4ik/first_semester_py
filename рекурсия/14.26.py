def find_x(f, a, b):
    c = (a + b) / 2
    if abs(f(c)) <= 0.0002:
        print('x = %.4f' % c)
    elif (f(c) >= 0) and (f(a) < 0):
        find_x(f, a, c)
    else:
        find_x(f, c, b)


# F = lambda x: 2*x*x*x - 3.6*x*x - 4.7*x + 3
F = lambda x: x*x*x*x + 2*x*x - x - 1
a = 2
b = 3
if F(a)*F(b) < 0:
    find_x(F, a, b)
else:
    print('Корня нет')
