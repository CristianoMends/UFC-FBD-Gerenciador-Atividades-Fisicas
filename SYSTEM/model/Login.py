import psycopg2

class Login:
    def __init__(self, login_id, email, password, registration_date, user_id):
        self.login_id = login_id
        self.email = email
        self.password = password
        self.user_id = user_id
        self.psycopg = psycopg2

    def get_login_id(self):
        return self.login_id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_user_id(self):
        return self.user_id

    def hasLogin(self, email, senha):
        try:
            self.cur.execute("SELECT * FROM LOGIN WHERE EMAIL = %s AND PASSWORD = %s", (email, senha))
            rows = self.cur.fetchall()
            if len(rows) > 0:
                return True
            else:
                return False
        except (Exception, self.psycopg.DatabaseError) as error:
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
        except (Exception, self.psycopg.DatabaseError) as error:
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
        except (Exception, self.psycopg.DatabaseError) as error:
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
