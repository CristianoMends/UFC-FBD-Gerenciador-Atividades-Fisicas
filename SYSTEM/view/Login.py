import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

from dao.consulta import Consulta
from view.Cadastro import Cadastro
from view.selecao import Selecao
from Launch import Launch


class Login:
    def __init__(self):
        self.consulta = Consulta()
        self.cadastro = Cadastro(self)
        self.selecao = Selecao()

        root = tk.Tk()
        self.root = root
        self.root.title("Login")

        self.textUsuario = None
        self.textSenha = None

        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_307 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_307["font"] = ft
        GLabel_307["fg"] = "#333333"
        GLabel_307["justify"] = "center"
        GLabel_307["text"] = "Login"
        GLabel_307.place(x=270, y=40, width=70, height=25)

        GLabel_186 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_186["font"] = ft
        GLabel_186["fg"] = "#333333"
        GLabel_186["justify"] = "left"
        GLabel_186["text"] = "Usuario"
        GLabel_186.place(x=160, y=90, width=70, height=25)

        self.textUsuario = tk.Entry(root)
        self.textUsuario["bg"] = "#ffffff"
        self.textUsuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.textUsuario["font"] = ft
        self.textUsuario["fg"] = "#333333"
        self.textUsuario["justify"] = "left"
        self.textUsuario["text"] = ""
        self.textUsuario.place(x=160, y=110, width=250, height=30)

        GLabel_905 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_905["font"] = ft
        GLabel_905["fg"] = "#333333"
        GLabel_905["justify"] = "left"
        GLabel_905["text"] = "Senha"
        GLabel_905.place(x=160, y=160, width=70, height=25)

        self.textSenha = tk.Entry(root)
        self.textSenha["bg"] = "#ffffff"
        self.textSenha["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.textSenha["font"] = ft
        self.textSenha["fg"] = "#333333"
        self.textSenha["justify"] = "left"
        self.textSenha["text"] = ""
        self.textSenha["show"] = "*"
        self.textSenha.place(x=160, y=180, width=250, height=30)

        self.btnEntrar = tk.Button(root)
        self.btnEntrar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.btnEntrar["font"] = ft
        self.btnEntrar["fg"] = "#000000"
        self.btnEntrar["justify"] = "center"
        self.btnEntrar["text"] = "Entrar"
        self.btnEntrar.place(x=250, y=240, width=100, height=25)
        self.btnEntrar["command"] = self.verificar_login

        self.btnCadastrar = tk.Button(root)
        self.btnCadastrar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        self.btnCadastrar["font"] = ft
        self.btnCadastrar["fg"] = "#000000"
        self.btnCadastrar["justify"] = "center"
        self.btnCadastrar["text"] = "Cadastrar-se"
        self.btnCadastrar.place(x=250, y=270, width=100, height=25)
        self.btnCadastrar["command"] = self.cadastrar_usuario

    def cadastrar_usuario(self):
        self.root.withdraw()
        self.cadastro.show()

    def verificar_login(self):
        usuario = self.textUsuario.get()
        senha = self.textSenha.get()

        usuario_encontrado = self.consulta.verificar_login(usuario, senha)

        if usuario_encontrado is not None:
            messagebox.showinfo("Sucesso", "Seja bem vindo")

            self.root.withdraw()
            self.selecao.show(usuario_encontrado)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def show(self):
        self.root.deiconify()
        self.root.mainloop()
