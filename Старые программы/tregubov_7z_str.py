def NumToStr(number):
    res = ""
    zero_nine = ("ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять")
    ten_nineteen = ("десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
                    "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать")
    if 0 <= number < 10:
        return zero_nine[number]
    elif 10 <= number <= 19:
        return ten_nineteen[number % 10]
    elif number % 10 == 0:
        return zero_nine[number // 10] + "дцать"
    elif number < 40:
        return zero_nine[number // 10] + "дцать " + zero_nine[number % 10]
    elif 40 < number < 50:
        return "сорок " + zero_nine[number % 10]
    elif 50 < number < 90:
        return zero_nine[number // 10] + "дцать " + zero_nine[number % 10]
    elif 90 < number < 100:
        return "девяносто " + zero_nine[number % 10]
    else:
        return "Силы кончились"


def DecToStr():
    for i in range(31):
        print(NumToStr(i), end="\n")


number = int(input("Введите число "))
print(NumToStr(number))


DecToStr()





