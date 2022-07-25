import tkinter as tk
from math import sqrt, factorial


def add_digit(digit):
    value = entry.get()
    if value[0] == '0':
        entry.delete(0)
        entry.insert('end', digit)
    else:
        entry.insert('end', digit)


def add_operation(operation):
    value = entry.get()
    if value[0] == '0' and operation in '√':
        entry.delete(0)
        entry.insert('end', operation)

    elif value[-1] in '-+/*!^.√':
        entry.delete(len(value) - 1)
        entry.insert('end', operation)

    else:
        entry.insert('end', operation)


def del_ent():
    entry.delete(0, "end")
    entry.insert('end', 0)


def calculate():
    value = entry.get()
    remuve = set('1234567890-/*.+()')
    pr_zn = set(value)

    for i in remuve:
        pr_zn.discard(i)

    if pr_zn == set():
        try:
            res = eval(value)
            entry.insert('end', '=' + str(res))
        except ZeroDivisionError:
            entry.delete(0, "end")
            entry.insert('end', 'Деление на ноль')

    elif set('^') == pr_zn:
        value = value.replace('^', '**')
        res = eval(value)
        entry.insert('end', '=' + str(res))

    elif set('√') == pr_zn:
        value = value.replace('√', 'sqrt(') + ')'
        res = eval(value)
        entry.insert('end', '=' + str(res))

    elif set('!') == pr_zn:
        value = 'factorial(' + value.replace('!', ')')
        res = eval(value)
        entry.insert('end', '=' + str(res))

    else:
        entry.delete(0, "end")
        entry.insert('end', 'Error')


root = tk.Tk()
root.geometry('310x440')
root.resizable(False, False)
root.title("Калькулятор")


entry = tk.Entry(root, width=14, font=("Arial Bold", 30), bg='mint cream', fg='black', justify=tk.RIGHT)
entry.insert('end', 0)
entry.grid(row=0, column=0, sticky='W')


frame_BUtt = tk.Frame()
tk.Button(master=frame_BUtt, text='1', font="Arial 30", command=lambda: add_digit(1), height=1, width=3, bg='bisque').grid(row=3, column=0)
tk.Button(master=frame_BUtt, text='2', font="Arial 30", command=lambda: add_digit(2), height=1, width=3, bg='bisque').grid(row=3, column=1)
tk.Button(master=frame_BUtt, text='3', font="Arial 30", command=lambda: add_digit(3), height=1, width=3, bg='bisque').grid(row=3, column=2)
tk.Button(master=frame_BUtt, text='4', font="Arial 30", command=lambda: add_digit(4), height=1, width=3, bg='bisque').grid(row=4, column=0)
tk.Button(master=frame_BUtt, text='5', font="Arial 30", command=lambda: add_digit(5), height=1, width=3, bg='bisque').grid(row=4, column=1)
tk.Button(master=frame_BUtt, text='6', font="Arial 30", command=lambda: add_digit(6), height=1, width=3, bg='bisque').grid(row=4, column=2)
tk.Button(master=frame_BUtt, text='7', font="Arial 30", command=lambda: add_digit(7), height=1, width=3, bg='bisque').grid(row=5, column=0)
tk.Button(master=frame_BUtt, text='8', font="Arial 30", command=lambda: add_digit(8), height=1, width=3, bg='bisque').grid(row=5, column=1)
tk.Button(master=frame_BUtt, text='9', font="Arial 30", command=lambda: add_digit(9), height=1, width=3, bg='bisque').grid(row=5, column=2)
tk.Button(master=frame_BUtt, text='0', font="Arial 30", command=lambda: add_digit(0), height=1, width=3, bg='bisque').grid(row=6, column=0)
tk.Button(master=frame_BUtt, text='/', font="Arial 30", command=lambda: add_operation('/'), height=1, width=3, bg='goldenrod1').grid(row=3, column=3)
tk.Button(master=frame_BUtt, text='*', font="Arial 30", command=lambda: add_operation('*'), height=1, width=3, bg='goldenrod1').grid(row=4, column=3)
tk.Button(master=frame_BUtt, text='-', font="Arial 30", command=lambda: add_operation('-'), height=1, width=3, bg='goldenrod1').grid(row=5, column=3)
tk.Button(master=frame_BUtt, text='+', font="Arial 30", command=lambda: add_operation('+'), height=1, width=3, bg='goldenrod1').grid(row=6, column=3)
tk.Button(master=frame_BUtt, text='=', font="Arial 30", height=1, width=3, bg='coral1', command=lambda: calculate()).grid(row=6, column=2)
tk.Button(master=frame_BUtt, text='.', font="Arial 30", command=lambda: add_operation('.'), height=1, width=3, bg='bisque').grid(row=6, column=1)
tk.Button(master=frame_BUtt, text='C', font="Arial 30", height=1, width=3, bg='ivory2', command=lambda: del_ent()).grid(row=2, column=3)
tk.Button(master=frame_BUtt, text='√', font="Arial 30", command=lambda: add_operation('√'), height=1, width=3, bg='ivory2').grid(row=2, column=0)
tk.Button(master=frame_BUtt, text='^', font="Arial 30", command=lambda: add_operation('^'), height=1, width=3, bg='ivory2').grid(row=2, column=1)
tk.Button(master=frame_BUtt, text='n!', font="Arial 30", command=lambda: add_operation('!'), height=1, width=3, bg='ivory2').grid(row=2, column=2)

frame_BUtt.grid(row=1, column=0, sticky='W')


root.mainloop()
