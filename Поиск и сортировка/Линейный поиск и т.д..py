a = []
T = int(input(">>> "))

i = 0
while i < len(a) and T != a[i]:
    i += 1

if i == len(a):
    print("Элемент отсутствует")
else:
    print(i)


# ---------------------------------------\

if T not in a:
    print("Элемент отсутствует")
else:
    print(a.index(T))


# --------------------------------------\

a += T
while i < len(a):
    i += 1

if i == len(a) - 1:
    print("Элемент отсутствует")
else:
    print(i)
