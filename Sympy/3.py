from sympy import gcd


def NOD_D(n, m):
    if m > n:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n


n_ = int(input("n >>> "))
m_ = int(input("m >>> "))
k_ = int(input('k >>> '))
res = NOD_D(k_, NOD_D(n_, m_))

resS = gcd(n_, gcd(m_, k_))

print(f'НОД {n_, m_, k_} = {res}')
print(f'НОД в семпае: ', resS)
