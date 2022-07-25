def el_sum_int_fl(**a):
    SUM = 0
    d_list = []
    for i in a:
        if isinstance(a[i], (int, float)):
            SUM += a[i]
        else:
            d_list += [a[i]]

    return SUM, d_list


A = {'a1': 12, 'a2': 12, 'a3': 12.3, 'a4': 12.3, 'a5': 'fr'}
S, el = el_sum_int_fl(**A)

print("S = %.2f" % S)
print(el)
