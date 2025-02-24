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
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (rua, numero, complemento, bairro, municipio, estado, cep, contato_id))
            id = cursor.fetchone()[0]
            DatabaseConfig.conn.commit()
            return id
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()
    @staticmethod
    def atualizar_endereco(data: dict):
        values = []
        parametros = []
        id = data.get("id")
        del data["id"]
        if data.get("contato_id"): del data["contato_id"]
        for key, value in data.items():
            if ((key == "complemento"
                and (value is None or (isinstance(value, str) and value.strip() != "")))
                or (isinstance(value, str) and value.strip() != "")):
                values.append(f"{key} = ?")
                parametros.append(value)
        parametros.append(id)
        if values:
            DatabaseConfig.conectar()
            comando = f"UPDATE enderecos SET {", ".join(values)} WHERE id = ?;"
            try:
                cursor = DatabaseConfig.conn.cursor()
                cursor.execute(comando, tuple(parametros))
                DatabaseConfig.conn.commit()
                return id
            except Exception as e:
                print(e)
            finally:
                DatabaseConfig.desconectar()
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