n = int(input("n = "))
Max = -100*100
num = -1
y = False
for i in range(1, n+1):
    x = int(input("Введите элемент последовательности: "))

    if y and (x > Max):
        Max = x
        num = i

    if x == 0:
        y = True

if num != -1:
    print("Максимальный элемент последовательности:%d" % Max)
    print("Номер максимального элемента последовательности:%d" % num)
else:
    print("Максимальный элемент не найден")
