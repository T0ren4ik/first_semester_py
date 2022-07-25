def F(P, n):
    if P[0] <= n:
        r = P.count(P[0])
        z = 0
        for i in range(r):
            z += 1
        print(P[z-1])
        F(P[r:], n)


L = [2, 2, 3, 3, 3, 4, 4, 4, 4]
n = L[0] + int(input('n >>> ')) - 1
F(L, n)
