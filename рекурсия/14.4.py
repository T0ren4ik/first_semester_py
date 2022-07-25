def sum_zn(a):
    if a == 0:
        return 0
    else:
        return sum_zn(a // 10) + a % 10


print(sum_zn(1234))
