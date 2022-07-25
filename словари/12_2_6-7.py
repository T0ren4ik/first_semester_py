"""
Данная программа служит для утоления непомерно огромных желаний Наталии Михайловны.

Основные изменения в новой версии программы: исправлены старые баги, добавлены новые.


Что нужно, чтобы всегда писать хороший код? Представляйте себе,
что читать и саппортить ваш продукт будет маньяк-убийца, которому кто-то сказал, где вы живете.

P/S
Описание это программы было написано исключительно в развлекательных целях. Без намерения кого-то обидеть.
Имена и фамилии вымышленные, а все совпадения случайны.
"""


def input_student(count):      # число студентов в списке L
    L = []             # список из 10 записей (словарей)
    assert count > 0 or count == '', 'Количество студентов должно быть больше нуля.'
    for i in range(count):   # ввод информации
        fio = input('Fio: ')
        name = (input('Name: '))
        patronymic = (input('Patronymic: '))
        gender = input('Gender: ')
        age = int(input('Age: '))
        kurs = int(input('Kurs: '))
        group = int(input('group: '))
        math = int(input('Math: '))
        rus = int(input('Rus: '))
        informatics = int(input('Informatic: '))

        # создансловарь
        student = {'FIO': fio, 'Name': name, 'patronymic': patronymic,
                   'gender': gender, 'age': age, 'kurs': kurs, 'group': group,
                   'math_analysis': math, 'programming': rus, 'algebra_geometry': informatics
                   }
        L.append(student)

        return L


# Функция печати списка
def output(res):
    for st in res:
        for x in st:
            print(f'{x}: {st[x]}')
        print("==" * 60)


# Функция печп=ати меню
def print_menu():
    print('1: Печать меню')
    print("2: Ввод элементов списка")
    print("3: Вывод элементов списка")
    print("4: Их сортировка(по курсу, а для студентов одного курса по фамилии)")
    print("5: Поиск курсас наибольшим процентом мужчин")
    print("6: Поиск самых распространенных мужских и женских имен")
    print("7: Их сортировкав порядке убывания средней оценки,")
    print("8: Поиск студентов, имеющих задолженность хотя бы по одному предмету (выдать их данные на экран)")
    print("9: Выдать номера групп в порядке убывания средней оценки")
    print("0: Выход из программы.")
    print('--' * 60)


# Функция сортировки по курсу и фамилии
def sort_kurs_fio(L):
    for i in range(0, len(L)-1):
        for j in range(0, len(L)-i-1):
            if L[j]['kurs'] > L[j+1]['kurs']:
                L[j], L[j+1] = L[j+1], L[j]

    for i in range(0, len(L)-1):
        for j in range(0, len(L)-i-1):
            if (L[j]['FIO'][0] > L[j+1]['FIO'][0]) and (L[j]['kurs'] == L[j+1]['kurs']):
                L[j], L[j+1] = L[j+1], L[j]

    return L


# Функция сортировки по средней оценки
def sort_sr_makr(L):
    for i in range(0, len(L)-1):
        for j in range(0, len(L)-i-1):
            sr_zn_i = L[j]['math_analysis'] + L[j]['programming'] + L[j]['algebra_geometry']
            sr_zn_i_1 = L[j+1]['math_analysis'] + L[j+1]['programming'] + L[j+1]['algebra_geometry']
            if sr_zn_i < sr_zn_i_1:
                L[j], L[j+1] = L[j+1], L[j]

    return L


# Функция поиска курса с наибольшим процентом мужчин
def find_kyrs_max_men(L):
    m = L[0]['kurs']
    for i in range(len(L)):
        if L[i]['kurs'] > m:
            m = L[i]['kurs']

    kyrs_m = {i: 0 for i in range(1, m+1)}
    kyrs = {j: 0 for j in range(1, m+1)}

    for i in range(0, len(L)):
        if L[i]['gender'] == 'М':
            kyrs_m[L[i]['kurs']] += 1
        kyrs[L[i]['kurs']] += 1

    ind_kyrsa = 1

    MAX_percent = kyrs_m[1] * 100 / kyrs[1]

    for el in kyrs_m:

        try:
            pr_el = kyrs_m[el] * 100 / kyrs[el]
        except ZeroDivisionError:
            pr_el = 0

        if pr_el > MAX_percent:
            MAX_percent = pr_el
            ind_kyrsa = el

    return ind_kyrsa, MAX_percent


# Функция поска самого популярного имени
def find_name_popular(L):
    name_dict_m = {}
    name_dict_j = {}
    for el in range(len(L)):
        if L[el]['gender'] == 'М':
            name_dict_m.setdefault(L[el]['Name'], 0)
            name_dict_m.update({L[el]['Name']: name_dict_m[L[el]['Name']] + 1})
        elif L[el]['gender'] == 'Ж':
            name_dict_j.setdefault(L[el]['Name'], 0)
            name_dict_j.update({L[el]['Name']: name_dict_j[L[el]['Name']] + 1})

    MAX_m = 1
    NAME_m = None
    for name in name_dict_m:
        if name_dict_m[name] >= MAX_m:
            MAX_m = name_dict_m[name]
            NAME_m = name

    MAX_j = 1
    NAME_j = None
    for name in name_dict_j:
        if name_dict_j[name] >= MAX_j:
            MAX_j = name_dict_j[name]
            NAME_j = name

    return NAME_m, MAX_m, NAME_j, MAX_j


