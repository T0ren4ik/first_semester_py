def el_int_sum(**a):
    print(a)
    d_int = []
    SUM = 0
    for i in a:
        if a[i].isdigit():
            SUM += a[i]
            d_int += [a[i]]

    return d_int, SUM


A = {"a1": 123, "a2": 12, 'a3': 123}
el, S = el_int_sum(**A)
print(el)
print(S)
