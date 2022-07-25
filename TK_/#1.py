from tkinter import *
from tkinter.messagebox import *  # подключаем диалоговые окна tkinter

root = Tk()
root.minsize(width=350, height=150)
root.maxsize(width=500, height=300)
root.title("Калькулятор")

# Создадим 3 фрейма: fr_xy, fr_op и fr_res для размещения компонент
# фрейм для ввода чисел x, y
fr_xy = Frame(root)
fr_xy.pack(side=TOP, expand=YES, fill=X)
# на нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, text = "x = ")
lx.pack(side=LEFT, padx=10, pady=10)
entX = Entry(fr_xy)
entX.insert(0, 0)  # в редактор записываем в позицию 0 число 0
entX.pack(side=LEFT, padx=10, pady=10)
entX.focus()  # редактор будет выбран при старте
ly = Label(fr_xy, text="y = ")
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy)
entY.insert(0, 0)
entY.pack(side=LEFT, padx=10, pady=10)

# создание фрейма с заголовком для выбора операции:
fr_op = LabelFrame(root, text = "Операция:")
fr_op.pack(side = TOP, expand=YES, fill=X)

# операцию будем выбирать с помощью виджета Radiobutton:
oper = ['+', '-']	# список операций
# вводим строковую переменную tkinter, ее свяжем с выбором Radiobutton
varOper = StringVar( )
# в цикле создаем 4 кнопки Radiobutton (связываем их с переменной):

for op in oper: Radiobutton(fr_op, text=op, variable=varOper, value=op).pack(side=LEFT, padx=20, pady=10)
varOper.set(oper[0])  # устанавливаем текущее значение '+'

# создаем фрейм для вычисления значения и вывода результата:
fr_res = Frame(root)
fr_res.pack(side=TOP, expand=YES, fill=BOTH)


# обработчик кнопки:
def OnButtunResult():
    try: x = float(entX.get())  # извлекаем число из 1-го редактора
    except ValueError:
        # вывод диалогового окна с ошибкой:
        showerror("Ошибка заполнения", "Переменная x не является числом")
        return
    try:
            y = float(entY.get())
    except ValueError:
        showerror("Ошибка заполнения", "Переменная y не является числом")
        return

    # в переменную op записываем выбранную операцию:
    op = varOper.get()  # вычисляем:
    if op == '+':
        res = x + y
    else:
        res = x - y
    # вывод результата на метку:
    lres['text'] = res


# создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res, text="=", width=10, command=OnButtunResult).pack(side=LEFT, padx=30, pady=20)
lres = Label(fr_res, text="")
lres.pack(side=LEFT, padx=30, pady=20)
root.mainloop()
