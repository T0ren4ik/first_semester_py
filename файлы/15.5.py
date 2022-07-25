n = int(input('n >>> '))
with open('z_d_n.txt', "w") as f:
    for i in range(10, 100, n):
        f.write(str(i) + '\n')
