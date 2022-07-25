s = input("s >>> ")
f = input("f >>> ")


cou = 0

for i in range(0, len(s) - len(f) + 1):
    if s[i: i + len(f)] == f:
        cou += 1


i = 0
coun = 0
while i < len(s) - len(f) + 1:
    if s[i: i + len(f)] == f:
        i += len(f)
        coun += 1
    else:
        i += 1

print(cou)
print(coun)
print(s.count(f))
