n = int(input('n >>> '))

last = n % 10
first = n

while first > 9:
    first = first // 10

if last == first:
    print("True")
else:
    print("False")
