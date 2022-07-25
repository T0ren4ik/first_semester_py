a = []

for i in range(len(a) - 1, 0, -1):
    imax = 0
    for j in range(0, i + 1):
        if a[j] > a[imax]:
            imax = j
    a[i], a[imax] = a[imax], a[i]

# -------------------------------------\

for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

# -------------------------------------\
