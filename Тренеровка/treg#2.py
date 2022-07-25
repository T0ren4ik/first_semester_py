a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
k = 2
n = 5
sUm = []


for j in range(n):
    SUM_K = 0
    i = 0
    while i < len(a) and i < k:
        SUM_K += a[i]
        i += 1
    sUm += [SUM_K]
    a = a[k:]

print(sUm)

res = max(sUm)
print(res)