from tkinter import *
from tkinter import ttk, Button
import os

root = Tk()
root.title("Игрульки от Светки Отвертки")
root.geometry("300x250")


label = Label(text="\nПривет, игрок\n Выбери игру:", font=("Arial", 14))
label.pack()

def open_file():
    filename = "game1.py"
    os.system(f"start {filename}")
def close_window():
    root.destroy()

def open_file2():
    filename = "game2.py"
    os.system(f"start {filename}")
def close_window():
    root.destroy()
def exit_app():
    root.destroy()


btn = ttk.Button(text="Кнопка1")
btn = ttk.Button(root, text="Камень, ножницы , бумага", command=open_file)
btn.pack(pady = 10)
btn.pack()

btn2 = ttk.Button(text="Кнопка2")
btn2 = ttk.Button(root, text="Угадай число2", command=open_file2)
btn2.pack(pady = 10)
btn2.pack()

exit_button = ttk.Button(root, text = "Выход", command=exit_app)
exit_button.pack(pady = 10)
exit_button.pack()

root.mainloop()




root.mainloop()