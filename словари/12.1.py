def inf_student():
    d_student = {"ФИО": None, "Курс": None, "Группа": None}
    for i in d_student:
        el = input('%s >>> ' % i)
        if el in "0123456789":
            d_student[i] = int(el)
        else:
            d_student[i] = el

    return d_student


res = inf_student()
print(res)
