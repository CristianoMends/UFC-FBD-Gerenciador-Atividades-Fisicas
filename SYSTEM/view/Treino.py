import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from dao.consulta import Consulta
import datetime
from tkinter import messagebox

class Treino:
    def __init__(self):
        self.consulta = Consulta()
        self.selecao = None
        self.usuarioAtual = None
        
        root = tk.Tk()
        self.root = root
        self.root.title("Treino")
        self.root.withdraw()

        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=13)

        GLabel_736=tk.Label(self.root)
        GLabel_736["font"] = ft
        GLabel_736["fg"] = "#333333"
        GLabel_736["justify"] = "left"
        GLabel_736["text"] = "Registre seu treino"
        GLabel_736.place(x=200,y=30,width=170,height=25)

        self.textNome=tk.Entry(self.root)
        self.textNome["bg"] = "#ffffff"
        self.textNome["borderwidth"] = "1px"
        self.textNome["font"] = ft
        self.textNome["fg"] = "#333333"
        self.textNome["justify"] = "left"
        self.textNome["text"] = ""
        self.textNome.place(x=110,y=90,width=250,height=25)

        GLabel_342=tk.Label(self.root)
        GLabel_342["fg"] = "#333333"
        GLabel_342["justify"] = "left"
        GLabel_342["text"] = "Nome do exercicio"
        GLabel_342.place(x=110,y=60,width=150,height=25)

        GLabel_119=tk.Label(self.root)
        GLabel_119["fg"] = "#333333"
        GLabel_119["justify"] = "left"
        GLabel_119["text"] = "Grupo Muscular"
        GLabel_119.place(x=110,y=130,width=150,height=25)

        self.gpMuscular_var = tk.StringVar()
        gpMuscular = [
            "Pernas", "Braços", "Costas", "Peito", "Abdômen", "Ombros"
        ]
        self.combobox_gpMuscular = ttk.Combobox(self.root, textvariable=self.gpMuscular_var, values=gpMuscular,state='readonly')
        self.combobox_gpMuscular.place(x=110,y=150,width=250,height=25)

        GLabel_87=tk.Label(self.root)
        GLabel_87["fg"] = "#333333"
        GLabel_87["justify"] = "left"
        GLabel_87["text"] = "Parte Muscular"
        GLabel_87.place(x=110,y=190,width=150,height=25)

        self.ptMuscular_var = tk.StringVar()
        ptMuscular = [
            "Quadríceps","Isquiotibiais","Panturrilhas","Bíceps","Tríceps","Antebraço",
            "Latíssimo do dorso","Trapézio","Dorsais","Peitoral maior","Peitoral menor","Reto abdominal",
            "Oblíquos","Deltoides","Trapezius", "Outro"
        ]
        pt = sorted(ptMuscular)
        self.combobox_ptMuscular = ttk.Combobox(self.root, textvariable=self.ptMuscular_var, values=pt,state='readonly')
        self.combobox_ptMuscular.place(x=110,y=210,width=250,height=25)

        GLabel_486=tk.Label(self.root)
        GLabel_486["fg"] = "#333333"
        GLabel_486["justify"] = "left"
        GLabel_486["text"] = "equipamento"
        GLabel_486.place(x=110,y=250,width=150,height=25)

        self.equipamento_var = tk.StringVar()
        equipamentos = [
            "Esteira ergométrica", "Bicicleta ergométrica","Supino Reto", "Elíptico", "Stepper",
            "Máquina de remo", "Máquina de musculação", "Banco inclinado",
            "Banco declinado", "Banco reto", "Smith machine", "Barra fixa",
            "Leg press", "Crossover", "Pulley", "Hack squat", "Máquina de abdominais",
            "Máquina de flexão de pernas", "Máquina de extensão de pernas",
            "Máquina de adução e abdução de quadril", "Plataforma vibratória",
            "Kettlebells", "Medicine balls", "Bosu ball", "TRX (suspension training)",
            "Escada de agilidade", "Escada de coordenação", "Steps", "Halteres",
            "Barra olímpica", "Colchonetes de yoga e pilates", "Outro"
        ]
        equipamento = sorted(equipamentos)
        self.combobox_equipamento = ttk.Combobox(self.root, textvariable=self.equipamento_var, values=equipamento,state='readonly')
        self.combobox_equipamento.place(x=110,y=270,width=250,height=25)

        GLabel_583=tk.Label(self.root)
        GLabel_583["fg"] = "#333333"
        GLabel_583["justify"] = "left"
        GLabel_583["text"] = "Peso"
        GLabel_583.place(x=110,y=310,width=70,height=25)

        self.textPeso=tk.Entry(self.root)
        self.textPeso["borderwidth"] = "1px"
        self.textPeso["fg"] = "#333333"
        self.textPeso["justify"] = "left"
        self.textPeso["text"] = ""
        self.textPeso.place(x=110,y=330,width=100,height=25)

        GLabel_423=tk.Label(self.root)
        GLabel_423["fg"] = "#333333"
        GLabel_423["justify"] = "left"
        GLabel_423["text"] = "Repetições"
        GLabel_423.place(x=110,y=370,width=70,height=25)

        self.textRepeticoes=tk.Entry(self.root)
        self.textRepeticoes["borderwidth"] = "1px"
        self.textRepeticoes["fg"] = "#333333"
        self.textRepeticoes["justify"] = "left"
        self.textRepeticoes["text"] = ""
        self.textRepeticoes.place(x=110,y=390,width=100,height=25)

        GButton_479=tk.Button(self.root)
        GButton_479["bg"] = "#f0f0f0"
        GButton_479["fg"] = "#000000"
        GButton_479["justify"] = "left"
        GButton_479["text"] = "Registrar"
        GButton_479.place(x=260,y=420,width=70,height=25)
        GButton_479["command"] = self.registrar

        GButton_375=tk.Button(self.root)
        GButton_375["bg"] = "#f0f0f0"
        GButton_375["fg"] = "#000000"
        GButton_375["justify"] = "left"
        GButton_375["text"] = "Cancelar"
        GButton_375.place(x=260,y=450,width=70,height=25)
        GButton_375["command"] = self.cancelar

    def registrar(self):
        nome = self.textNome.get()
        gpMuscular = self.combobox_gpMuscular.get()
        ptMuscular = self.combobox_ptMuscular.get()
        equipamento = self.combobox_equipamento.get()
        peso = self.textPeso.get()
        repeticoes = self.textRepeticoes.get()
        data = datetime.date.today()
        hora = datetime.datetime.now().time().strftime("%H:%M:%S")

        if self.consulta.cadastrar_exercicio(self.usuarioAtual.id,nome, gpMuscular, ptMuscular, equipamento, peso, data, hora, repeticoes):
           messagebox.showinfo("Sucesso!", "Exercicio cadastrado com sucesso!")
        else:
          messagebox.showerror("Erro!", "Erro ao cadastrar exercicio!")
    def cancelar(self):
        self.voltar()
    def voltar(self):
        resposta = messagebox.askokcancel("Confirmação", "Deseja voltar?")
        if resposta:
            self.root.withdraw()
            self.selecao.show(self.usuarioAtual)
        
    def show(self, usuarioAtual, selecao):
        self.selecao = selecao
        self.usuarioAtual = usuarioAtual

        self.root.deiconify()
        self.root.mainloop()
