a = [int(i) for i in input('>>> ').split()]

Min = a[0]
index = 0
for i in range(1, len(a)):
    if a[i] <= Min:
        Min = a[i]
        index = i

print(Min, index)
