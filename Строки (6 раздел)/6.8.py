def sum(a, b, s):
    a = int(a, s)
    b = int(b, s)
    resp = a + b
    res = ""

    while resp // s != 0:
        res = str(resp % s) + res
        resp //= s
    res = str(resp) + res

    print(res)


sum("10023", "10023", 16)
