x = float(input("Введите x "))
y = float(input("Введите y "))
r = float(input("Введите r "))
R = x**2 + y**2 - r**2
R1 = x**2 + y**2 - (2*r)**2
if r >= 1:
    if (R >= 0) and (R1 <= 0):
        print("Точка принадлежит кольцу")
