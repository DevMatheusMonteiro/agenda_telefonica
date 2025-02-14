from database.database_config import DatabaseConfig
class TelefoneRepository:
    @staticmethod
    def criar_telefone(data: dict):
        telefone = data.get("telefone")
        contato_id = data.get("contato_id")
        comando = """
                INSERT INTO telefones (telefone, contato_id)
                VALUES (?, ?) RETURNING id;
            """
        try:
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (telefone, contato_id))
            id = cursor.fetchone()[0]
            return id
        except Exception as e:
            raise Exception(e)
    @staticmethod
    def atualizar_telefone(data: dict):
        values = []
        parametros = []
        id = data.get("id")
        telefone = data.get("telefone")
        if telefone and telefone.strip() != "":
            values.append("telefone = ?")
            parametros.append(telefone)
        parametros.append(id)
        if values:
            comando = f"UPDATE telefones SET {", ".join(values)} WHERE id = ?;"
            try:
                cursor = DatabaseConfig.conn.cursor()
                cursor.execute(comando, tuple(parametros))
                return id
            except Exception as e:
                raise Exception(e)