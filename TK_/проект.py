import numpy as np


def tower(FromT, AuxT, ToT, n):
    if n == 1:                              # Если остался один диск, то переместить его:
        print(f'Переместить диск №{n} с {FromT} на {ToT} \n{tower_watch(FromT, ToT)} \n')
    else:
        tower(FromT, ToT, AuxT, n - 1)		# 2.1. (n – 1) диск FromT –> AuxT
        print(f'Переместить диск №{n} с {FromT} на {ToT} \n{tower_watch(FromT, ToT)} \n')	   # 2.2. 1 диск FromT –> ToT
        tower(AuxT, FromT, ToT, n - 1)	    # 2.3. (n – 1) диск AuxT –> ToT


def tower_watch(S, K):
    global A, n_
    ST = {'A': 0, 'B': 1, 'C': 2}

    ind = n_ - 1

    for el in range(len(A[:, ST[K]])):
        if A[:, ST[K]][el] != 0:
            ind = el - 1
            break

    ind_n = 0
    for el in range(len(A[:, ST[S]])):
        if A[:, ST[S]][el] != 0:
            ind_n = el
            break

    pr_zn = A[ind_n][ST[S]]
    A[ind_n][ST[S]] = 0
    A[ind][ST[K]] = pr_zn
    return A


np.set_printoptions(formatter={'all': lambda x: str(x)[0]})

n_ = 2
A = np.zeros((n_, 3))
C = list(np.array([range(1, n_+1)]))
A[:, 0] = np.array([range(1, n_+1)])

tower('A', 'B', 'C', n_)

