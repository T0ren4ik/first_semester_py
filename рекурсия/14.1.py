def x_1(n):
    if n == 1:
        return 1
    else:
        return x_1(n-1) + 2


def x_5(n):
    if n == 3:
        return 0
    elif n == 2:
        return -2
    elif n == 1:
        return 1
    else:
        return 2*x_5(n-1) * x_5(n-1) - x_5(n-2) * x_5(n-2) - x_5(n-3)

# n = int(input('n >>> '))
n = 2

print('x_1')
for i in range(1, 5):
        res_1 = x_1(i)
        print('x' + str(i), " = ", res_1)

print()
print('x_5')
for i in range(1, 5):
        res_5 = x_5(i)
        print('x' + str(i), " = ", res_5)

