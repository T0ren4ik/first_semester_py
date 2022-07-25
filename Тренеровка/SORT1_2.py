a = [int(i) for i in (input("el >>> ")).split()]

for i in range(len(a) - 1, 0, -1):
    imax = 0
    for j in range(i + 1):
        if a[j] > a[imax]:
            a[j], a[imax] = a[imax], a[j]
    a[i], a[imax] = a[imax], a[i]
print(a)


a1 = [int(i) for i in (input("el >>> ")).split()]

for i in range(len(a1)):
    for j in range(0, len(a1) - i - 1):
        if a1[j] > a1[j + 1]:
            a1[j], a1[j + 1] = a1[j + 1], a1[j]

print(a1)
