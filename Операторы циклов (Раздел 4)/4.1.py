from math import sqrt

b = float(input("b >>> "))

a = b
i = 1

print('i  |a      |Условие')
print('%-3d|%+-7.2f|%-7s' % (i, a, a >= 0))
while a >= 0:
    i += 1
    a = a - i / sqrt(i - 1)
    print('%-3d|%+-7.2f|%-7s' % (i, a, a >= 0))

print(a)
