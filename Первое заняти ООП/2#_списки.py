def del_(a):
    i = 0
    flag = False
    while i < len(a) and not flag:
        count = 0
        j = 0

        while j < len(a) and not flag:
            if i != j and a[i] % a[j] == 0:
                count += 1
            j += 1

        flag = count == len(a) - 1

        i += 1

    return flag


a = [6, 72, 18, 36]
res = del_(a)

print(res)


