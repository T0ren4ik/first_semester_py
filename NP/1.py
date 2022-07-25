import numpy as np
from matplotlib import pyplot as plt


def arr_():
    NN = ['Максим', 'Наталья', 'Владимир', 'Саша', 'Ксения']

    ST = {'st': np.random.choice(NN), 'Mat_an': np.random.randint(2, 6), 'Dis': np.random.randint(2, 6),
          'Al_gem': np.random.randint(2, 6)}

    return ST


def mark_sr_enjoyer(Ar):
    Br = []
    MM = {'2': 0, '3': 0, '4': 0, '5': 0}
    for i in range(len(Ar)):
        MM[str(A[i][3])] += 1
        MM[str(A[i][2])] += 1
        MM[str(A[i][1])] += 1
        PP = str((int(A[i][3]) + int(A[i][2]) + int(A[i][1])) / 3)
        Br += [[f'{PP:.4}']]

    Br = np.array(Br)
    res = np.hstack((Ar, Br))

    return res, Br, MM


def sort_(A):
    for i in range(len(A) - 1):
        if A[i][4] < A[i + 1][4]:
            p = A[i][4]
            A[i][4] = A[i + 1][4]
            A[i + 1][4] = p

    return A


def pct_label1(m):
    explod = [0, 0, 0, 0.4]
    fig, ax = plt.subplots()
    ax.pie(m.values(), autopct=lambda x: pct_label(x, m), shadow=True, explode=explod)
    plt.legend(list(m.keys()), title="Оценки", loc='best')
    plt.show()


def pct_label(x, list_):
    y = int(round(x / 100 * np.sum(list(list_.values()))))
    return str(y) + '\n{:.0f}%'.format(x)


np.set_printoptions(formatter={'all': lambda x: str(x) + ' ' * (8 - len(x))})

# n = int(input('>>> '))
n_ = 5
A = np.array([[i for i in arr_().values()] for j in range(n_)])
print('Создан массив: \n', A, '\n', 'Размерность: ', A.shape, '\n')

A_M, Marks, mm = mark_sr_enjoyer(A)
print('Столбец средних оценок: \n', Marks, '\n', 'Размерность: ', Marks.shape, '\n')
print('Неотсортированный массив: \n', A_M, '\n', 'Размерность: ', A_M.shape, '\n')

A_M_S = sort_(A_M)
print('Отсортированный массив: \n', A_M_S, '\n', 'Размерность: ', A_M.shape, '\n')

pct_label1(mm)
