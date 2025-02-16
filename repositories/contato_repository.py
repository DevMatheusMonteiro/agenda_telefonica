from database.database_config import DatabaseConfig
from models.contato import Contato
from models.endereco import Endereco
from models.telefone import Telefone
from models.email import Email
from .endereco_repository import EnderecoRepository
from .email_repository import EmailRepository
from .telefone_repository import TelefoneRepository
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
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando)
            registros = cursor.fetchall()
            if registros: 
                for registro in registros:
                    contato = Contato(id=registro[0], nome=registro[1], data_nascimento=registro[2])
                    if registro[3]:
                        endereco = Endereco(id=registro[3], rua=registro[4], numero=registro[5], complemento=registro[6], bairro=registro[7], municipio=registro[8], estado=registro[9], cep=registro[10], contato_id=contato.id)
                        contato.endereco = endereco
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
            DatabaseConfig.desconectar()
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
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(comando, (id,))
            registro = cursor.fetchone()
            if registro and not (len(set(registro)) == 1 and list(set(registro))[0] is None):
                contato = Contato(id=registro[0], nome=registro[1], data_nascimento=registro[2])
                if registro[3]:
                        endereco = Endereco(id=registro[3], rua=registro[4], numero=registro[5], complemento=registro[6], bairro=registro[7], municipio=registro[8], estado=registro[9], cep=registro[10], contato_id=contato.id)
                        contato.endereco = endereco
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
            DatabaseConfig.desconectar()
    @staticmethod
    def criar_contato(data: dict):
        criar_contato = "INSERT INTO contatos (nome, data_nascimento) VALUES (?, ?) RETURNING id;"
        nome = data.get("nome")
        data_nascimento = data.get("data_nascimento")
        endereco = data.get("endereco")
        emails = data.get("emails")
        telefones = data.get("telefones")
        try:
            DatabaseConfig.conectar()
            cursor = DatabaseConfig.conn.cursor()
            cursor.execute(criar_contato, (nome, data_nascimento))
            contato_id = cursor.fetchone()[0]
            endereco_id = None
            emails_id = []
            telefones_id = []
            if endereco:
                endereco["contato_id"] = contato_id
                endereco_id = EnderecoRepository.criar_endereco(endereco)
            if emails:
                for email in emails:
                    email["contato_id"] = contato_id
                    email_id = EmailRepository.criar_email(email)
                    emails_id.append(email_id)
            if telefones:
                for telefone in telefones:
                    telefone["contato_id"] = contato_id
                    telefone_id = TelefoneRepository.criar_telefone(telefone)
                    telefones_id.append(telefone_id)
            DatabaseConfig.conn.commit()
            return (contato_id, endereco_id, emails_id, telefones_id)
        except Exception as e:
            print(e)
        finally:
            DatabaseConfig.desconectar()
    @staticmethod
    def atualizar_contato(data: dict):
        id = data.get("id")
        values = []
        parametros = []
        nome = data.get("nome")
        data_nascimento = data.get("data_nascimento")
        endereco = data.get("endereco")
        endereco_id = None
        emails = data.get("emails")
        emails_id = []
        telefones = data.get("telefones")
        telefones_id = []
        if nome and nome.strip() != "":
            values.append("nome = ?")
            parametros.append(nome)
        if data_nascimento and data_nascimento.strip() != "":
            values.append("data_nascimento = ?")
            parametros.append(data_nascimento)
        parametros.append(id)
        if values:
            comando = f"UPDATE contatos SET {", ".join(values)} WHERE id = ?;"
            try:
                DatabaseConfig.conectar()
                cursor = DatabaseConfig.conn.cursor()
                cursor.execute(comando, tuple(parametros))
                if endereco:
                    endereco_id = EnderecoRepository.atualizar_endereco(endereco)
                if emails:
                    for email in emails:
                        email_id = EmailRepository.atualizar_email(email)
                        emails_id.append(email_id)
                if telefones:
                    for telefone in telefones:
                        telefone_id = TelefoneRepository.atualizar_telefone(telefone)
                        telefones_id.append(telefone_id)
                DatabaseConfig.conn.commit()
                return (id, endereco_id, emails_id, telefones_id)
            except Exception as e:
                print(e)
            finally:
                DatabaseConfig.desconectar()
    @staticmethod
    def remover_contato(id: int):
        comando = "DELETE FROM contatos WHERE id = ?;"
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