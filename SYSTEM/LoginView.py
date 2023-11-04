import tkinter as tk
from tkinter import  messagebox

#ShowMessage(root,"titulo","mensagem","error")


class ShowMessage:
    def __init__(self, root,title,message,type = "info"):
        self.root = root
        self.root.title(title)

        # Botão para exibir a mensagem
        self.show_message(title,message,type)

    def show_message(self,title,message,type = "info"):
        if type == "info":
            messagebox.showinfo(title, message)
        elif type == "error":
            messagebox.showerror(title,message)
        else:
            return Exception
class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela de Login")
        self.root.configure(bg="black")  # Definindo o fundo da janela como preto

        self.username = tk.StringVar()
        self.password = tk.StringVar()


        label_usuario = tk.Label(root, text="Email:", bg="black", fg="white")
        label_usuario.pack()

        entry_usuario = tk.Entry(root, textvariable=self.username, bg="gray", fg="white")
        entry_usuario.pack()

        label_senha = tk.Label(root, text="Senha:", bg="black", fg="white")
        label_senha.pack()

        entry_senha = tk.Entry(root, textvariable=self.password, show="*", bg="gray", fg="white")
        entry_senha.pack()

        # Frame para os botões
        button_frame = tk.Frame(root, bg="black")
        button_frame.pack()

        # Botão de login
        button_login = tk.Button(button_frame, text="Entrar", command=self.verificar_login, bg="white", fg="black")
        button_login.pack(side=tk.LEFT, padx=5, pady=5)

        # Botão de criar conta
        button_criar_conta = tk.Button(button_frame, text="Criar Conta", command=self.criar_conta, bg="white", fg="black")
        button_criar_conta.pack(side=tk.LEFT, padx=5, pady=5)

    def verificar_login(self):
        if self.username.get() == "usuario" and self.password.get() == "senha":
            print("Login bem-sucedido!")
            
        else:
            print("Nome de usuário ou senha incorretos")

    def criar_conta(self):
        #falta o script
        print("insira o script do banco de daods")