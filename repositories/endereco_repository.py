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
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (rua, numero, complemento, bairro, municipio, estado, cep, contato_id))
            id = cursor.fetchone()[0]
            conn.commit()
            return id
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)