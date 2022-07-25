def init(s):
    if len(s):
        return s[0].isdigit() & init(s[1:])
    else:
        return True


def znak(s):
    L = '+-*/'
    if len(s):
        if s[0] in L:
            return True
        else:
            return znak(s[1:])
    else:
        return False


S = ['123 123 123 123', '2f ,23 214', '213 1,4 123', '123, 123 123', '']
for i in S:
    if i != '':
        k = i.split()
        res = init(k)

        print(res)
    else:
        print(False)


print()
Sz = 'wefg+hnbvcsa'
print(znak(Sz))
