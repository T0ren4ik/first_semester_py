def A_A(S):
    s = S.lower()
    s += " "
    a = []
    i = 0

    while i < len(s) and len(s) > 0:
        while i < len(s) and s[i] == " ":
            i += 1

        j = i
        while j < len(s) and s[j] != " ":
            j += 1
        if s[i: j] != "":
            a.append(s[i: j])

        s = str(s[j:])
        i = 0

    return a


def COUNT(a_):
    count = 0
    for i in a_:
        if i[0] == i[-1]:
            count += 1
    return count


s = "ada   a.,r  araf  // 1231   141"

a_ = A_A(s)
count_ = COUNT(a_)

print(count_)
