a = abs(1234)

x = set(str(a))

v_z = set('1234567890')

p_zn = v_z - x
res = list(p_zn)

res.sort()

print(res)
