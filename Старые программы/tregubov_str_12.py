S = input("Введите строку ")

newS = S
while newS != "":
    print(newS[0], "встречается", S.count(newS[0]), "раз")
    newS = newS.replace(newS[0], "")


print("")


newS1 = S


while newS1 != "":
    for i in range(len(S)):
        count = 0
        for j in range(i, len(newS1)):
            if S[i] == S[j]:
                count += 1

print(count)

"""
for i in range(len(S)):
    count = 0

    for j in range(i,  len(newS1)):
        if S[i] == S[j]:
            count += 1
    print(S[i], "встречается", count, "раз")
"""



