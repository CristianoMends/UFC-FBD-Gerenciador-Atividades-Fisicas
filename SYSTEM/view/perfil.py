import tkinter as tk
import tkinter.font as tkFont

class Perfil:
    def __init__(self):
        self.usuarioAtual = None
        root = tk.Tk()
        self.root = root
        self.root.title("Perfil")
        self.root.withdraw()
        
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_733=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_733["font"] = ft
        GLabel_733["fg"] = "#333333"
        GLabel_733["justify"] = "center"
        GLabel_733["text"] = "Seu perfil"
        GLabel_733.place(x=160,y=20,width=260,height=25)

        GLabel_853=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_853["font"] = ft
        GLabel_853["fg"] = "#333333"
        GLabel_853["justify"] = "left"
        GLabel_853["text"] = "Usuario:"
        GLabel_853.place(x=20,y=60,width=60,height=30)

        GLabel_285=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_285["font"] = ft
        GLabel_285["fg"] = "#333333"
        GLabel_285["justify"] = "left"
        GLabel_285["text"] = "Peso:"
        GLabel_285.place(x=20,y=90,width=60,height=25)

        GLabel_252=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_252["font"] = ft
        GLabel_252["fg"] = "#333333"
        GLabel_252["justify"] = "left"
        GLabel_252["text"] = "Altura:"
        GLabel_252.place(x=20,y=120,width=60,height=25)

        GLabel_36=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_36["font"] = ft
        GLabel_36["fg"] = "#333333"
        GLabel_36["justify"] = "left"
        GLabel_36["text"] = "IMC:"
        GLabel_36.place(x=20,y=150,width=60,height=25)

        GListBox_45=tk.Listbox(self.root)
        GListBox_45["bg"] = "#ffffff"
        GListBox_45["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_45["font"] = ft
        GListBox_45["fg"] = "#333333"
        GListBox_45["justify"] = "center"
        GListBox_45.place(x=20,y=180,width=542,height=131)

        GLabel_229=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_229["font"] = ft
        GLabel_229["fg"] = "#333333"
        GLabel_229["justify"] = "left"
        GLabel_229["text"] = "Equipamento mais utilizado:"
        GLabel_229.place(x=20,y=330,width=185,height=25)

        self.textUsuario=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        self.textUsuario["font"] = ft
        self.textUsuario["fg"] = "#333333"
        self.textUsuario["justify"] = "left"
        self.textUsuario["text"] = f"{""}"
        self.textUsuario.place(x=80,y=60,width=170,height=25)

        self.textPeso=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        self.textPeso["font"] = ft
        self.textPeso["fg"] = "#333333"
        self.textPeso["justify"] = "left"
        self.textPeso["text"] = ""
        self.textPeso.place(x=80,y=90,width=70,height=25)

        self.textAltura=tk.Entry(self.root)
        self.textAltura["bg"] = "#ffffff"
        self.textAltura["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textAltura["font"] = ft
        self.textAltura["fg"] = "#333333"
        self.textAltura["justify"] = "left"
        self.textAltura["text"] = ""
        self.textAltura.place(x=80,y=120,width=70,height=25)

        self.textImc=tk.Entry(self.root)
        self.textImc["bg"] = "#ffffff"
        self.textImc["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textImc["font"] = ft
        self.textImc["fg"] = "#333333"
        self.textImc["justify"] = "left"
        self.textImc["text"] = ""
        self.textImc.place(x=80,y=150,width=70,height=25)

        self.eqUtilizado=tk.Entry(self.root)
        self.eqUtilizado["bg"] = "#ffffff"
        self.eqUtilizado["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.eqUtilizado["font"] = ft
        self.eqUtilizado["fg"] = "#333333"
        self.eqUtilizado["justify"] = "left"
        self.eqUtilizado["text"] = ""
        self.eqUtilizado.place(x=20,y=350,width=160,height=25)

        GLabel_659=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_659["font"] = ft
        GLabel_659["fg"] = "#333333"
        GLabel_659["justify"] = "left"
        GLabel_659["text"] = "Maior peso utilizado:"
        GLabel_659.place(x=20,y=380,width=150,height=25)

        self.textMaiorPeso=tk.Entry(self.root)
        self.textMaiorPeso["bg"] = "#ffffff"
        self.textMaiorPeso["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textMaiorPeso["font"] = ft
        self.textMaiorPeso["fg"] = "#333333"
        self.textMaiorPeso["justify"] = "left"
        self.textMaiorPeso["text"] = ""
        self.textMaiorPeso.place(x=20,y=400,width=115,height=25)

        GButton_836=tk.Button(self.root)
        GButton_836["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_836["font"] = ft
        GButton_836["fg"] = "#000000"
        GButton_836["justify"] = "center"
        GButton_836["text"] = "Editar dados"
        GButton_836.place(x=250,y=420,width=100,height=25)
        GButton_836["command"] = self.editarPerfil

        GButton_155=tk.Button(self.root)
        GButton_155["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_155["font"] = ft
        GButton_155["fg"] = "#000000"
        GButton_155["justify"] = "center"
        GButton_155["text"] = "Voltar"
        GButton_155.place(x=250,y=450,width=100,height=25)
        GButton_155["command"] = self.voltar

    def editarPerfil(self):
        print("command")


    def voltar(self):
        print("command")

    def show(self, usuarioAtual):
        self.usuarioAtual = usuarioAtual
        self.textUsuario["text"] = f"{self.usuarioAtual.nome}"
        self.textPeso["text"] = f"{self.usuarioAtual.peso}"
        self.textMaiorPeso["text"] = f"{self.cunsulta.getMaiorPesoUsuario()}"


        self.root.deiconify()  # Torna a janela visível
        self.root.mainloop()
