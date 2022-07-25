def MIN(a):
    '''
      a = list(a)
      a.sort()
      return a[0]
    '''
    a = list(a)
    Min = a[0]
    for i in a:
        if i < Min:
            Min = i
    return Min


def MAX(a):
    a = list(a)
    a.sort()
    return a[-1]


def eratosfen(set0):
    set_p = set()
    n = MAX(set0)
    sieve = set(range(2, n + 1))
    while sieve:
        ntx = MIN(sieve)
        if ntx in set0:
            set_p.add(ntx)
        sieve -= set(range(ntx, n + 1, ntx))

    return set_p


m = {i for i in range(10, 50)}

print(len(eratosfen(m)))
print(eratosfen(m))
