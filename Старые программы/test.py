import TregubovMaximU_5g_PodProg as PP
import random


random.seed()
vv = 1
PP.PrintMenu()
print('!!!: Начнем с заполнения списков (п.1)')
while vv != "x" :
    if vv == "1":
        n = int(input('Количество элементов >>> '))
        A = PP.random_list1(n)
        B = PP.random_list1(n)
        print('1: Получены элементы списка. Печать: п.2')
    elif vv == "2":
        print('2: Вывод списков')
        PP.print_list2(A)
        PP.print_list2(B)
    elif vv == "3":
        print("3: Обмен элементов списков: первого из A и последнего из B.")
        A, B = PP.A_B(A, B)
    elif vv == "4":
        print("4: Добавление элемента в начало списка (без использования цикла).")
        A = PP.Add(A, B)
    elif vv == "5":
        print("5: Вставка элемента с No (random) из списка B в начало списка A (сдвиги; без срезов).")
        A = PP.Add2(A, B)
    elif vv == "d":
        print("d: Печать документации по заданной пользователем функции проекта.")
        PP.PrintMenu()

    print(55 * '-')
    vv = input('Выберите команду меню (9: Вывод меню) >>> ')