def zet(s):
    if len(s) > 0:
        if s[0] % 2 == 1:
            print(s[0])
            zet(s[1:])
        else:
            zet(s[1:])
    else:
        print("Конец света")


S = [1, 2, 3, 4, 6, 7, 9, 2]
zet(S)
