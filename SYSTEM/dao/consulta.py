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

    def obterListaEquipamentos(self):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                cursor.execute('''
                    SELECT DISTINCT equipamento FROM exercicio
                ''')

                resultados = cursor.fetchall()

                equipamentos = [resultado[0] for resultado in resultados]

                return equipamentos
        except psycopg2.Error as e:
            print(f"Erro no banco de dados: {e}")
            return None

    def obterTopSessoes(self):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                # Consulta SQL para obter o top 3 usuários com mais sessões no mês atual
                cursor.execute('''
                    SELECT
                        U.NOME,
                        COUNT(E.EXERCICIO_ID) AS NUMERO_SESSOES
                    FROM
                        USUARIO U
                    JOIN
                        EXERCICIO E ON U.USUARIO_ID = E.USER_ID
                    WHERE
                        EXTRACT(MONTH FROM E.DATE) = EXTRACT(MONTH FROM CURRENT_DATE)
                    GROUP BY
                        U.USUARIO_ID, U.NOME, U.SOBRENOME
                    ORDER BY
                        NUMERO_SESSOES DESC
                    LIMIT 3;
                ''')

                # Obter todos os resultados
                resultados = cursor.fetchall()

                # Retornar os resultados como uma lista de tuplas (nome, numero_sessoes)
                return resultados
        except psycopg2.Error as e:
            # Tratar erros de banco de dados
            print(f"Erro no banco de dados: {e}")
            return None

    def obterTopPesoUtilizado(self):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                # Consulta SQL para obter o Top 3 Usuários com Maior Peso Utilizado no Mês Atual:
                cursor.execute('''
                    
                        SELECT
                            U.NOME,
                            E.NOME AS NOME_EXERCICIO,
                            MAX(E.WEIGHT_USED) AS MAIOR_PESO_UTILIZADO
                        FROM
                            USUARIO U
                        JOIN
                            EXERCICIO E ON U.USUARIO_ID = E.USER_ID
                        WHERE
                            EXTRACT(MONTH FROM E.DATE) = EXTRACT(MONTH FROM CURRENT_DATE)
                        GROUP BY
                            U.USUARIO_ID, U.NOME, U.SOBRENOME
                        ORDER BY
                            MAIOR_PESO_UTILIZADO DESC
                        LIMIT 3;

                ''')

                # Obter todos os resultados
                resultados = cursor.fetchall()

                # Retornar os resultados como uma lista de tuplas (nome, NOME_EXERCICIO)
                return resultados
        except psycopg2.Error as e:
            # Tratar erros de banco de dados
            print(f"Erro no banco de dados: {e}")
            return None

    def obterTopQtdHoras(self):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                # Consulta SQL para obter o Top 3 usuarios com maior quantidades de horas registradas
                cursor.execute('''
                            SELECT
                                U.NOME,
                                SUM(E.DURATION) AS TEMPO_TOTAL_EXERCICIOS
                            FROM
                                USUARIO U
                            JOIN
                                EXERCICIO E ON U.USUARIO_ID = E.USER_ID
                            WHERE
                                EXTRACT(MONTH FROM E.DATE) = EXTRACT(MONTH FROM CURRENT_DATE)
                            GROUP BY
                                U.USUARIO_ID, U.NOME, U.SOBRENOME
                            ORDER BY
                                TEMPO_TOTAL_EXERCICIOS DESC
                            LIMIT 3;

                ''')

                # Obter todos os resultados
                resultados = cursor.fetchall()

                # Retornar os resultados como uma lista de tuplas (nome, TEMPO_TOTAL_EXERCICIOS)
                return resultados
        except psycopg2.Error as e:
            # Tratar erros de banco de dados
            print(f"Erro no banco de dados: {e}")
            return None

    def getMaiorPesoUsuario(self):
        pass

