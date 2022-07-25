from sympy import integrate, var


def integral(f, a, b, n):
    h = (b - a) / n
    xkn = a
    xkk = a + h
    SS = 0

    # центральные
    for i in range(n):
        SS += f((xkn + xkk) / 2)
        xkn += h
        xkk += h
    SS *= h

    xkn = a
    SL = 0
    # Левые
    for i in range(n):
        SL += f(xkn)
        xkn += h

    SL *= h

    xkk = a + h
    SP = 0
    # Правые
    for i in range(n):
        SP += f(xkk)
        xkk += h
    SP *= h

    return SP, SS, SL


F = lambda x: 1 / (1 + x*x)
a_ = 0
b_ = 1
n_ = 4
h_ = (b_ - a_) / n_
EPS = 1e-4

# Левые
countL = 1
N = n_
SIL = integral(F, a_, b_, N*2)[0]
while abs((integral(F, a_, b_, N)[0] - integral(F, a_, b_, N*2)[0]) / 3) > EPS:
    SIL = integral(F, a_, b_, N * 2)[0]
    countL += 1
    N *= 2

print(f'Левые.   Значение: {SIL}, погрешность: {countL}')

# середина
countS = 1
N = n_
SIS = integral(F, a_, b_, N*2)[1]
while abs((integral(F, a_, b_, N)[1] - integral(F, a_, b_, N*2)[1]) / 3) > EPS:
    SIS = integral(F, a_, b_, N * 2)[1]
    countS += 1
    N *= 2

print(f'Средние. Значение: {SIS}, погрешность: {countS}')

# середина
countP = 1
N = n_
SIP = integral(F, a_, b_, N*2)[2]
while abs((integral(F, a_, b_, N)[2] - integral(F, a_, b_, N*2)[2]) / 3) > EPS:
    SIP = integral(F, a_, b_, N * 2)[2]
    countP += 1
    N *= 2

print(f'Правые.  Значение: {SIP}, погрешность: {countP}')

t = 0
var('t')
SSS = integrate(1/(1 + t*t), (t, a_, b_)).evalf()
print("Sympy:", SSS)
