import psycopg2
from psycopg2 import OperationalError
class Connection:
    def __init__(self):
        self.user = "postgres"
        self.dbname = "registro_academia"
        self.password = "cristiano1234"
        self.host = "localhost"
        self.port = "5432"
        self.conn = None

    def getConnection(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                options="-c statement_timeout=10000",
                connect_timeout=10
            )
            return self.conn
        except (Exception, psycopg2.DatabaseError, OperationalError) as error:
            print(error)
