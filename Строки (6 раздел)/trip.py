s = input(">>> ")

i = 0
while i < len(s) and s[i] == " ":
    i += 1

s = s[i:]

j = len(s)
while j > 0 and s[j - 1] == " ":
    j -= 1

s = s[:j]
print(s)
