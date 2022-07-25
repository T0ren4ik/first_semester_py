def get_mn_sogl(mn):
    mn = set(mn)
    gl = {'a', 'e', 'i', 'o', 'u' 'y', 'A', 'E', 'I', 'O', 'U', 'Y', ' ', '.', '?', '!', ','}
    res_ = []
    for i in mn:
        if i not in gl:
            res_ += i

    return res_


mn = 'eRt , gfdS'

res = get_mn_sogl(mn)

print(res)
