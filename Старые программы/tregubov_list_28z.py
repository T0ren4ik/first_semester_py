def Replase (A):
    for i in range(0, len(A)-1, 2):
        A[i], A[i+1] = A[i+1], A[i]
    return A


A = [int(s) for s in (input(">>>")).split()]
Replase(A)

print(A)


# -------------------------------------------
print("--"*15)


A = [int(s) for s in (input(">>>")).split()]
