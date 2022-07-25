n = int(input('n >>> '))
ziclo = n
res = 0

while ziclo > 0:
    res = res * 10 + ziclo % 10
    ziclo = ziclo // 10

print(res)
