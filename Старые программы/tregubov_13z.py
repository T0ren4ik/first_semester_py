a = int(input("a = "))
b = int(input("b = "))
m = int(input("m = "))

def SP_A_B_M(a, b, m = 2):
    S = 0
    P = 1
    if a > b:
        print("Ошибка ввода данных")
    else:
        for i in range(a, b+1):
            if i % m == 0:
                S += i
                P *= i

    return S, P

print("Сумма и произведение:", SP_A_B_M(a, b, m))

