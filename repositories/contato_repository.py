from database.database_config import DatabaseConfig
from models.contato import Contato
from models.endereco import Endereco
from models.telefone import Telefone
from models.email import Email
class ContatoRepository:
    @staticmethod
    def consultar_contatos():
        comando = """
                SELECT 
                c.id, 
                c.nome, 
                c.data_nascimento, 
                e.rua, 
                e.numero, 
                e.complemento,
                e.bairro, 
                e.municipio, 
                e.estado, 
                e.cep, 
                GROUP_CONCAT(DISTINCT t.telefone) AS telefones, 
                GROUP_CONCAT(DISTINCT em.email) AS emails
                FROM contatos c
                INNER JOIN enderecos e ON c.id = e.contato_id
                LEFT JOIN telefones t ON c.id = t.contato_id
                LEFT JOIN emails em ON c.id = em.contato_id
                GROUP BY c.id;
            """
        contatos = []
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando)
            registros = cursor.fetchall()
            for registro in registros:
                contato = Contato(id=registro[0], nome=registro[1], data_nascimento=registro[2], endereco=Endereco(rua=registro[3], numero=registro[4], complemento=registro[5], bairro=[6], municipio=registro[7], estado=registro[8], cep=registro[9]))
                telefones = registro[10].split(",")
                for telefone in telefones:
                    contato.add_telefone(Telefone(telefone))
                emails = registro[11].split(",")
                for email in emails:
                    contato.add_email(Email(email))
                contatos.append(contato)
            return contatos
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)
    @staticmethod
    def consultar_contato(id: int):
        comando = "SELECT * FROM contatos WHERE id = ?;"
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (id,))
            registro = cursor.fetchone()
            if registro:
                return Contato(registro[0], registro[1], registro[2])
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)
    @staticmethod
    def criar_contato(data: dict):
        nome = data.get("nome")
        data_nascimento = data.get("data_nascimento")
        comando = "INSERT INTO contatos (nome, data_nascimento) VALUES (?, ?) RETURNING id;"
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (nome, data_nascimento))
            id = cursor.fetchone()
            conn.commit()
            return id[0]
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)
    @staticmethod
    def atualizar_contato(data: dict):
        id = data.get("id")
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
    @staticmethod
    def remover_contato(id: int):
        comando = "DELETE FROM contatos WHERE id = ?;"
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (id,))
            conn.commit()
            return id
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)