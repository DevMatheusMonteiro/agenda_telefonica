from database.database_config import DatabaseConfig
from models.contato import Contato
class ContatoRepository:
    @staticmethod
    def consultar_contatos():
        comando = "SELECT * FROM contato;"
        contatos = []
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando)
            registros = cursor.fetchall()
            for registro in registros:
                registro = Contato(id=registro[0], nome=registro[1], data_nascimento=registro[2])
                contatos.append(registro)
            return contatos
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)
    @staticmethod
    def consultar_contato(id):
        comando = "SELECT * FROM contato WHERE id = ?;"
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (id,))
            registro = cursor.fetchone()
            if registro:
                return Contato(registro[0], registro[1], registro[2])
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)