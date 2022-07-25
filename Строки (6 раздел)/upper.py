s = input(">>> ")
S = ""

for i in s:
    if "a" <= i <= "z":
        pr = ord(i) - ord("a")
        S += chr(ord('A') + pr)
    else:
        S += i

print(S)
