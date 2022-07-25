s = "afasf123 a sad"
s = s.lower()


for i in range(len(s)):
    A = "a" <= s[i] <= "z"
    B = s[i] not in s[0: i]
    if A and B:
        print(s[i])
