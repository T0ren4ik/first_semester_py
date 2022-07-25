i1 = int(input(">>>"))
i2 = int(input(">>>"))
a = [int(s) for s in (input(">>>")).split()]


for i in range(i1+1, i2+1):
    y = a[i]
    j = i - 1
    print("y   |   j ")
    print("%-4d|%4d" % (y, j))
    print("условие| a[j+1] | a[j] | j ")
    while (j >= i1) and (y < a[j]):
        a[j+1] = a[j]
        j = j - 1
        print("%-7s|%-8d|%-6d%-3d" % (bool((j >= 0) and (y < a[j])), a[j+1], a[j], j))
    a[j+1] = y


print()
print(a)
