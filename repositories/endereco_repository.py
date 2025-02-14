from database.database_config import DatabaseConfig
class EnderecoRepository:
    @staticmethod
    def criar_endereco(data:dict):
        rua = data.get("rua")
        numero = data.get("numero")
        complemento = data.get("complemento")
        bairro = data.get("bairro")
        municipio = data.get("municipio")
        estado = data.get("estado")
        cep = data.get("cep")
        contato_id = data.get("contato_id")
        comando = """
                INSERT INTO enderecos (rua, numero, complemento, bairro, municipio, estado, cep, contato_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?) RETURNING id;
            """
        try:
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (rua, numero, complemento, bairro, municipio, estado, cep, contato_id))
            id = cursor.fetchone()[0]
            return id
        except Exception as e:
            raise Exception(e)
    @staticmethod
    def atualizar_endereco(data: dict):
        id = data.get("contact_id")
        values = []
        parametros = []
        nome = data.get("nome")
        data_nascimento = data.get("data_nascimento")
        if nome:
            values.append("nome = ?")
            parametros.append(nome)
        if data_nascimento:
            values.append("data_nascimento = ?")
            parametros.append(data_nascimento)
        parametros.append(id)
        if values:
            comando = f"UPDATE contatos SET {", ".join(values)} WHERE id = ?;"
            try:
                conn = DatabaseConfig.conectar()
                cursor = conn.cursor()
                cursor.execute(comando, tuple(parametros))
                conn.commit()
                return id
            except Exception as e:
                print(e)
            finally:
                DatabaseConfig.desconectar(conn)