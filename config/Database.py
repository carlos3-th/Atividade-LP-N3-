import psycopg2


class Database:

    def __init__(self):
        self.bd = None

    def conectar(self):
        self.bd = psycopg2.connect(host="localhost", database="TrabalhoLP", user="postgres", password="postgres")
        print("Conexão Realizada com Sucesso")
        return self.bd

    def desconectar(self):
        self.bd.close()