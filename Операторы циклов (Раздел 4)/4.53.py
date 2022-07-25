a = [int(i) for i in input('>>> ').split()]

ind_n = None
ind_k = None
product = 1
i = 0
flag = True

while len(a) > i and flag:
    ind_n = i
    while a[i] > 0:
        ind_k = i
        i += 1
        flag = False
    i += 1

for i in range(ind_n, ind_k + 1):
    product *= a[i]

print(product)