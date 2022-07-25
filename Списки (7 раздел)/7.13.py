a = [3, 9, 12, 3, 54, 64]

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] * a[i] == a[j] and a[i] not in a[0: i]:
            print(a[i], a[j])
