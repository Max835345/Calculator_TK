from tkinter import *


def btn_click(item):
    global expression
    try:
        input_field['state'] = 'normal'
        expression += item
        input_field.insert(END, item)

        if item == '=':
            result = str(eval(expression[:-1]))
            input_field.insert(END, result)
            expression = ''
        input_field['state'] = 'readonly'

    except ZeroDivisionError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка (деление на 0)')
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка')


def bt_clear():
    global expression
    expression = ''
    input_field['state'] = 'normal'
    input_field.delete(0, END)
    input_field['state'] = 'readonly'


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 228
window_height = 305
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(0, 0)
root.title("Калькулятор")

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky='nsew')
input_field = Entry(frame_input, font="Arial 15 bold", width=24, state='readonly')

input_field.pack(fill=BOTH)

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

expression = ''
button = Button(root, text='C', command=lambda: bt_clear())
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        (Button(root, width=2, height=3, text=buttons[row][col],
                command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col,
                                                                                    sticky="nsew", padx=1, pady=1))

root.mainloop()
