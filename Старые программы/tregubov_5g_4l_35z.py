from math import sqrt
x = -1

print("   x  |  y = F(x)")
print("-----------------")
for i in range(21):
    if x < 0.5:
        print("%+.2f |     -" % x)
    else:
        y = (x * x) / sqrt(2 * x - 1)
        print("%+.2f | %+.4f" % (x, y))
    x += 0.1
