with open('1.txt') as f:
    L = f.readlines()
    print(L)
    for i in range(0, len(L), 2):
        print(L[i][:-1])
