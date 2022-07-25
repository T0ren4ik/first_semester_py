n = int(input("n >>> "))

flag = True
while n > 9 and flag:
    flag = True if n % 10 < n % 100 // 10 else False
    n = n // 10

print(flag)
