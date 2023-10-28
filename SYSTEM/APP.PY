import psycopg2

from Connection import Connection
from User import User


class APP:
    def __init__(self):
        connection = Connection()
        conn = connection.getConnection()
        cur = conn.cursor()

    # checa se existe um login cadastrado para o email e senha informados
    def hasLogin(self, email, senha):
        try:
            self.cur.execute("SELECT * FROM LOGIN WHERE EMAIL = %s AND PASSWORD = %s", (email, senha))
            rows = self.cur.fetchall()
            if len(rows) > 0:
                return True
            else:
                return False
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # retorna instancia de User pelo id
    def getUser(self, email, password):
        try:
            self.cur.execute(
                "SELECT u.* FROM USER_ u INNER JOIN LOGIN l ON u.USER_ID = l.LOGIN_ID WHERE l.EMAIL = %s AND l.PASSWORD = %s",
                (email, password))
            user_data = self.cur.fetchone()
            if user_data:
                return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
            else:
                return None
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    # ---------------------------
    # crie login com informações de usuario e login e insere nas tabelas
    def createLogin(self, first_name, last_name, date_birth, weight, height, email, password):
        try:
            self.cur.execute("""
                INSERT INTO USER_ (FIST_NAME, LAST_NAME, DATE_BIRTH, WEIGHT, HEIGTH)
                VALUES (%s, %s, %s, %s, %s) RETURNING USER_ID;
            """, (first_name, last_name, date_birth, weight, height))
            user_id = self.cur.fetchone()[0]

            self.cur.execute("""
               INSERT INTO LOGIN (EMAIL, PASSWORD, USER_ID)
               VALUES (%s, %s, %s);
            """, (email, password, user_id))

            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(f"Ocorreu um erro: {error}")

    # -------------------------------

    def getAllExercise(self, email, password):
        user = self.getUser(email, password)

        self.cur.execute("SELECT * FROM EXERCISE WHERE USER_ID = %s", (user.get_user_id(),))
        rows = self.cur.fetchall()
        res = ""
        for row in rows:
            res += str(row[1]) + str(row[2]) + str(row[3]) + str(row[4]) + str(row[5]) + str(row[6]) + str(
                row[7]) + str(row[8])
        return res


"""
while (1 > 0):
    frase = input("Digite um comando: entrar | criarLogin | sair : ")
    palavras = frase.split(" ")

    if palavras[0] == "entrar":
        email = input("email: ")
        senha = input("senha: ")
        if hasLogin(email, senha):
            actualId = get_user_id(email, senha)
            user = getUserById(actualId)
            print(f"Bem vindo de volta {user.get_first_name()}")
            cur.execute("SELECT * FROM EXERCISE WHERE USER_ID = %s", (actualId,))
            rows = cur.fetchall()

            clear()
            print(f"Lista de exercicios de {user.getFirstName()}\n")
            for row in rows:
                print(
                    f"Nome: {row[1]}, Grupo: {row[2]}, Parte: {row[3]}, Maquina: {row[4]}, Peso: {row[5]}, Data: {row[6]}, Hora: {row[7]}, Repetições: {row[8]}")
            print("\n")
        else:
            print("Não encontrado!")
    elif palavras[0] == "sair":
        print("Sistema encerrado...")
        break
    elif palavras[0] == "criarLogin":
        print("Digite os dados: \n")
        # dados usuario
        first_name = input("Primeiro nome: ")
        last_name = input("Sobrenome: ")
        date_birth = input("Data de nascimento: ")
        weight = input("Peso: ")
        height = input("Altura: ")
        # dados login
        email = input("Email: ")
        password = input("Senha: ")
        createLogin(first_name, last_name, date_birth, weight, height, email, password)
    else:
        print("comando invalido!")
"""
