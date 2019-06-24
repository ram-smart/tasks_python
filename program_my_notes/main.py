from tkinter import *
from functions import *


root = Tk()
root.title("Программа Заметки")
root.geometry("400x400+900+50")

btn_new_note = Button(text="Новая заметка")
btn_new_note.pack()

btn_settings = Button(text="Настройки")
btn_settings.pack()







root.mainloop()
