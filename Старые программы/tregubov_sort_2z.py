A = [int(s) for s in (input(">>>")).split()]
a = A[:]

for i in range(1, len(a)):
    y = a[i]
    j = i - 1
    print("y   |   j ")
    print("%-4d|%4d" % (y, j))
    print("условие| a[j+1] | a[j] | j ")
    while (j >= 0) and (abs(y) < abs(a[j])):
        a[j+1] = a[j]
        j = j - 1
        print("%-7s|%-8d|%-6d%-3d" % ((abs(y) < abs(a[j])), a[j+1], a[j], j))
    a[j+1] = y

a = a[::-1]
print(a)
