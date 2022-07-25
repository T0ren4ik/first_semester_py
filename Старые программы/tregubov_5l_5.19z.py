def p(n, b1, q):
    #  считаю Bn
    y = b1
    for i in range(1, n):
        y *= q
    return (abs(b1 * y)) ** (n / 2)


n = int(input("n = "))
b1 = float(input("b1 = "))
q = float(input("q = "))


composition = p(n, b1, q)

print(composition)
