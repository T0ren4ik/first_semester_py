s = input(">>> ")
S = " " + s
i = 0
a = []

while len(S) > 0:
    while i < len(S) and S[i] == " ":
        i += 1
    j = i
    while j < len(S) and S[j] != " ":
        j += 1
    if S[i: j] != '':
        a += [S[i: j]]
    S = S[j:]
    i = 0

print(a)
