def DivMod(a, b):
    x = a // b
    y = a % b

    return y, x


a_ = int(input("a >>> "))
b_ = int(input("b >>> "))

res = DivMod(a_, b_)

print(res)
