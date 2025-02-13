from database.database_config import DatabaseConfig
class EmailRepository:
    @staticmethod
    def criar_email(data: dict):
        email = data.get("email")
        contato_id = data.get("contato_id")
        comando = """
                INSERT INTO emails (email, contato_id)
                VALUES (?, ?) RETURNING id;
            """
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (email, contato_id))
            id = cursor.fetchone()[0]
            conn.commit()
            return id
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)