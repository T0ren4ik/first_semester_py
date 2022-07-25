a = [16, 14, 12, 10, 7, 6, 2, 1]
N = int(input(">>> "))
i = 0

a. append(N)
while N < a[i]:
    i += 1

if i == a.index(N):
    print("Элемент присутствует в списке")
    a = a[: len(a) - 1]
else:
    # a[i: i] = [N]

    for j in range(len(a) - 1, i, -1):
        a[j] = a[j - 1]
    a[i] = N

print(a)
