def bracket_view(s):
    i = 0
    while i < len(s):
        if i < len(s) and (s[i] not in ('(', ')')):
            s = s[0: i] + s[i+1:]
        else:
            i += 1
    return s


def bracket_structure(s):
    s1 = s.find('(')
    S = s[s1:]
    s2 = S.find(')')
    if len(s) == 0:
        return True

    elif -1 not in (s1, s2):
        s = s[0:s1] + s[s1+1:]
        s = s[0:s2-1] + s[s2:]
        return bracket_structure(s) and True
    else:
        return False


#S = input("S >>> ")
test = ['()', '()()()', '(())', '((()()))', '())(', '(())((())']

for S in test:
    S = bracket_view(S)
    res = bracket_structure(S)

    print(res)
