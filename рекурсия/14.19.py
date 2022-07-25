def bin_k(n, m):
    if n == 0 or (m == n and m >= 0 and n >= 0):
        return 1
    elif n > m > 0:
        return 0
    else:
        return bin_k(n-1, m-1) + bin_k(n, m-1)


print(bin_k(1, 7))


