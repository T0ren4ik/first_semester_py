K = int(input("N >>> "))

if K // 1000 == 0:
    u3 = K % 10
    if (u3 >= 1) and (u3 <= 5):
        u1 = K // 100
        u2 = K // 10 % 10

        max3 = u1
        t1, t2 = u2, u3
        if u2 > max3:
            max3 = u2
            t1, t2 = u3, u1
        if u3 > max3:
            t1, t2 = u1, u2
            max3 = u3

        max2 = t1
        last = t2
        if t2 > max2:
            max2 = t2
            last = t1

        res = max3 * 100 + max2 * 10 + last

        print(res)
    else:
        print("Последняя цифра не удовлетворяет условию")
else:
    print("Число не 3-ое")
