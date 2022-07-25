a = ['c', 'a', 'g', 'a', 't']


for i in range(len(a)):
    if 'a' <= a[i] <= 'z' and a[i] not in a[0: i]:
        print(a[i])

