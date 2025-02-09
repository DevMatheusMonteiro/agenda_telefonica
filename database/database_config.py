import sqlite3
from os import path
BANCO = "database.db"
BASE_DIR = path.dirname(path.abspath(__file__))
DIR_BANCO = path.join(BASE_DIR, BANCO)
def verificar_db():
    if not path.exists(DIR_BANCO):
        print("Erro: banco não existe")
        exit()
def conectar():
    conn = None
    try:
        conn = sqlite3.connect(DIR_BANCO)
    except Exception as e:
        print(e)
    return conn
def desconectar(conn):
    if conn is not None:
        conn.close()