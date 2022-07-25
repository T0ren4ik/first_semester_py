with open('4.txt') as f:
    count = 0
    for line in f:
        if line not in ('', '\n'):
            count += 1
    f.close()

print(count)
