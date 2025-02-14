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