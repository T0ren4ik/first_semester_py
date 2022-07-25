with open('9.txt') as f:
    L = []
    for line in f:
        L += line.split()

with open('z_s_nz.txt', 'w') as f1:
    for i in L:
        r = len(str(i))
        for j in str(i):
            if '-' != j:
                if int(j) % 2 != 0:
                    r -= 1
            else:
                r -= 1

            if not r:
                f1.write(str(i) + ' ')
