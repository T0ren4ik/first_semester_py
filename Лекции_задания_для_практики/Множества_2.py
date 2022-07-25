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


m = {i for i in range(10, 50, 3)}
print(eratosfen(m))
