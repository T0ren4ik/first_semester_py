print(4 * " %.1s |" % ("x", "y", "z", "F"))
print(4 * "----")

for x in False, True:
    for y in False, True:
        for z in False, True:
            xi, yi, zi = int(x), int(y), int(z)
            F = int(not yi & (xi or not zi))
            print(4 * "%2d |" % (xi, yi, zi, F))
