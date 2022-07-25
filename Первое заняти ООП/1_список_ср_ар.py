a = [1, 2, 3, 7, 1, 4]


Max_i = 0
pr_zn = 0
for j in range(len(a)):
    pr_zn += a[j]
sr_arM = (pr_zn - a[0]) / (len(a) - 1)

for i in range(1, len(a)):
    pr_zn = 0
    sr_ar = 0
    for j in range(len(a)):
        pr_zn += a[j]

    sr_ar = (pr_zn - a[i]) / (len(a) - 1)

    if abs(sr_ar - a[i]) <= abs(sr_arM - a[Max_i]):
        Max_i = i
        sr_arM = sr_ar

print(Max_i)
