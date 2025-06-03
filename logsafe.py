from tkinter import *

janela = Tk()
janela.title("LogSafe")
janela.geometry("980x550")
janela.configure(bg="#1f1f1f")

label = Label(janela, text="Carteira de Logins", font=("Myriad Pro", 30), bg="#1f1f1f", fg="White")
label.pack(pady=10)

pin_entry = Entry(janela,width=10,  bg="#383434", fg="white")
pin_entry.pack(pady=50)

bot = Button(janela, text="Acessar Carteira", bg="black", fg="white", width="20", font=("Myriad Pro", 15))
bot.pack(pady=50)



pin_value = pin_entry.get()

janela.mainloop()