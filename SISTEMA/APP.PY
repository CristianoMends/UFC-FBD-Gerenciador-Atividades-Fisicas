import psycopg2
from Connection import Connection
from User import User

connection = Connection()
conn = connection.getConnection()
cur = conn.cursor()

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
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def getUser(user_id):
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

def createLogin(first_name, last_name, date_birth, weight, height, email, password):
    try:
        cur.execute("""
            INSERT INTO USER_ (FIST_NAME, LAST_NAME, DATE_BIRTH, WEIGHT, HEIGTH)
            VALUES (%s, %s, %s, %s, %s) RETURNING USER_ID;
        """, (first_name, last_name, date_birth, weight, height))
        user_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO LOGIN (EMAIL, PASSWORD, USER_ID)
            VALUES (%s, %s, %s);
        """, (email, password, user_id))

        conn.commit()
        print("Login criado com sucesso.")
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(f"Ocorreu um erro: {error}")

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

def getUserExercises(user_id):
    exercise_list = []
    try:
        cur.execute("SELECT * FROM EXERCISE WHERE USER_ID = %s", (user_id,))
        rows = cur.fetchall()
        for row in rows:
            exercise = Exercise(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            exercise_list.append(exercise)
        return exercise_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None



while(True):
    frase = input("Digite um comando: entrar | criarLogin | sair : ")
    palavras = frase.split(" ")

    if palavras[0] == "entrar":
        email = input("email: ")
        senha = input("senha: ")
        if hasLogin(email, senha):
            actualId = getUserId(email,senha)
            user = getUser(actualId)
            print(f"Bem vindo de volta {user.getFirstName()}")
            cur.execute("SELECT * FROM EXERCISE WHERE USER_ID = %s", (actualId,))
            rows = cur.fetchall()

            clear()
            print(f"Lista de exercicios de {user.getFirstName()}\n")
            for row in rows:
                print(f"Nome: {row[1]}, Grupo: {row[2]}, Parte: {row[3]}, Maquina: {row[4]}, Peso: {row[5]}, Data: {row[6]}, Hora: {row[7]}, Repetições: {row[8]}")
            print("\n")
        else:
            print("Não encontrado!")
    elif palavras[0] == "sair":
        print("Sistema encerrado...")
        break
    elif palavras[0] == "criarLogin":
        print("Digite os dados: \n")
        #dados usuario
        first_name = input("Primeiro nome: ")
        last_name = input("Sobrenome: ")
        date_birth = input("Data de nascimento: ")
        weight = input("Peso: ")
        height = input("Altura: ")
        #dados login
        email = input("Email: ")
        password = input("Senha: ")
        createLogin(first_name, last_name, date_birth, weight, height, email, password)
    else:
        print("comando invalido!")