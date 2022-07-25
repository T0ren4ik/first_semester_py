def min_zn_str(st, ind_i):
    min_ = st[0]
    ind_j = 0
    for i in range(len(st)):
        if min_ > st[i]:
            min_ = st[i]
            ind_j = i

    return min_, ind_i, ind_j


def max_zn_stolb(stolb, ind_j):
    max_ = stolb[0]
    ind_i = 0
    for i in range(len(stolb)):
        if max_ < stolb[i]:
            max_ = stolb[i]
            ind_i = i

    return max_, ind_i, ind_j


def sed(a):
    i = 0
    aT = []
    for j in range(len(a[i])):
        stolb = []
        for i in range(len(a)):
            stolb += [a[i][j]]
        aT += [stolb]

    list_sed_t = []
    for i in range(len(a)):
        for j in range(len(aT)):
            min_zn_str_ind = min_zn_str(a[i], i)
            max_zn_stolb_ind = max_zn_stolb(aT[j], j)
            # print(min_zn_str_ind, max_zn_stolb_ind)
            if max_zn_stolb_ind == min_zn_str_ind:
                list_sed_t += [min_zn_str_ind]

    return list_sed_t


A = [[5, 3, 4],
     [6, 2, 3],
     [11, 1, 3]
     ]


res = sed(A)
for i in range(len(res)):
    print(f"a[{res[i][1]},{res[i][2]}] = {res[i][0]}")
