a = [1, 2, 4, 6, 9, 11, 21, 35, 77]
T = int(input(">>> "))
p = 0
q = len(a) - 1

print("Разыскиваемый элемент %d" % T)
print("s  |   A[s]  |   A[s] < T   |   p  |   q  |  p != q")
while p != q:
    s = (p + q) // 2
    if T > a[s]:
        p = s + 1
    else:
        q = s
    print("%-3d|  %3d    |    %5s     | %3d  | %3d  |  %5s    " % (s, a[s], (T > a[s]), p, q, (p != q)))

if a[p] == T:
    print(p)
else:
    print("Элемента нет")
