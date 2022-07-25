# функция перевода в 10-ую систему счисления
def des(x, a):
    L = len(x)
    if L == 1:
        return alf[x]
    else:
        return alf[x[0]] * a ** (L - 1) + (des(x[1:], a))


# функция, которая переводит из 10-ой в любую
def change(x, b):
    if int(x) // b <= 1:
        if alf_change[str(int(x) // b)] == '0':
            return alf_change[str(int(x) % b)]
        else:
            return alf_change[str(int(x) // b)] + alf_change[str(int(x) % b)]
    else:
        return change(str(int(x) // b), b) + alf_change[str(int(x) % b)]


# словарь строка число
namber = {str(i): i for i in range(10)}
alf = {"A": 10, 'B': 11, 'C': 12, "D": 13, 'E': 14, 'F': 15}
alf.update(namber)

# словарь число вуква
namber_change = {str(i): str(i) for i in range(10)}
alf_change = {'10': "A", '11':  'B', '12': 'C', '13': "D", '14': 'E', '15': 'F'}
alf_change.update(namber_change)


# запуск программы
try:
    x = input('x = ')
    s_i_x = int(input('Система счисления x:'))
    s_i_nx = int(input('В какую систему счисления переводить:'))
    print()
except (KeyError, ValueError):
    print("Введенные вами данные неверны")
    x = input('x = ')
    s_i_x = int(input('Система счисления x:'))
    s_i_nx = int(input('В какую систему счисления переводить:'))
    print()


if s_i_nx == 10:
    res10 = des(x, s_i_x)
    print(res10)

else:
    res10 = des(x, s_i_x)
    resn = change(res10, s_i_nx)
    print(resn)
