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
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (email, contato_id))
            id = cursor.fetchone()[0]
            return id
        except Exception as e:
            raise Exception(e)
        