# Функция поиска задолжников
def find_st_debt(L):
    debt_list = []
    debt = {i for i in range(0, 60)}
    for i in range(len(L)):
        mark = {L[i]['math_analysis'], L[i]['programming'], L[i]['algebra_geometry']}
        if debt & mark != set():
            debt_list += [L[i]]

    return debt_list


# Функция выводы среднего балла в группе
def group_sort_mark(L):
    group_kurs = {}

    for i in range(len(L)):
        mark = L[i]['math_analysis'] + L[i]['programming'] + L[i]['algebra_geometry']
        k_g = str(L[i]['kurs']) + " курс, " + str(L[i]['group']) + " группа"
        group_kurs.setdefault(k_g, (0, 0))
        group_kurs[k_g] = (group_kurs[k_g][0] + mark, group_kurs[k_g][1] + 1)

    for i in group_kurs:
        group_kurs[i] = group_kurs[i][0] / group_kurs[i][1]

    sort_list = []
    for i in group_kurs:
        sort_list += [[i, group_kurs[i]]]

    for i in range(len(sort_list)):
        for j in range(len(sort_list)-i-1):
            if sort_list[j][1] < sort_list[j+1][1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]

    return sort_list


# Задание списков руками
student = {'FIO': "Трегубов", 'Name': "Максим", 'patronymic': "Юрьевич",
                   'gender': "М", 'age': 18, 'kurs': 1, 'group': 5,
                   'math_analysis': 81, 'programming': 81, 'algebra_geometry': 81
           }
student1 = {'FIO': "Иваницкая", 'Name': "Алиса", 'patronymic': "Игоревна",
                   'gender': "Ж", 'age': 18, 'kurs': 1, 'group': 5,
                   'math_analysis': 72, 'programming': 50, 'algebra_geometry': 82
            }
student2 = {'FIO': "Полякова", 'Name': "Наталия", 'patronymic': "Михайловна",
                   'gender': "Ж", 'age': 18, 'kurs': 100, 'group': 100,
                   'math_analysis': 100, 'programming': 100, 'algebra_geometry': 100
            }
student3 = {'FIO': "Черненко", 'Name': "Александр", 'patronymic': "Александрович",
                   'gender': "М", 'age': 19, 'kurs': 2, 'group': 5,
                   'math_analysis': 60, 'programming': 70, 'algebra_geometry': 66
            }
student4 = {'FIO': "Ершов", 'Name': "Александр", 'patronymic': "Александрович",
                   'gender': "М", 'age': 20, 'kurs': 2, 'group': 5,
                   'math_analysis': 82, 'programming': 81, 'algebra_geometry': 88
            }
student5 = {'FIO': "Фурсова", 'Name': "Александра", 'patronymic': "Cергеевна",
                   'gender': "Ж", 'age': 18, 'kurs': 2, 'group': 5,
                   'math_analysis': 50, 'programming': 50, 'algebra_geometry': 71
            }

L = [student1] + [student2] + [student] + [student3] + [student4] + [student5]


# Запуск почти бесконечного цикла (Меню)
vv = 1
print('>> Меню (Лучше начать с 2: Ввода элементов списка)')
while vv != 0:
    if vv == 1:
        print('--' * 60)
        print('>>> Печать меню')
        print()
        print_menu()

    elif vv == 2:
        print(">> Вызвана функция для ввода информации")
        print()
        try:
            count = int(input("Количество студентов: "))
            L = input_student(count)
        except AssertionError as err:
            print("Error!!! ", err)
            count = int(input("Количество студентов: "))
            L = input_student(count)
        except ValueError as err_:
            print("Error!!! ", err_)
            count = int(input("Количество студентов: "))
            L = input_student(count)

        print("--" * 60)

    elif vv == 3:
        print('>>> Печать списка студентов')
        print()
        output(L)

    elif vv == 4:
        print('>>> Сортировка по курсу и фамилии была сделана')
        print()
        L = sort_kurs_fio(L)
        print("--" * 60)

    elif vv == 5:
        print('>>> Поиск курса с наибольшим процентом мужчин была сделана')
        print()
        res_5 = find_kyrs_max_men(L)
        print(res_5[0], ' - курс с наибольшим количеством мужчин, а именно: %3.f' % res_5[1])
        print("--" * 60)

    elif vv == 6:
        print('>>> Поиск самого популярного имени был сделан')
        print()
        res_6 = find_name_popular(L)
        print(res_6[0], ' - самое популярное мужское имя. Его носят ', res_6[1], " человек")
        print(res_6[2], ' - самое популярное женское имя. Его носят ', res_6[3], " человек")
        print("--" * 60)

    elif vv == 7:
        print('>>> Сортировка в порядке убывания средней оценки была проведена')
        print()
        L = sort_sr_makr(L)
        print("--" * 60)

    elif vv == 8:
        print('>>> Поиск студентов имеющих задолжность был сделан. Вот они:')
        print()
        res_8 = find_st_debt(L)
        output(res_8)
        print("--" * 60)

    elif vv == 9:
        print('>>> Вывод групп в порядке убывания средней оценки исполнено')
        print()
        res_9 = group_sort_mark(L)
        print(res_9)
        print("--" * 60)

    elif vv == -1:
        print('Введите команду в числовом формате. Числа от 0 до 9')
        print()
        print("--" * 60)
    else:
        print('Неверная команда!!!')
        print("--" * 60)

    try:
        vv = int(input("Введите команду. (Меню - 1):"))
    except ValueError:
        vv = -1

    print()
