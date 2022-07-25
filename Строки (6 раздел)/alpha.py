s = input(">>> ")

i = 0
flag = True


while i < len(s) and flag:
    a = "a" <= s[i] <= "z"
    A = "A" <= s[i] <= "Z"
    B = "0" <= s[i] <= "9"

    print(s[i], A, a, B)

    flag = A or B or a
    i += 1

print(flag)
