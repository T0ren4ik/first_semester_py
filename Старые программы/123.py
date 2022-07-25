import random
def Add(A, B):
    """Вставка элемента с No (random) из списка B в начало списка A (без цикла)."""
    x = random.randint(0, len(B))
    A[0:0] = [B[x]]
    return A

