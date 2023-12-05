import psycopg2
from dao.Connection import Connection
from model.entidades import Usuario
class Consulta:
    def __init__(self):
        self.connection = Connection()

    def cadastrar_usuario(self, nome, sobrenome, usuario, senha, nascimento, peso, altura):
        conn = None
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO usuario (nome, sobrenome, data_nascimento, peso, altura)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nome, sobrenome, nascimento, peso, altura))

            cursor.execute("SELECT lastval()")
            usuario_id = cursor.fetchone()[0]

            cursor.execute('''
                INSERT INTO login (usuario_id, usuario, senha)
                VALUES (%s, %s, %s)
            ''', (usuario_id, usuario, senha))

            conn.commit()
            return True
        except psycopg2.IntegrityError:
            return False
        finally:
            if conn:
                conn.close()

    def verificar_login(self, usuario, senha):
        global conn
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM usuario
                inner join login
                on login.usuario_id = usuario.usuario_id
                WHERE login.usuario = %s AND login.senha = %s
            ''', (usuario, senha))

            result = cursor.fetchone()

            if result:
                return Usuario(result[1], result[2], str(result[3]), result[6], result[7])
            else:
                return None
        finally:
            if conn:
                conn.close()

