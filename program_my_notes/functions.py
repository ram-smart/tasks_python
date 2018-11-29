def new_window():
    root = Tk()
    root.title("Заметка")
    root.geometry("400x400+500+50")
    btn_new_note = Button(text="Новая заметка")
    btn_new_note.pack()
    root.mainloop()
