product = 1
factorial = 1
z = 1

for i in range(1, 9):
    factorial *= i
    product *= 2 + z * 1 / factorial
    z = -z

print(product)