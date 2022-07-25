def set_k(set0, k):
    set_dk = set()
    for i in set0:
        if i % k == 0:
            set_dk.add(i)

    return set_dk


set_n = {i for i in range(1016, 7937 + 1)}
set_3 = set_k(set_n, 3)
set_7 = set_n - set_k(set_n, 7)
set_17 = set_n - set_k(set_n, 17)
set_19 = set_n - set_k(set_n, 19)
set_27 = set_n - set_k(set_n, 27)
set_r = set_3 & set_7 & set_17 & set_19 & set_27
print(len(set_r))

M = {i for i in range(1016, 7937 + 1) if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0}
print(len(M))

print(set_r - M)



