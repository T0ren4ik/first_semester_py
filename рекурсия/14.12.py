def posl(a, i=0):
    if i == len(a) - 1:
        return True
    elif a[i] < a[i+1]:
        return True & posl(a, i+1)
    else:
        return False


A = [[1, 4, 3, 5, 6], [1, 4, 6, 8, 9], [0, 1, 1, 2, 5]]

for i in A:
    res = posl(i)

    print(res)
