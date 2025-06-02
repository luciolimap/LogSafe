from tkinter import *

janela = Tk()
janela.title("LogSafe")
janela.geometry("980x550")
janela.configure(bg="#1f1f1f")

label = Label(janela, text="Carteira de Logins", font=("Myriad Pro", 30), bg="black", fg="White")
label.grid(column=2, row=0)

bot = Button(janela, text="Acessar Carteira", bg="black", fg="white", width="20", font=("Myriad Pro", 15))
bot.grid(column=2, row=3)

pin_entry = Entry(janela,width=10)
pin_entry.grid(column=2, row=2)

pin_value = pin_entry.get()

janela.mainloop()