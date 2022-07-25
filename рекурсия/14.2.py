def sum_kr_z(z, a, b):
    if b < a:
        return 0
    elif b % z == 0:
        print(b)
        return b + sum_kr_z(z, a, b-1)
    else:
        return sum_kr_z(z, a, b-1)


print(sum_kr_z(2, 2, 6))
