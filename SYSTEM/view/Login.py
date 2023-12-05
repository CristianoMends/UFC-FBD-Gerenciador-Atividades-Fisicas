import tkinter as tk
from tkinter import messagebox
import psycopg2

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")

        self.label_usuario = tk.Label(self.root, text="Usuário:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(self.root, text="Senha:")
        self.label_senha.pack()

        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack()

        self.botao_entrar = tk.Button(self.root, text="Entrar", command=self.verificar_login)
        self.botao_entrar.pack()

        self.botao_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_usuario)
        self.botao_cadastrar.pack()


    def exibir_tela_login(self):
        self.root.deiconify()  # Torna a janela visível
        self.root.mainloop()
