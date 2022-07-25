L = [1, 2, 1, 2, 1, 2, 1]
el = set(L)

count = {}
for i in el:
    count[i] = L.count(i)

print(count)
