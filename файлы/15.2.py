with open('2.txt', 'w') as f:
    n = 3

    for i in range(n):
        f.write(str(input(">>> ")) + '\n')


with open('2.txt') as f1:
    L = f1.readlines()
    for i in L:
        r = 1
        for j in i:
            if j in (str(i) for i in range(10)):
                r = 0

        if r:
            print(i)
