with open('7.txt') as f:
    L = []
    for line in f:
        L = line.split()

    MAX = int(L[0])
    for i in L:
        if int(i) > MAX:
            MAX = int(i)

print(MAX)
