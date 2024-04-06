from operator import ge
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

window = Tk()
window.geometry("410x125")
window.title("Компьютер угадывает число")

min_number = 1
max_number = 15


def generate_number():
    global number
    list1.delete(0, END)
    number = randint(min_number, max_number)
    list1.insert(END, number)


def give_more():
    try:
        global number, min_number
        min_number = number + 1
        generate_number()
    except ValueError:
        messagebox.showinfo("Лимит попыток исчерпан", "Пожалуйста, начните заново")


def give_less():
    try:
        global number, max_number
        max_number = number - 1
        generate_number()
    except ValueError:
        messagebox.showinfo("Лимит попыток исчерпан", "Пожалуйста, начните заново")


def win():
    global min_number, max_number
    list1.delete(0, END)
    list1.insert(END, "Победа!")
    min_number = 1
    max_number = 15


b1 = Button(window, text='>', command=give_more)
b1.grid(row=0, column=1)

b2 = Button(window, text='<', command=give_less)
b2.grid(row=1, column=1)

b3 = Button(window, text='=', command=win)
b3.grid(row=2, column=1)

b4 = Button(window, text='Старт', command=generate_number)
b4.grid(row=3, column=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=0, column=2, rowspan=6, columnspan=2, sticky=(N, W, E, S))

sb1 = ttk.Scrollbar(window, orient=VERTICAL, command=list1.yview)
sb1.grid(row=0, column=4, rowspan=6, sticky=(N, S))

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()