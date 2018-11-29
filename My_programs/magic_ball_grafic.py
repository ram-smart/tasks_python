from tkinter import *
from tkinter import messagebox
from random import randint

dict = {
    1: 'Бесспорно',
    2: 'Предрешено',
    3: 'Никаких сомнений',
    4: 'Определённо да',
    5: 'Можешь быть уверен в этом',
    6: 'Мне кажется — «да»',
    7: 'Вероятнее всего',
    8: 'Хорошие перспективы',
    9: 'Знаки говорят — «да»',
    10: 'Да',
    11: 'Пока не ясно, попробуй снова',
    12: 'Спроси позже',
    13: 'Лучше не рассказывать',
    14: 'Сейчас нельзя предсказать',
    15: 'Сконцентрируйся и спроси опять',
    16: 'Даже не думай',
    17: 'Мой ответ — «нет»',
    18: 'По моим данным — «нет»',
    19: 'Перспективы не очень хорошие',
    20: 'Весьма сомнительно'
}
def select():
    key = randint(1, 20)
    result.set(dict[key])
    messagebox.showinfo("Ответ", result.get())

root = Tk()
root.title("Магический шар")
root.geometry("350x350")

result = StringVar()

header = Label(text = "Привет, я программа \"Магический шар\" "
                      "\nЗадай вопрос, нажми на кнопку \"Ответ\"", padx=15, pady=15)
header.pack(side = TOP)

btn = Button(text = "Ответ", background="green", foreground="black", font="Verdana 13",
             padx=5, pady=5, command=select)
btn.place(relx=.3, rely=.3, relheight=.3, relwidth=.3)

root.mainloop()