A = [int(s) for s in (input(">>>")).split()]

count = 0
Max_Len = 0
I = -1
j = 0

while j < len(A):
    if A[j] < 0:
        j += 1
        while j < len(A) and A[j] < 0:
            count += 1
            j += 1
    if A[j] > 0:
        j += 1
        while j < len(A) and A[j] < 0:
            count += 1
            j += 1
    if count > Max_Len:
        Max_Len = count
        count = 0
        I = j


res = A[I - Max_Len:I]
print("Максимальная длина равна %d, срез этой серии:" % Max_Len, res)
