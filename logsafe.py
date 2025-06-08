import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet
import os

# Parte do código que envolve a encriptagem das informações do usuário

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

if not os.path.exists("chave.key"): # Isso daqui serve pra gerar uma chave que descriptografa o arquivo .txt (só é gerada na primeira vez que o programa é rodado)
    gerar_chave()

chave = carregar_chave()
f = Fernet(chave)

def salvar_login(): # Aqui é onde os campos de entrada são mostrados para o usuário preencher com informações.
    email = entry_email.get()
    senha = entry_senha.get()

    if email and senha:
        email_criptografado = f.encrypt(email.encode())
        senha_criptografada = f.encrypt(senha.encode())

        with open("logins.txt", "ab") as arquivo:
            arquivo.write(email_criptografado + b"\n")
            arquivo.write(senha_criptografada + b"\n")

        messagebox.showinfo("Sucesso", "Login salvo com sucesso!")
        entry_email.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

def ver_logins(): # Parte do código na qual o usuário necessita digitar um PIN para ter acesso aos logins salvos no .txt
    pin_inserido = simpledialog.askstring("PIN", "Digite o PIN para ver os logins:", show='*')

    if pin_inserido == "1234":
        try:
            with open("logins.txt", "rb") as arquivo:
                linhas = arquivo.readlines() # Ele checa se existem linhas salvas no .txt, se sim, ele mostrará os logins

            if not linhas:
                messagebox.showinfo("Logins", "Nenhum login salvo ainda.") # Caso o usuário não tenha inserido nenhum login, nenhuma linha estará escrita no .txt (logo a mensagem de erro aparece)
                return

            logins_decodificados = "--- Carteira de Logins ---\n\n" # Tela na qual o programa mostra os logins salvos do usuário.
            for i in range(0, len(linhas), 2):
                email_criptografado = linhas[i].strip()
                senha_criptografada = linhas[i+1].strip()

                email = f.decrypt(email_criptografado).decode()
                senha = f.decrypt(senha_criptografada).decode()

                logins_decodificados += f"Email: {email}\nSenha: {senha}\n\n"

            # Janela para exibir os logins
            janela_logins = tk.Toplevel(janela)
            janela_logins.title("Logins Salvos")
            texto_logins = tk.Text(janela_logins, height=10, width=50)
            texto_logins.pack(padx=10, pady=10)
            texto_logins.insert(tk.END, logins_decodificados)
            texto_logins.config(state=tk.DISABLED) # Impede a edição

        except FileNotFoundError:
            messagebox.showinfo("Logins", "Nenhum login salvo ainda.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao ler os logins: {e}")

    elif pin_inserido is not None:
        messagebox.showerror("Erro", "PIN incorreto!") # Caso seja digitado algo diferente de 1234, que é o PIN exemplificado no programa, a mensagem de erro será mostrada.