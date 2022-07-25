import random


def random_list1(count_elements):
    """Создаем и заполнем элементами список"""
    _list = [random.randint(1, 2*count_elements + 1) for i in range(count_elements)]
    return _list


def print_list2(_list):
    """Печаиаем список"""
    for elem in _list:
        print('%5d' % elem, end=' ')
    print()


def A_B(A, B):
    """Обмен элементов списков: первого из A и последнего из B."""
    A[0], B[len(B)-1] = B[len(B)-1], A[0]
    return A, B


def Add(A, B):
    """Вставка элемента с No (random) из списка B в начало списка A (без цикла)."""
    x = random.randint(0, len(B)-1)
    A[0:0] = [B[x]]
    return A


def Add2(A,B):
    """Вставка элемента с No (random) из списка B в начало списка A (сдвиги; без срезов)."""
    x = random.randint(0, len(B)-1)
    A.insert(0, B[x])
    return A





def PrintMenu():
    """Печать меню."""
    print(55 * '-')
    print('1 : Получение элементов случайным образом')
    print('2 : Вывод списков')
    print("3: Обмен элементов списков: первого из A и последнего из B.")
    print("4: Вставка элемента с No (random) из списка B в начало списка A (без цикла).")
    print("5: Вставка элемента с No (random) из списка B в начало списка A (сдвиги; без срезов).")
    print("d: Печать документации по заданной пользователем функции проекта.")
    print("m: Печать меню.")
    print('x: Выход из программы.')
    print(55 * '-')
