import sqlite3
from os import path
class DatabaseConfig:
    @staticmethod
    def conectar():
        BANCO = "database.db"
        BASE_DIR = path.dirname(path.abspath(__file__))
        DIR_BANCO = path.join(BASE_DIR, BANCO)
        try:
            conn = sqlite3.connect(DIR_BANCO)
            conn.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print(e)
        return conn
    @staticmethod
    def desconectar(conn):
        if conn is not None:
            conn.close()
    @staticmethod
    def create_tables():
        try:
            conn = DatabaseConfig.conectar()
            if conn is None:
                return print("Erro na conexão com o banco")
            cursor = conn.cursor()
            cursor.executescript(
                """
                    CREATE TABLE IF NOT EXISTS contatos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR(255) NOT NULL,
                        data_nascimento DATE NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS emails(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email VARCHAR(255) NOT NULL,
                        contato_id INTEGER NOT NULL,
                        FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE
                    );
                    CREATE TABLE IF NOT EXISTS telefones(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        telefone VARCHAR(255) NOT NULL,
                        contato_id INTEGER NOT NULL,
                        FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE
                    );
                    CREATE TABLE IF NOT EXISTS enderecos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        rua VARCHAR(255) NOT NULL,
                        numero VARCHAR(255) NOT NULL,
                        complemento VARCHAR(255),
                        bairro VARCHAR(255) NOT NULL,
                        municipio VARCHAR(255) NOT NULL,
                        estado VARCHAR(255) NOT NULL,
                        cep VARCHAR(255) NOT NULL,
                        contato_id INTEGER NOT NULL,
                        FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE
                    );
                """
            )
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)