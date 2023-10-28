import tkinter as tk
from APP import APP


app = APP()

class View:
    def __init__(self):
        self.root = tk.Tk()

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        self.password_label = tk.Label(self.root, text="Senha:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Entrar", command=self.login)
        self.login_button.pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if app.hasLogin(email, password):
            print("entrando")
        else:
            print("Usuario não encontrado")

    def run(self):
        self.root.mainloop()

view = View()
view.run()
