def nod_rec(a, b):
    if b == 0:
        return a
    else:
        if a > b:
            return nod_rec(b, a % b)
        else:
            return nod_rec(a, b % a)


print(nod_rec(27, 72))
