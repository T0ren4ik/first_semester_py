def FAKtor(n):
    res = "1"
    k = 2
    while n > 1:
        if n % k == 0:
            res += "*" + str(k)
            n //= k
        else:
            k += 1

    return res


n_ = int(input("n >>> "))
res_ = FAKtor(n_)
print(res_)
