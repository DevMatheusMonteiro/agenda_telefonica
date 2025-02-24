from models.email import Email
from database.database_config import DatabaseConfig
class EmailRepository:
    @staticmethod
    def consultar_email(id:int):
        comando = "SELECT * FROM emails WHERE id = ?"
        try:
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (id,))
            registro = cursor.fetchone()
            if registro:
                email = Email(id=registro[0], email=registro[1], contato_id=registro[2])
                return email
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()
    def consultar_por_email(data:dict):
        comando = "SELECT * FROM emails WHERE email = ? and contato_id = ?"
        try:
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (data["email"], data["contato_id"]))
            registro = cursor.fetchone()
            if registro:
                email = Email(id=registro[0], email=registro[1], contato_id=registro[2])
                return email
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()
    @staticmethod
    def criar_email(data: dict):
        email = data.get("email")
        contato_id = data.get("contato_id")
        comando = """
                INSERT INTO emails (email, contato_id)
                VALUES (?, ?) RETURNING id;
            """
        try:
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (email, contato_id))
            id = cursor.fetchone()[0]
            return id
        except Exception as e:
            raise Exception(e)
    @staticmethod
    def atualizar_email(data: dict):
        values = []
        parametros = []
        id = data.get("id")
        email = data.get("email")
        if email and email.strip() != "":
            values.append("email = ?")
            parametros.append(email)
        parametros.append(id)
        if values:
            comando = f"UPDATE emails SET {", ".join(values)} WHERE id = ?;"
            try:
                cursor = DatabaseConfig.conn.cursor()
                cursor.execute(comando, tuple(parametros))
                return id
            except Exception as e:
                raise Exception(e)
    @staticmethod
    def remover_email(id:int):
        comando = "DELETE FROM emails WHERE id = ?;"
        try:
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (id,))
            DatabaseConfig.conn.commit()
            return id
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()