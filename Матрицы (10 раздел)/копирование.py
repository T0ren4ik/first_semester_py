a = [[1, 2],
     [1, 2]
     ]


b = [[a[i][j] for j in range(len(a[i]))] for i in range(len(a))]

a[0][0] = 0
print(a)
print(b)
