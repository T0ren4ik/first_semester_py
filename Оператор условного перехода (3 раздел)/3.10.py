N = int(input("N >>> "))

if N // 100 == 0:
    u1 = N // 10
    u2 = N % 10
    res = u1 + u2

elif N // 1000 == 0:
    u1 = N // 100 if N // 100 != 0 else 1
    u2 = N // 10 % 10 if N // 10 % 10 != 0 else 1
    u3 = N % 10 if N % 10 != 0 else 1
    res = u1 * u2 * u3
else:
    res = "No"

print(res)
