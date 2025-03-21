import sqlite3
from os import path
class DatabaseConfig:
    conn = None
    @staticmethod
    def conectar():
        BANCO = "database.db"
        BASE_DIR = path.dirname(path.abspath(__file__))
        DIR_BANCO = path.join(BASE_DIR, BANCO)
        try:
            DatabaseConfig.conn = sqlite3.connect(DIR_BANCO)
            DatabaseConfig.conn.execute("PRAGMA foreign_keys = ON;")
        except Exception as e:
            print(e)
    @staticmethod
    def desconectar():
        if DatabaseConfig.conn is not None:
            DatabaseConfig.conn.close()
    @staticmethod
    def create_tables():
        try:
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
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
            DatabaseConfig.conn.commit()
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()