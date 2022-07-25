def str_in_list(L):
    k = False
    for x in L:
        if not isinstance(x, list):
            if isinstance(x, str):
                return True
        else:
            k = str_in_list(x)

    return k


def str_list(L):
    s = ''
    for x in L:
        if not isinstance(x, list):
            s += str(x) + ' '
        else:
            s += str_list(x)

    return s


#        0   1          2        3   len = 4
mn_vl = [1, 1,  [1, [14, -7], 2], -6]
print(str_list(mn_vl))

print(str_in_list(mn_vl))
