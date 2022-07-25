from sympy import divisors, primerange


def D():
    try:
        n = int(input('n >>> '))
        assert n > 0
    except (ValueError, AssertionError):
        print('Вы ввели не число')
        n = D()

    return n


n = D()
LD = divisors(n)
LP = primerange(2, n)

res = list(set(LD) & set(LP))

print(f'Простые дилители числа: {n}', str(res)[1: -1])
