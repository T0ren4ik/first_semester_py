a = [float(i) for i in input('>>> ').split()]

z = []
for i in a:
    if abs(i) <= 2:
        z += [i]
    else:
        z += [0.5]

print(z)
print(max(z))
