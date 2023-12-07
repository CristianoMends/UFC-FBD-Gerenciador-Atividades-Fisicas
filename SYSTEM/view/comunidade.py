import tkinter as tk
import tkinter.font as tkFont
from dao.consulta import Consulta
from tkinter import messagebox
from tkinter import ttk


class comunidade:
    def __init__(self):
        self.consulta = Consulta()
        self.selecao = None
        self.usuarioAtual = None

        root = tk.Tk()
        self.root = root
        self.root.title("Comunidade")
        self.root.withdraw()

        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_436=tk.Label(root)
        GLabel_436["fg"] = "#333333"
        GLabel_436["justify"] = "center"
        GLabel_436["text"] = "Comunidade"
        GLabel_436.place(x=280,y=0,width=100,height=25)

        GButton_812=tk.Button(root)
        GButton_812["bg"] = "#f0f0f0"
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Voltar"
        GButton_812.place(x=300,y=410,width=70,height=25)
        GButton_812["command"] = self.voltar

        GLabel_794=tk.Label(root)
        GLabel_794["fg"] = "#333333"
        GLabel_794["justify"] = "left"
        GLabel_794["text"] = "  Top 3 Maior peso por equipamento:"
        GLabel_794.place(x=180,y=50,width=220,height=25)

        self.equipamentos1_var = tk.StringVar()
        equipamentos = self.consulta.getListaEquipamentos()
        self.eq = sorted(equipamentos)
        self.combobox_eq1 = ttk.Combobox(self.root, textvariable=self.equipamentos1_var, values=self.eq,
                                         state='readonly')
        self.combobox_eq1.place(x=400,y=50,width=112,height=25)
        self.combobox_eq1.bind("<<ComboboxSelected>>", self.showTop1)


        self.listBox1 = tk.Listbox(self.root, bg="#ffffff", borderwidth="1px")
        self.listBox1.place(x=180,y=80,width=331,height=63)

        scrollbar1 = tk.Scrollbar(self.root)
        scrollbar1.place(x=150,y=80,height=63)
        self.listBox1.config(yscrollcommand=scrollbar1.set)
        scrollbar1.config(command=self.listBox1.yview)

        GLabel_282=tk.Label(root)
        GLabel_282["fg"] = "#333333"
        GLabel_282["justify"] = "left"
        GLabel_282["text"] = "Top 3 Mais sessões registradas"
        GLabel_282.place(x=180,y=160,width=220,height=25)

        GButton_812 = tk.Button(root)
        GButton_812["bg"] = "#f0f0f0"
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Atualizar"
        GButton_812.place(x=400,y=160,width=112,height=25)
        GButton_812["command"] = self.showTop2

        self.listBox2 = tk.Listbox(self.root, bg="#ffffff", borderwidth="1px")
        self.listBox2.place(x=180,y=190,width=331,height=63)

        scrollbar2 = tk.Scrollbar(self.root)
        scrollbar2.place(x=150, y=80, height=63)
        self.listBox2.config(yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=self.listBox2.yview)

        GLabel_530=tk.Label(root)
        GLabel_530["fg"] = "#333333"
        GLabel_530["justify"] = "center"
        GLabel_530["text"] = "Estatisticas mensais"
        GLabel_530.place(x=250,y=20,width=150,height=25)

    def voltar(self):
        resposta = messagebox.askokcancel("Confirmação", "Deseja voltar para Login?")
        if resposta:
            self.root.withdraw()
            self.selecao.show(self.usuarioAtual)

    def showTop1(self,event=None):
        self.listBox1.delete(0, tk.END)

        resultados = self.consulta.obterTopPesoUtilizado(self.combobox_eq1.get())

        if resultados:
            for resultado in resultados:
                texto = f"{resultado[0]} - {resultado[1]}"
                self.listBox1.insert(tk.END, texto)
    def showTop2(self,event=None):
        self.listBox2.delete(0, tk.END)
        resultados = self.consulta.obterTopSessoes()

        if resultados:
            for resultado in resultados:
                texto = f"{resultado[0]} - {resultado[1]}"
                self.listBox2.insert(tk.END, texto)

    def showTop3(self,event=None):
        self.listBox1.delete(0, tk.END)

        resultados = self.consulta.obterTopPesoUtilizado(self.combobox_eq1.get())

        if resultados:
            for resultado in resultados:
                texto = f"{resultado[0]} - {resultado[1]}"
                self.listBox1.insert(tk.END, texto)

    def show(self, usuarioAtual, selecao):
        self.selecao = selecao
        self.usuarioAtual = usuarioAtual

        self.root.deiconify()
        self.root.mainloop()

