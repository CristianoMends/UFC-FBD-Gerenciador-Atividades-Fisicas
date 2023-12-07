from datetime import datetime


class Usuario:
    def __init__(self,id:int, nome:str, sobrenome:str, data_nascimento, peso:float, altura:float):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        self.peso = peso
        self.altura = altura

    def toString(self):
        return f"Nome: {self.nome}, Sobrenome: {self.sobrenome}, Nasc: {self.data_nascimento}, Peso: {str(self.peso)}, Alt: {self.altura}"



class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha


class Exercicio:
    def __init__(self, nome, grupo_muscular, parte_muscular, equipamento, peso_utilizado, data, hora, repeticoes,
                 usuario):
        self.nome = nome
        self.grupo_muscular = grupo_muscular
        self.parte_muscular = parte_muscular
        self.equipamento = equipamento
        self.peso_utilizado = peso_utilizado
        self.data = datetime.strptime(data, "%Y-%m-%d").date()
        self.hora = datetime.strptime(hora, "%H:%M").time()
        self.repeticoes = repeticoes
        self.usuario = usuario

