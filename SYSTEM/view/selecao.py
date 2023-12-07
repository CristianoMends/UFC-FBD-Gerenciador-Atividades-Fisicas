import tkinter as tk
import tkinter.font as tkFont
from view.perfil import Perfil
from view.Treino import Treino
from view.comunidade import comunidade


class Selecao:
    def __init__(self):
        self.usuarioAtual = None
        self.perfil = Perfil()
        self.Treino = Treino()
        self.comunidade = comunidade()

        root = tk.Tk()
        self.root = root
        self.root.title("Selecao")
        self.root.withdraw()

        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        btnTreino=tk.Button(self.root)
        btnTreino["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnTreino["font"] = ft
        btnTreino["fg"] = "#000000"
        btnTreino["justify"] = "center"
        btnTreino["text"] = "Treino"
        btnTreino.place(x=100,y=170,width=100,height=25)
        btnTreino["command"] = self.showTreino

        GLabel_120=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_120["font"] = ft
        GLabel_120["fg"] = "#333333"
        GLabel_120["justify"] = "left"
        GLabel_120["text"] = "Veja treinos de outros usuarios."
        GLabel_120.place(x=220,y=110,width=250,height=25)

        GLabel_496=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_496["font"] = ft
        GLabel_496["fg"] = "#333333"
        GLabel_496["justify"] = "left"
        GLabel_496["text"] = "Registre seus treinos."
        GLabel_496.place(x=220,y=170,width=250,height=25)

        btnPerfil=tk.Button(self.root)
        btnPerfil["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnPerfil["font"] = ft
        btnPerfil["fg"] = "#000000"
        btnPerfil["justify"] = "center"
        btnPerfil["text"] = "Perfil"
        btnPerfil.place(x=100,y=230,width=100,height=25)
        btnPerfil["command"] = self.showPerfil

        GLabel_679=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_679["font"] = ft
        GLabel_679["fg"] = "#333333"
        GLabel_679["justify"] = "left"
        GLabel_679["text"] = "Veja seu perfil"
        GLabel_679.place(x=220,y=230,width=150,height=25)

        self.labelInicial=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=14)
        self.labelInicial["font"] = ft
        self.labelInicial["fg"] = "#333333"
        self.labelInicial["justify"] = "left"
        self.labelInicial["text"] = f"Olá {""} , Bem vindo!"
        self.labelInicial.place(x=180,y=30,width=250,height=25)

        btnComunidade=tk.Button(self.root)
        btnComunidade["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        btnComunidade["font"] = ft
        btnComunidade["fg"] = "#000000"
        btnComunidade["justify"] = "center"
        btnComunidade["text"] = "Comunidade"
        btnComunidade.place(x=100,y=110,width=100,height=25)
        btnComunidade["command"] = self.showComunidade

    def showTreino(self):
        self.root.withdraw()
        self.Treino.show(self.usuarioAtual,self)


    def showPerfil(self):
        self.root.withdraw()
        self.perfil.show(self.usuarioAtual, self)


    def showComunidade(self):
        self.root.withdraw()
        self.comunidade.show(self.usuarioAtual, self)

    def show(self, usuarioAtual):
        self.usuarioAtual = usuarioAtual
        self.labelInicial["text"] = f"Olá {usuarioAtual.nome} , Bem vindo!"
        self.root.deiconify()
        self.root.mainloop()