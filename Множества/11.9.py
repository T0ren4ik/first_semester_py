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


def zet_pros_z(a):
    sp = list(a)
    sp.sort()
    res_ = []
    for i in range(0, len(a), 4):
        k = len(str(sp[i])) - 1
        d = int('1' + '0' * k)

        if i < len(sp) - 4:
            des = set()
            for j in range(i, i + 4):
                des.add(sp[j] // d)

            if des == {sp[i] // d}:
                res_ += [sp[i: i + 4]]

    return res_


m = {i for i in range(10, 100)}

r = eratosfen(m)
print("Простые числа: ", r)

res = zet_pros_z(r)

print("Четверки меньших 𝑛 простых чисел, принадлежащих одному десятку:", res)
