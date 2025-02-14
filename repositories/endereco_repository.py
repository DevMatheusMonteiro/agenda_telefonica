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
        values = []
        parametros = []
        id = data.get("id")
        rua = data.get("rua")
        numero = data.get("numero")
        complemento = data.get("complemento")
        bairro = data.get("bairro")
        municipio = data.get("municipio")
        estado = data.get("estado")
        cep = data.get("cep")
        if rua:
            values.append("rua = ?")
            parametros.append(rua)
        if numero:
            values.append("numero = ?")
            parametros.append(numero)
        if complemento:
            values.append("complemento = ?")
            parametros.append(complemento)
        if bairro:
            values.append("bairro = ?")
            parametros.append(bairro)
        if municipio:
            values.append("municipio = ?")
            parametros.append(municipio)
        if estado:
            values.append("estado = ?")
            parametros.append(estado)
        if cep:
            values.append("cep = ?")
            parametros.append(cep)
        parametros.append(id)
        if values:
            comando = f"UPDATE enderecos SET {", ".join(values)} WHERE id = ?;"
            try:
                cursor = DatabaseConfig.conn.cursor()
                cursor.execute(comando, tuple(parametros))
                return id
            except Exception as e:
                raise Exception(e)