def Replase(A):
    MAX = A[0]
    index = 0
    for i in range(1, len(A)):
        if A[i] > MAX:
            MAX = A[i]
            index = i
    A[index], A[0] = A[0], A[index]
    return A


A = [int(s) for s in (input(">>>")).split()]

A = Replase(A)

print(A)
