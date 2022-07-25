a = [int(s) for s in (input(">>>")).split()]


flag = False
i = 0


while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] % 10 == a[j] % 10:
            flag = True
        j += 1
    i += 1


print(flag)
