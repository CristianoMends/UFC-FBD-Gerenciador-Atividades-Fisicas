import psycopg2
from SYSTEM.model.Connection import Connection
from SYSTEM.view.LoginView import LoginView
from SYSTEM.view.Mainview import MainView
from SYSTEM.model.Exercise import Exercise
from SYSTEM.model.User import User


class APP:
    def __init__(self):
        connection = Connection()
        conn = connection.getConnection()
        self.cur = conn.cursor()
        self.psycopg = psycopg2

        self.loginView = LoginView()
        self.mainView = MainView()

        self.loginView.getBtnLogin().configure(command=self.checkLogin)

    def showLoginView(self):
        self.loginView.show()

    def hideLoginView(self):
        self.loginView.hide()

    def showMainView(self):
        self.mainView.show()

    def hideMainView(self):
        self.mainView.hide()

    def checkLogin(self):
        email = self.loginView.getEmail()
        senha = self.loginView.getPassword()
        try:
            self.cur.execute("SELECT * FROM LOGIN WHERE EMAIL = %s AND PASSWORD = %s", (email, senha))
            rows = self.cur.fetchall()
            if len(rows) > 0:
                self.loginView.destroy()
                self.mainView.show()
            else:
                self.loginView.showMessage("Erro", "Usuario nao encontrado","error")
        except (Exception, self.psycopg.DatabaseError) as error:
            print(error)




