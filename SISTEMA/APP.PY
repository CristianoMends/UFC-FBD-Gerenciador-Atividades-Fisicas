import psycopg2
from Connection import Connection
from User import User

connection = Connection()
cur = connection.getCursor()

def hasLogin(email, senha):
    try:
        cur.execute("SELECT * FROM LOGIN WHERE EMAIL = %s AND PASSWORD = %s", (email, senha))
        rows = cur.fetchall()
        if len(rows) > 0:
            return True
        else:
            return False
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_user_data(user_id, cur):
    try:
        cur.execute("SELECT * FROM USER_ WHERE USER_ID = %s", (user_id,))
        user_data = cur.fetchone()
        if user_data:
            return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
        else:
            return None
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def criarLogin():


def getUserId(email, senha):
    try:
        cur.execute("SELECT USER_ID FROM LOGIN WHERE EMAIL = %s AND PASSWORD = %s", (email, senha))
        row = cur.fetchone()
        if row is not None:
            return row[0]  # Retorna o ID do usuário se o login for bem-sucedido
        else:
            return None  # Retorna None se o login falhar
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


while(True):
    frase = input("Digite um comando: entrar | criarLogin | sair : ")
    palavras = frase.split(" ")

    if palavras[0] == "entrar":
        email = input("email: ")
        senha = input("senha: ")
        if hasLogin(email, senha):
            user = get_user_data(getUserId(email,senha))
            print(f"Bem vindo de volta")

        else:
            print("Não encontrado!")
    elif palavras[0] == "sair":
        print("Sistema encerrado...")
        break
    elif palavras[0] == "criarLogin":

    else:
        print("comando invalido!")