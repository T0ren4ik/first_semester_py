def eratosfen(set0):
    set_p = set()
    n = max(set0)
    sieve = set(range(2, n + 1))
    while sieve:
        ntx = min(sieve)
        if ntx in set0:
            set_p.add(ntx)
        sieve -= set(range(ntx, n + 1, ntx))

    return set_p


def ab(n, b):
    a = set()
    x = b
    a.add(x)
    for i in range(1, n):
        x = x + int(2/3*i)
        a.add(x)

    return a


n_ = 5
b_ = 3

set_a = ab(n_, b_)

print(set_a)

# поиск простых числео в множестве а
# ================================

set_pr = eratosfen(set_a)

print(set_pr)

