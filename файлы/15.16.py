n = 3
with open('16.txt') as f1:
    r = len(f1.readlines())
    f1.seek(0)

    Ln = []
    for i in range(n-1):
        Ln += [f1.readline()]
    p = f1.tell()
    str_n = f1.readline()[:-1]
    Lk = []
    for j in range(n, r):
        Lk += [f1.readline()]


with open('16.txt', 'r+') as f:
    f.truncate(p)
    f.seek(p)
    str_n = str_n[::-1]
    f.write(str_n+'\n')
    for i in range(len(Lk)):
        f.write(Lk[i])
