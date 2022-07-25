def mn_zet(mn):
    mn_zet = set()
    for i in mn:
        if i % 2 == 0:
            mn_zet.add(i)

    return mn_zet


A = {i for i in range(2, 30, 3)}

res = mn_zet(A)

print(res)
