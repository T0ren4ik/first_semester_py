def NOD_M(n, m):
    while n != m:
        if m > n:
            m, n = n, m - n
        else:
            m, n = n - m, m

    return m


def NOD_D(n, m):
    if m > n:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n


n_ = int(input("n >>> "))
m_ = int(input("m >>> "))
res = NOD_M(n_, m_)
res1 = NOD_D(n_, m_)

print(res, res1)

# -----------------------------------------------
# 4.10
k_ = int(input("k >>> "))

print(NOD_D(NOD_D(n_, m_), k_))