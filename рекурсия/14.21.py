def F(L):
    res = 1
    for x in L:
        if not isinstance(x, list):
            if x > 0:
                res *= x

        else:
            res *= F(x)
    return res


mn_vl = [1, 1,  [1, [14, -7], 2], -6]
print(F(mn_vl))
