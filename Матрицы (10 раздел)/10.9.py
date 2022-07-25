def PrintMat(a):
    for row in a:
        for el in row:
            print("%+-.1f" % el, end="  ")
        print()


a = [[3, 3, 3],
     [-1, 0, 6],
     [0, -1, -9]
     ]
v_s = []

PrintMat(a)
print()
for i in range(len(a)):
    p_max = max(a[i])
    v_s += [p_max]
    if p_max:
        for j in range(len(a[i])):
            a[i][j] /= p_max
    else:
        a[i] = [0] * len(a[i])

PrintMat(a)
print()
print(v_s)

