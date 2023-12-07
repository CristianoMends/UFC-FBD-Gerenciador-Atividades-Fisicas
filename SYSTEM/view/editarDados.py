import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from dao.consulta import Consulta


class editarDados:
    def __init__(self):
        self.usuarioAtual = None

        root = tk.Tk()
        self.root = root
        self.root.title("Editar Dados")
        self.root.withdraw()

        self.textPeso = None
        self.textSobrenome = None
        self.textSenha = None
        self.textUsuario = None
        self.textNome = None
        self.textAltura = None
        self.consulta = Consulta()

        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_907=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_907["font"] = ft
        GLabel_907["fg"] = "#333333"
        GLabel_907["justify"] = "center"
        GLabel_907["text"] = "atualize seus dados"
        GLabel_907.place(x=150,y=5,width=221,height=30)

        self.dadosAtuais = tk.Label(root)
        self.dadosAtuais["fg"] = "#333333"
        self.dadosAtuais["justify"] = "left"
        self.dadosAtuais["text"] = "{}"
        self.dadosAtuais.place(x=50, y=30, width=400, height=25)

        GLabel_395=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_395["font"] = ft
        GLabel_395["fg"] = "#333333"
        GLabel_395["justify"] = "left"
        GLabel_395["text"] = "Nome"
        GLabel_395.place(x=50,y=70,width=70,height=25)

        self.textNome=tk.Entry(root)
        self.textNome["bg"] = "#ffffff"
        self.textNome["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textNome["font"] = ft
        self.textNome["fg"] = "#333333"
        self.textNome["justify"] = "left"
        self.textNome["text"] = ""
        self.textNome.place(x=50,y=90,width=200,height=30)

        GLabel_76=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_76["font"] = ft
        GLabel_76["fg"] = "#333333"
        GLabel_76["justify"] = "center"
        GLabel_76["text"] = "Sobrenome"
        GLabel_76.place(x=50,y=120,width=70,height=25)

        self.textSobrenome=tk.Entry(root)
        self.textSobrenome["bg"] = "#ffffff"
        self.textSobrenome["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textSobrenome["font"] = ft
        self.textSobrenome["fg"] = "#333333"
        self.textSobrenome["justify"] = "left"
        self.textSobrenome["text"] = ""
        self.textSobrenome.place(x=50,y=140,width=200,height=30)

        GLabel_506=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_506["font"] = ft
        GLabel_506["fg"] = "#333333"
        GLabel_506["justify"] = "left"
        GLabel_506["text"] = "Usuario"
        GLabel_506.place(x=260,y=70,width=70,height=25)

        self.textUsuario=tk.Entry(root)
        self.textUsuario["bg"] = "#ffffff"
        self.textUsuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textUsuario["font"] = ft
        self.textUsuario["fg"] = "#333333"
        self.textUsuario["justify"] = "left"
        self.textUsuario["text"] = ""
        self.textUsuario.place(x=260,y=90,width=200,height=30)

        GLabel_442=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_442["font"] = ft
        GLabel_442["fg"] = "#333333"
        GLabel_442["justify"] = "left"
        GLabel_442["text"] = "Senha"
        GLabel_442.place(x=260,y=120,width=70,height=25)

        self.textSenha=tk.Entry(root)
        self.textSenha["bg"] = "#ffffff"
        self.textSenha["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textSenha["font"] = ft
        self.textSenha["fg"] = "#333333"
        self.textSenha["justify"] = "left"
        self.textSenha["text"] = ""
        self.textSenha.place(x=260,y=140,width=200,height=30)

        GLabel_858=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_858["font"] = ft
        GLabel_858["fg"] = "#333333"
        GLabel_858["justify"] = "left"
        GLabel_858["text"] = "Nascimento"
        GLabel_858.place(x=50,y=180,width=70,height=25)

        self.textNascimento=tk.Entry(root)
        self.textNascimento["bg"] = "#ffffff"
        self.textNascimento["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textNascimento["font"] = ft
        self.textNascimento["fg"] = "#333333"
        self.textNascimento["justify"] = "left"
        self.textNascimento["text"] = ""
        self.textNascimento.place(x=50,y=200,width=100,height=25)

        GLabel_497=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_497["font"] = ft
        GLabel_497["fg"] = "#333333"
        GLabel_497["justify"] = "left"
        GLabel_497["text"] = "Peso"
        GLabel_497.place(x=50,y=230,width=70,height=25)

        self.textPeso=tk.Entry(root)
        self.textPeso["bg"] = "#ffffff"
        self.textPeso["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textPeso["font"] = ft
        self.textPeso["fg"] = "#333333"
        self.textPeso["justify"] = "left"
        self.textPeso["text"] = ""
        self.textPeso.place(x=50,y=250,width=100,height=25)

        GLabel_265=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_265["font"] = ft
        GLabel_265["fg"] = "#333333"
        GLabel_265["justify"] = "left"
        GLabel_265["text"] = "Altura"
        GLabel_265.place(x=50,y=290,width=70,height=25)

        self.textAltura=tk.Entry(root)
        self.textAltura["bg"] = "#ffffff"
        self.textAltura["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textAltura["font"] = ft
        self.textAltura["fg"] = "#333333"
        self.textAltura["justify"] = "left"
        self.textAltura["text"] = ""
        self.textAltura.place(x=50,y=310,width=99,height=25)

        self.btnFinalizar=tk.Button(root)
        self.btnFinalizar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btnFinalizar["font"] = ft
        self.btnFinalizar["fg"] = "#000000"
        self.btnFinalizar["justify"] = "center"
        self.btnFinalizar["text"] = "Atualizar"
        self.btnFinalizar.place(x=210,y=380,width=70,height=25)
        self.btnFinalizar["command"] = self.atualizar


    def atualizar(self):
        resposta = messagebox.askokcancel("Confirmação", "Tem certeza que deseja atualizar todos os seus dados?")
        if resposta:
            nome = self.textNome.get()
            sobrenome = self.textSobrenome.get()
            usuario = self.textUsuario.get()
            senha = self.textSenha.get()
            nascimento = self.textNascimento.get()
            peso = self.textPeso.get()
            altura = self.textAltura.get()

            if not (peso.replace('.', '', 1).isdigit() and altura.replace('.', '', 1).isdigit()):
                messagebox.showerror("Erro!", "Peso e Altura devem ser números.")
                return
            if not (len(nascimento) == 10 and
                    nascimento[2] == '/' and
                    nascimento[5] == '/' and
                    nascimento[:2].isdigit() and nascimento[3:5].isdigit() and
                    nascimento[6:].isdigit()):
                messagebox.showerror("Erro!", "Formato de data inválido. Use DD/MM/AAAA.")
                return

            if self.consulta.atualizar_usuario(self.usuarioAtual.id, nome,sobrenome, usuario, senha, nascimento, peso, altura):
                messagebox.showinfo("Sucesso!", "Dados atualizados com sucesso!")
                self.fechar()
            else:
                messagebox.showerror("Erro!", "Erro ao atualizar usuário!")
    def fechar(self):
        self.root.destroy()

    def show(self, usuarioAtual):
        self.usuarioAtual = usuarioAtual
        self.dadosAtuais["text"] = f"{self.usuarioAtual.toString()}"

        self.root.deiconify()
        self.root.mainloop()


