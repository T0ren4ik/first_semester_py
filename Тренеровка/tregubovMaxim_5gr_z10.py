with open('Strings.txt') as f:
    isx = f.readlines()

    new = []
    for i in range(len(isx)):
        dl = len(isx[i]) - 1
        j = isx[i].replace('\n', '')
        if dl < 5:
            new += [(f'№{i} < на {5 - dl} симв.', '*' * (5-dl) + j)]
        elif dl == 5:
            new += [(f'№{i} не изменилась.', j)]
        else:
            new += [(f'№{i} > на {abs(5 - dl)} симв.', j)]

    res = {}

    for i in new:
        res.setdefault(i[0], i[1])


with open('Strings_new.txt', 'w') as f1:
    for el in res:
        f1.write(el + ':' + res[el] + '\n')


with open('Strings_new.txt') as f2:
    S = f2.readlines()
    for k in range(len(S)):
        print(isx[k].replace('\n', '') + S[k][2:], end='')
