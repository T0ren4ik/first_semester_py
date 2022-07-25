def current_row(n):
    row = list()
    for i in range(n):
        if i == 0 or i == n - 1:
            row.append(1)
        else:
            c_row = current_row(n - 1)
            row.append(c_row[i - 1] + c_row[i])
    return row


def triangle(m):
    result = list()
    for i in range(m):
        result.append(current_row(i + 1))

    for j in result:
        print(' ' * (m - result.index(j) - len(j)//2 + 10), end='')
        print(j)


triangle(10)
