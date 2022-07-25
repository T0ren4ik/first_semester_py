S = input("Введите строку ")
count = 0

for i in range(len(S)):
    if S[i:i+3] == "101":
        count += 1


print(count)


count = 0
newS = S

for i in range(len(S)):
    if newS.find("101", i, i + 3) != -1:
        count += 1

print(count)
