import tkinter as tk
import tkinter.font as tkFont
from dao.consulta import Consulta
from tkinter import messagebox
from view.editarDados import editarDados


class Perfil:
    def __init__(self):
        self.consulta = Consulta()
        self.selecao = None
        self.usuarioAtual = None
        self.editarDados = editarDados()

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

        self.listBoxExercicios = tk.Listbox(self.root, bg="#ffffff", borderwidth="1px")
        self.listBoxExercicios.place(x=20, y=180, width=542, height=131)

        scrollbar = tk.Scrollbar(self.root)
        scrollbar.place(x=562, y=180, height=131)
        self.listBoxExercicios.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listBoxExercicios.yview)

        GLabel_229=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_229["font"] = ft
        GLabel_229["fg"] = "#333333"
        GLabel_229["justify"] = "left"
        GLabel_229["text"] = "Equipamento mais utilizado:"
        GLabel_229.place(x=20,y=330,width=200,height=25)

        self.textUsuario=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        self.textUsuario["font"] = ft
        self.textUsuario["fg"] = "#333333"
        self.textUsuario["justify"] = "left"
        self.textUsuario["text"] = f"{""}"
        self.textUsuario.place(x=80,y=60,width=100,height=25)

        self.textPeso=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        self.textPeso["font"] = ft
        self.textPeso["fg"] = "#333333"
        self.textPeso["justify"] = "left"
        self.textPeso["text"] = ""
        self.textPeso.place(x=80,y=90,width=100,height=25)

        self.textAltura=tk.Label(self.root)
        self.textAltura["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textAltura["font"] = ft
        self.textAltura["fg"] = "#333333"
        self.textAltura["justify"] = "left"
        self.textAltura["text"] = ""
        self.textAltura.place(x=80,y=120,width=100,height=25)

        self.textImc=tk.Label(self.root)
        self.textImc["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textImc["font"] = ft
        self.textImc["fg"] = "#333333"
        self.textImc["justify"] = "left"
        self.textImc["text"] = ""
        self.textImc.place(x=80,y=150,width=70,height=25)

        self.eqUtilizado=tk.Label(self.root)
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

        self.textMaiorPeso=tk.Label(self.root)
        self.textMaiorPeso["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.textMaiorPeso["font"] = ft
        self.textMaiorPeso["fg"] = "#333333"
        self.textMaiorPeso["justify"] = "left"
        self.textMaiorPeso["text"] = ""
        self.textMaiorPeso.place(x=20,y=400,width=115,height=25)

        self.btnEditar=tk.Button(self.root)
        self.btnEditar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        self.btnEditar["font"] = ft
        self.btnEditar["fg"] = "#000000"
        self.btnEditar["justify"] = "center"
        self.btnEditar["text"] = "Editar dados"
        self.btnEditar.place(x=250,y=420,width=100,height=25)
        self.btnEditar["command"] = self.editarPerfil

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
        self.btnEditar.destroy()
        self.editarDados.show(self.usuarioAtual)

    def mensagem(self):
        messagebox.showinfo("Aviso", "Você não pode mais editar seus dados!")


    def voltar(self):
        resposta = messagebox.askokcancel("Confirmação", "Deseja voltar para Login?")
        if resposta:
            self.root.withdraw()
            self.selecao.show(self.usuarioAtual)

    def show_exercicios(self):
        exercicios = self.consulta.getExerciciosUsuario(self.usuarioAtual.id)

        self.listBoxExercicios.delete(0, tk.END)

        for exercicio in exercicios:
            exercicio_str = (f"{exercicio['nome']} | {exercicio['grupo_muscular']} | {exercicio['parte_muscular']} | "
                             f"{exercicio['equipamento']} | {exercicio['peso_utilizado']} | {exercicio['data']} | "
                             f"{exercicio['hora']} | {exercicio['repeticoes']}")
            self.listBoxExercicios.insert(tk.END, exercicio_str)

    def show(self, usuarioAtual, selecao):
        self.selecao = selecao
        self.usuarioAtual = usuarioAtual

        id:int = self.usuarioAtual.id
        nome:str = self.usuarioAtual.nome
        peso:float = self.usuarioAtual.peso
        altura:float = self.usuarioAtual.altura
        imc:float = peso/(altura*altura)
        maiorPeso = self.consulta.getMaiorPesoUsuario(id)
        eqUtilizado = self.consulta.getEqMaisUtilizado(id)

        self.textUsuario["text"] = f"{nome}"
        self.textPeso["text"] = f"{str(peso)}"
        self.textMaiorPeso["text"] = f"{"Nenhum" if maiorPeso is None else maiorPeso}"
        self.textImc["text"] = "{:.2f}".format(imc)
        self.textAltura["text"] = f"{altura}"
        self.eqUtilizado["text"] = f"{"Nenhum" if eqUtilizado is None else eqUtilizado}"

        self.show_exercicios()
        self.root.deiconify()
        self.root.mainloop()
