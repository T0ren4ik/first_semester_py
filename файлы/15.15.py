with open('14.txt', 'r+') as f:
    L = f.readlines()
    r = len(L)
    for i in range(len(L)):
        L[i] = len(L[i])

    for i in range(r-1, 1, -1):
        f.seek(f.tell() - L[i])
        k = f.tell()
        pr_zn = f.readline()
        pr_zn = pr_zn[-2] + pr_zn[1:-2] + pr_zn[0] + '\n'
        f.truncate(k)
        f.readline(pr_zn)
        f.seek(f.tell() - L[i] - 1)

    f.seek(f.tell() - L[i])
    pr_zn = f.readline()
    pr_zn = pr_zn[-2] + pr_zn[1:-2] + pr_zn[0] + '\n'
    f.readline(pr_zn)