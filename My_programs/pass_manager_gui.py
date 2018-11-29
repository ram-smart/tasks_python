import tkinter
import sqlite3

root = tkinter.Tk()
root.title(root)
root.geometry('400x400')

btn = tkinter.Button(text = 'Создать раздел',
                     padx = '5',
                     pady = '5',
                     font = 'Arial 11',
                     activeforeground = '#0040FF',
                     highlightcolor = '#0040FF')
btn.pack()

btn = tkinter.Button(text = 'Трейдинг',
                     padx = '5',
                     pady = '5',
                     font = 'Arial 11',
                     activeforeground = '#0040FF',
                     highlightcolor = '#0040FF')
btn.pack()

root.mainloop()
