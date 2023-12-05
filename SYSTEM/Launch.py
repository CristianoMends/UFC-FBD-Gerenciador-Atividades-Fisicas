import tkinter as tk

from model.entidades import Usuario
import view.Login
from view.Cadastro import Cadastro

class Launch:
    def __init__(self):
        self.login = view.Login.Login()
        self.cadastro = Cadastro(self.login)

    def run(self):
        self.login.show()


if __name__ == "__main__":
    Launch().run()
