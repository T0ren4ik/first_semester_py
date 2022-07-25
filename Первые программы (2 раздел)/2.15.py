Zislo = int(input(">>>"))

u1 = Zislo // 100
u2 = Zislo // 10 % 10
u3 = Zislo % 10

res = u3 * 100 + u2 * 10 + u1

print(res)
