def set_k(set0, k):
    set_k = set()
    for i in set0:
        if i % k == 0:
            set_k.add(i)

    return set_k


M = {i for i in range(21)}
set_2 = set_k(M, 2)
set_3 = set_k(M, 3)
set_6 = set_2 & set_3
set_2_3 = set_2 | set_3

print("Числа кратные 2", set_2)
print("Числа кратные 3", set_3)
print("Числа кратные 6", set_6)
print("Числа кратные 2 or 3", set_2_3)

