def UpperLegacy(string):
    st_res = ""
    for i in string:
        if "а" <= i <= "я":
            y = chr(ord("А") + (ord(i) - ord("а")))
            st_res += y
        else:
            st_res += i
    return st_res

string = input("Введите строку:")

print(UpperLegacy(string))
print(string.upper())
