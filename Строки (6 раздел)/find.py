s = "12377123"
f = '9'


i = 0
flag = True
res = -1
while i < len(s) and flag:
    if s[i: i + len(f)] == f:
        flag = False
        res = i
    else:
        i += 1

print(s.find(f))
print(res)
