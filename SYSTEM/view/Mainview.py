import tkinter as tk
from tkinter import messagebox


class MainView:
    def __init__(self):
        pass

    def show(self):
        self.root = tk.Tk()
        self.root.title("Página Principal")
        self.root.configure(bg="white")  # Definindo o fundo da janela como branco
        self.root.geometry("500x500+100+100")
        self.root.resizable(False, False)  # Evita que a janela seja redimensionada


        # Botão para cadastrar exercício
        self.button_cadastrar_exercicio = tk.Button(self.root, text="Cadastrar Exercício",
                                                    command=self.cadastrarExercicio, bg="blue", fg="white")
        self.button_cadastrar_exercicio.pack(pady=10)

        # Botão para ver lista de exercícios
        self.button_ver_lista_exercicios = tk.Button(self.root, text="Ver Lista de Exercícios",
                                                     command=self.verListaExercicios, bg="green", fg="white")
        self.button_ver_lista_exercicios.pack(pady=10)
        self.root.mainloop()

    def hide(self):
        self.root.withdraw()

    def cadastrarExercicio(self):
        # Implemente a lógica para cadastrar um novo exercício aqui
        messagebox.showinfo("Cadastrar Exercício", "Lógica para cadastrar exercício a ser implementada")

    def verListaExercicios(self):
        # Implemente a lógica para exibir a lista de exercícios aqui
        messagebox.showinfo("Lista de Exercícios", "Lógica para ver lista de exercícios a ser implementada")

