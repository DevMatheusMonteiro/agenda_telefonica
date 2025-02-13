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
                e.id as endereco_id,
                e.rua, 
                e.numero, 
                e.complemento,
                e.bairro, 
                e.municipio, 
                e.estado, 
                e.cep,
                GROUP_CONCAT(DISTINCT t.id) as telefones_id,
                GROUP_CONCAT(DISTINCT t.telefone) AS telefones, 
                GROUP_CONCAT(DISTINCT em.id) as emails_id,
                GROUP_CONCAT(DISTINCT em.email) AS emails
                FROM contatos c
                LEFT JOIN enderecos e ON c.id = e.contato_id
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
            print(registros)
            if registros: 
                for registro in registros:
                    contato = Contato(id=registro[0], nome=registro[1], data_nascimento=registro[2], endereco=Endereco(id=registro[3], rua=registro[4], numero=registro[5], complemento=registro[6], bairro=registro[7], municipio=registro[8], estado=registro[9], cep=registro[10]))
                    if registro[11] is not None and registro[12] is not None:
                        ids = registro[11].split(",")
                        telefones = registro[12].split(",")
                        for i in range(len(ids)):
                            contato.add_telefone(Telefone(id=ids[i], telefone=telefones[i], contato_id=contato.id))
                    if registro[13] is not None and registro[14] is not None:
                        ids = registro[13].split(",")
                        emails = registro[14].split(",")
                        for i in range(len(ids)):
                            contato.add_email(Email(id=ids[i], email=emails[i], contato_id=contato.id))
                    contatos.append(contato)
            return contatos
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar(conn)
    @staticmethod
    def consultar_contato(id: int):
        comando = """
            SELECT 
                c.id, 
                c.nome, 
                c.data_nascimento, 
                e.id as endereco_id,
                e.rua, 
                e.numero, 
                e.complemento,
                e.bairro, 
                e.municipio, 
                e.estado, 
                e.cep,
                GROUP_CONCAT(DISTINCT t.id) as telefones_id,
                GROUP_CONCAT(DISTINCT t.telefone) AS telefones, 
                GROUP_CONCAT(DISTINCT em.id) as emails_id,
                GROUP_CONCAT(DISTINCT em.email) AS emails
                FROM contatos c
                LEFT JOIN enderecos e ON c.id = e.contato_id
                LEFT JOIN telefones t ON c.id = t.contato_id
                LEFT JOIN emails em ON c.id = em.contato_id
                WHERE c.id = ?;
            """
        try:
            conn = DatabaseConfig.conectar()
            cursor = conn.cursor()
            cursor.execute(comando, (id,))
            registro = cursor.fetchone()
            if registro and not (len(set(registro)) == 1 and list(set(registro))[0] is None):
                contato = Contato(id=registro[0], nome=registro[1], data_nascimento=registro[2], endereco=Endereco(id=registro[3], rua=registro[4], numero=registro[5], complemento=registro[6], bairro=registro[7], municipio=registro[8], estado=registro[9], cep=registro[10]))
                if registro[11] is not None and registro[12] is not None:
                    ids = registro[11].split(",")
                    telefones = registro[12].split(",")
                    for i in range(len(ids)):
                        contato.add_telefone(Telefone(id=ids[i], telefone=telefones[i], contato_id=contato.id))
                if registro[13] is not None and registro[14] is not None:
                    ids = registro[13].split(",")
                    emails = registro[14].split(",")
                    for i in range(len(ids)):
                        contato.add_email(Email(id=ids[i], email=emails[i], contato_id=contato.id))
                return contato
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