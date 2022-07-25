def FOR_N(n = 30):
    x = 1 / 2
    SUM = x

    for i in range(2, n + 1):
        x = x * (-2) / (i + 1)
        SUM += x

    return SUM


print("SUM = %.5f" % FOR_N())
print("SUM = %.5f" % FOR_N(2))
