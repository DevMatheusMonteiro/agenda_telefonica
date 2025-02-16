from models.endereco import Endereco
from database.database_config import DatabaseConfig
class EnderecoRepository:
    @staticmethod
    def consultar_endereco(id:int):
        comando = "SELECT * FROM enderecos WHERE id = ?"
        try:
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (id,))
            registro = cursor.fetchone()
            if registro:
                endereco = Endereco(id=registro[0], rua=registro[1], numero=registro[2], complemento=registro[3], bairro=registro[4], municipio=registro[5], estado=registro[6], cep=registro[7], contato_id=registro[8])
                return endereco
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()
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
        if rua and rua.strip() != "":
            values.append("rua = ?")
            parametros.append(rua)
        if numero and numero.strip() != "":
            values.append("numero = ?")
            parametros.append(numero)
        values.append("complemento = ?")
        parametros.append(complemento)
        if bairro and bairro.strip() != "":
            values.append("bairro = ?")
            parametros.append(bairro)
        if municipio and municipio.strip() != "":
            values.append("municipio = ?")
            parametros.append(municipio)
        if estado and estado.strip() != "":
            values.append("estado = ?")
            parametros.append(estado)
        if cep and cep.strip() != "":
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
    @staticmethod
    def remover_endereco(id:int):
        comando = "DELETE FROM enderecos WHERE id = ?;"
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