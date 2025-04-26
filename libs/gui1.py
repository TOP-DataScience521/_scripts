from tkinter import (
    Button,
    Frame, 
    Label,
    StringVar,
    Tk,
)


root = Tk()

root.title('Демонстратор GUI')
root.geometry('400x300+750+450')

mainframe = Frame(master=root)
mainframe.grid(row=0, column=0, sticky='nsew')

lbl_text = StringVar(
    master=mainframe, 
    value='Добро пожаловать в графический интерфейс'
)

Label(
    master=mainframe,
    textvariable=lbl_text,
).grid(
    row=0,
    column=0,
    sticky='nsew',
)

def change_text():
    lbl_text.set('Была нажата кнопка')

Button(
    master=mainframe,
    text='НАЖМИ МЕНЯ',
    command=change_text,
).grid(
    row=1,
    column=0,
    sticky='nsew',
    padx=50,
    pady=20,
)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mainframe.rowconfigure(0, weight=2)
mainframe.rowconfigure(1, weight=1)
mainframe.columnconfigure(0, weight=1)


root.mainloop()

