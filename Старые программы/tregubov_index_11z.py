A = [53, 44, 40, 39, 37, 23, 21, 18, 16, 15, 13, 10, 8, 7, 3]
T = int(input(">>>"))

p = 0
q = len(A)-1

print("Разыскиваемый элемент %d" % T)
print("s  |   A[s]  |   A[s] < T   |   p  |   q  |  p != q")


while p != q:
    s = (p + q) // 2
    if A[s] > T:
        p = s + 1
    else:
        q = s
    print("%-3d|  %3d    |    %5s     | %3d  | %3d  |  %5s    " % (s, A[s], (A[s] < T), p, q, (p != q)))

if A[q] == T:
    print("A[%d] =  " % q, T)
else:
    print("Элемента нет")


print("--" * 28)
# ----------------------------------------------------------------------------------------------------------------

print("Разыскиваемый элемент %d" % T)
print("s  |   A[s]  |   A[s] < T   |   p  |   q  |  p != q")
s = (p + q) // 2

while p != q and A[s] != T:
    s = (p + q) // 2
    if A[s] > T:
        p = s + 1
    else:
        q = s
    print("%-3d|  %3d    |    %s     | %3d  | %3d  |  %s    " % (s, A[s], bool(A[s] < T), p, q, bool(p != q)))

if A[q] == T:
    print("A[%d] =  " % q, T)
elif A[s] == T:
    print("-  |   -   |      -     |  -  |   -   |   -     ")
    print("A[%d] =  " % s, T)
else:
    print("Элемента нет")

