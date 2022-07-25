a = [s for s in (input(">>>")).split()]
i = 0

while (i < len(a)) and a[i] not in "aeiouyAEIOUY":
    i += 1

print(False if i == len(a) else True)

