n = int(input("n = "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        print(i, end="\t")
        count += 1

print()
print("количество делителей:", count)
