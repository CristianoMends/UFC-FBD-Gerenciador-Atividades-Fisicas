import tkinter as tk
from tkinter import messagebox
import psycopg2

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack()

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        self.botao_entrar = tk.Button(root, text="Entrar", command=self.verificar_login)
        self.botao_entrar.pack()

        self.botao_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.botao_cadastrar.pack()

    def conectar_banco(self):
        try:
            conn = psycopg2.connect(
                dbname="registro_academia",
                user="postgres",
                password="cristiano1234",
                host="localhost",
                port="5432"
            )
            return conn
        except psycopg2.Error as e:
            self.exibir_erro("Erro ao conectar ao banco de dados", e)
            return None

    def exibir_erro(self, titulo, mensagem):
        messagebox.showerror(titulo, mensagem)

    def verificar_login(self):
        conn = self.conectar_banco()

        if conn:
            usuario = self.entry_usuario.get()
            senha = self.entry_senha.get()

            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM login WHERE usuario = %s AND senha = %s;", (usuario, senha))
                resultado = cursor.fetchone()

                if resultado:
                    self.exibir_mensagem("Login", "Login bem-sucedido!")
                    self.abrir_tela_principal()
                else:
                    self.exibir_erro("Login", "Login falhou. Verifique seu usuário e senha.")
            except psycopg2.Error as e:
                self.exibir_erro("Erro ao verificar login", e)

            conn.close()

    def cadastrar_usuario(self):
        conn = self.conectar_banco()

        if conn:
            usuario = self.entry_usuario.get()
            senha = self.entry_senha.get()

            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO login (usuario, senha) VALUES (%s, %s);", (usuario, senha))
                conn.commit()
                self.exibir_mensagem("Cadastro", "Cadastro bem-sucedido! Você pode fazer login agora.")
            except psycopg2.IntegrityError as e:
                self.exibir_erro("Cadastro", "Usuário já cadastrado. Escolha outro usuário.")
            except psycopg2.Error as e:
                self.exibir_erro("Erro ao cadastrar usuário", e)

            conn.close()

    def abrir_tela_principal(self):
        messagebox.showinfo("ok")

    def exibir_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
