with open('123.txt', 'r+') as f:
    L = f.readline()
    print(f.tell())
    f.seek(f.tell() + 1)
    print(f.tell())