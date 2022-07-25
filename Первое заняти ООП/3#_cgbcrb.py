def fin_sim(s, zp):
    s = s.lower()
    a = s.split()
    count = 0

    for i in a:
        if zp in i:
            count += 1

    return count


zp_ = 'e'
test = ['123 wer1 //3 we1// ', 'fsfsf /23e4 2/1r', '',
        ' ', 'trd 123', 'Esdf we 435/ Eesdf', 'EeEsdfs, err Ee '
        ]

for i in test:
    print(fin_sim(i, zp_))
