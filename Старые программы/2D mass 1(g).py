a = [0]*3
k = 9
for i in range(3):
    a[i] = [0]*3
    for j in range(len(a[i])):
        a[i][j] = k
        k -= 1

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
