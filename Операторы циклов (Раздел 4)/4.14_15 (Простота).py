def Prostota(n):
    if n != 1 and n != 2:
        d = 2
        flag = True
        while n >= d*d and flag:
            flag = n % d != 0
            d += 1
        return flag
    else:
        return False


m = []

for i in range(100, 200 + 1):
    if Prostota(i):
        m.append(i)
        