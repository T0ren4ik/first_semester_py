a = [1, 2, 2, 4, 4, 6, 7]
b = [1, 4, 6]

a_s = set(a)
b_s = set(b)

p_res = a_s & b_s

res = list(p_res)

print(res)
