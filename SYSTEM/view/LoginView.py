import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela de Login")
        self.bg_color = "black"
        self.label_color = "black"
        self.entry_bg_color = "#34495E"
        self.button_bg_color = "#E67E22"
        self.width = 500
        self.heith = 250
        self.text_color = "white"

        self.root.configure(bg=self.bg_color)
        self.root.geometry(f"{self.width}x{self.heith}+100+100")
        self.root.resizable(False, False)

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        welcome = tk.Label(self.root, text="Bem vindo!", bg=self.label_color, fg=self.text_color)
        welcome.place(x=(self.width/2)-20, y=10)

        welcome_text = tk.Label(self.root, text="Digite seu email e senha para entrar, ou clique em criar conta para criar uma nova conta!", bg=self.label_color, fg=self.text_color)
        welcome_text.place(x=10, y=30)

        label_usuario = tk.Label(self.root, text="Email:", bg=self.label_color, fg=self.text_color)
        label_usuario.place(x=50, y=80)

        entry_email = tk.Entry(self.root, textvariable=self.email, bg=self.entry_bg_color, fg=self.text_color, width=30)
        entry_email.place(x=100, y=80)

        label_password = tk.Label(self.root, text="Senha:", bg=self.label_color, fg=self.text_color)
        label_password.place(x=50, y=105)

        entry_password = tk.Entry(self.root, textvariable=self.password, show="*", bg=self.entry_bg_color, fg=self.text_color, width=30)
        entry_password.place(x=100, y=105)

        button_frame = tk.Frame(self.root, bg=self.label_color)
        button_frame.place(x=50, y=155)

        self.button_login = tk.Button(button_frame, text="Entrar", bg=self.button_bg_color, fg=self.text_color, width=10)
        self.button_login.pack(side=tk.LEFT, padx=5, pady=5)

        button_criar_conta = tk.Button(button_frame, text="Criar Conta", command=self.showCreateAccount, bg=self.button_bg_color, fg=self.text_color, width=10)
        button_criar_conta.pack(side=tk.LEFT, padx=5, pady=5)

    def show(self):
        self.root.mainloop()

    def hide(self):
        self.root.withdraw()

    def destroy(self):
        self.root.destroy()

    def showMessage(self, title, message, type):
        if type == "info":
            messagebox.showinfo(title, message)
        elif type == "error":
            messagebox.showerror(title, message)
        else:
            return Exception

    def showCreateAccount(self):
        #falta o script
        print("insira o script do banco de dados")

    def getEmail(self):
        return self.email.get()

    def getPassword(self):
        return self.password.get()

    def getBtnLogin(self):
        return self.button_login