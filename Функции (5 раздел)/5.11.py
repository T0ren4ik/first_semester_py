def KkMm(m, a, k = 2):
    SUM = 0

    for i in a:
        if (i % k == 0) and (i < m):
            SUM += i

    return SUM


a_ = [int(i) for i in input("a >>> ").split()]
k_ = int(input("k >>> "))
m_ = int(input("M >>> "))

SUM_ = KkMm(m_, a_, k_)

print(SUM_)
