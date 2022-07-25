x = int("10101101", 2)
y = int("255", 8)
z = int("1E", 16)

res = x - y + z
res2 = bin(res)
res8 = oct(res)
res16 = hex(res)

print(res2, res8, res16)