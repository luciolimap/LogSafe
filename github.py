from tkinter import *
janela = Tk()
janela.title("LogSafe")
janela.geometry("980x550")

label = Label(janela, text="Carteira de Logins", font=("Myriad Pro", 30), bg="light grey", fg="White")
label.grid(column=0, row=0)

bot = Button(janela, text="Acessar Carteira", bg="black", fg="white", width="20", font=("Myriad Pro", 15))
bot.grid(column=1, row=0)
janela.mainloop()