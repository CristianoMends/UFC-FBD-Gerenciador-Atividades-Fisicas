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

    def atualizar_usuario(self, usuario_id, nome, sobrenome, usuario, senha, nascimento, peso, altura):
        conn = None
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                UPDATE usuario
                SET nome = %s, sobrenome = %s, data_nascimento = %s, peso = %s, altura = %s
                WHERE usuario_id = %s
            ''', (nome, sobrenome, nascimento, peso, altura, usuario_id))

            cursor.execute('''
                UPDATE login
                SET usuario = %s, senha = %s
                WHERE usuario_id = %s
            ''', (usuario, senha, usuario_id))

            conn.commit()
            return True
        except psycopg2.Error as e:
            return False
        finally:
            if conn:
                conn.close()

    def verificar_login(self, usuario, senha):
        conn = None
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT * FROM usuario
                INNER JOIN login
                ON login.usuario_id = usuario.usuario_id
                WHERE login.usuario = %s AND login.senha = %s
            ''', (usuario, senha))

            result = cursor.fetchone()

            if result:
                usuario_instance = Usuario(result[0], result[1], result[2], str(result[3]), result[4], result[5])
                return usuario_instance
            else:
                return None
        finally:
            if conn:
                conn.close()

    def getListaEquipamentos(self):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                cursor.execute('''
                    SELECT DISTINCT equipamento FROM exercicio
                ''')

                resultados = cursor.fetchall()

                equipamentos = [resultado[0] for resultado in resultados]

                return equipamentos
        except psycopg2.Error as e:
            return None

    def obterTopSessoes(self):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                cursor.execute('''
                    SELECT u.nome, COUNT(e.exercicio_id) AS total_exercicios
                    FROM usuario u
                    LEFT JOIN exercicio e ON u.usuario_id = e.usuario_id
                    GROUP BY u.nome
                    ORDER BY total_exercicios DESC
                    limit 3;
                ''')

                resultados = cursor.fetchall()

                return resultados
        except psycopg2.Error as e:
            print(f"Erro no banco de dados: {e}")
            return None

    def obterTopPesoUtilizado(self,eq:str):
        try:
            with self.connection.getConnection() as conn, conn.cursor() as cursor:
                cursor.execute(f'''
                    select distinct u.nome,e.peso_utilizado
                    from exercicio e
                    inner join usuario u on u.usuario_id = e.usuario_id
                    where e.equipamento = '{eq}'
                    order by e.peso_utilizado desc
                    limit 3

                ''')

                resultados = cursor.fetchall()

                return resultados
        except psycopg2.Error as e:
            print(f"Erro no banco de dados: {e}")
            return None



    def getMaiorPesoUsuario(self, usuario_id):
        conn = None
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT MAX(peso_utilizado) FROM exercicio
                WHERE usuario_id = %s
            ''', (usuario_id,))

            resultado = cursor.fetchone()

            if resultado and resultado[0] is not None:
                return resultado[0]
            else:
                return None
        finally:
            if conn:
                conn.close()

    def getEqMaisUtilizado(self, usuario_id):
        conn = None
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT EQUIPAMENTO
                FROM EXERCICIO
                WHERE EQUIPAMENTO IS NOT NULL AND USUARIO_ID = %s
                GROUP BY EQUIPAMENTO
                ORDER BY COUNT(EQUIPAMENTO) DESC
                LIMIT 1
            ''', (usuario_id,))

            result = cursor.fetchone()

            if result:
                return result[0]  # Retorna o nome do equipamento mais utilizado
            else:
                return None  # Retorna None se não houver dados

        finally:
            if conn:
                conn.close()

    def getExerciciosUsuario(self, usuario_id):
        conn = None
        try:
            conn = self.connection.getConnection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT NOME, GRUPO_MUSCULAR, PARTE_MUSCULAR, EQUIPAMENTO, PESO_UTILIZADO, DATA, HORA, REPETICOES
                FROM EXERCICIO
                WHERE USUARIO_ID = %s
            ''', (usuario_id,))

            results = cursor.fetchall()

            exercicios = []
            for result in results:
                exercicio = {
                    'nome': result[0],
                    'grupo_muscular': result[1],
                    'parte_muscular': result[2],
                    'equipamento': result[3],
                    'peso_utilizado': result[4],
                    'data': result[5],
                    'hora': result[6],
                    'repeticoes': result[7],
                }
                exercicios.append(exercicio)

            return exercicios

        finally:
            if conn:
                conn.close()

    def cadastrar_exercicio(self, usuario_id, nome, grupo_muscular, parte_muscular, equipamento, peso_utilizado, data,
                            hora, repeticoes):
        self.conn = None
        try:
            self.conn = self.connection.getConnection()
            self.cursor = self.conn.cursor()
            sql = '''
                INSERT INTO exercicio (usuario_id, nome, grupo_muscular, parte_muscular, equipamento, peso_utilizado, data, hora, repeticoes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            self.cursor.execute(sql, (
            usuario_id, nome, grupo_muscular, parte_muscular, equipamento, peso_utilizado, data, hora, repeticoes))

            self.conn.commit()

            self.cursor.close()
            self.conn.close()

            return True

        except Exception as e:
            return False


