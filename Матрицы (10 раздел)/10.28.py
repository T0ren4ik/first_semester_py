a = [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]
     ]


i = 0
j = 0
flag = True
while i < len(a) and flag:
    j = 0
    while j < len(a[i]) and flag:
        flag = a[i][j] == a[0][0]
        j += 1
    i += 1

print(flag)
