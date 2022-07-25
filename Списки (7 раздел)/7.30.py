# a = [0, 0, 0, 0]
a = [1, 2, 3, 4, -1, -1, 2, 3]

mx_len = 0
i_k = None
for i in range(len(a)):
    if i < len(a) and a[i] > 0:
        przn = 0
        while i < len(a) and a[i] > 0:
            przn += 1
            i += 1

        if przn > mx_len:
            mx_len = przn
            i_k = i

    if i < len(a) and a[i] < 0:
        przn = 0
        while i < len(a) and a[i] < 0:
            przn += 1
            i += 1

        if przn > mx_len:
            mx_len = przn
            i_k = i


if i_k != None:
    print(mx_len, a[i_k - mx_len: mx_len])
else:
    print(mx_len, [])
