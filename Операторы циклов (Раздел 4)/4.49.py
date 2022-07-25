a = [int(i) for i in input('>>> ').split()]

i = 0
while a[i] != 0:
    i += 1

Sum = 0
product = 1
for i in range(i + 1, len(a)):
    if a[i] > 0:
        Sum += a[i]
        product *= a[i]

print(Sum, product)
