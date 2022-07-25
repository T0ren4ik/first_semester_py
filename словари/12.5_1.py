def el_sum_int_fl(**a):
    SUM = 0
    d_list = []
    for i in a:
        j = a[i].replace('.', '', 1)
        if a[i].isdigit():
            SUM += float(a[i])
        elif "." in a[i] and j.isdigit():
            SUM += float(a[i])
        else:
            d_list += [a[i]]

    return SUM, d_list


A = {'a1': '12', 'a2': '12', 'a3': '12.3', 'a5': 'fr'}
S, el = el_sum_int_fl(**A)
print("S = %.2f" % S)
print(el)
