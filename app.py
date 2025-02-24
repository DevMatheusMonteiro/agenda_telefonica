from repositories.contato_repository import ContatoRepository
from services.contato_service import ContatoService
from services.endereco_service import EnderecoService
from repositories.endereco_repository import EnderecoRepository
from repositories.email_repository import EmailRepository
from repositories.telefone_repository import TelefoneRepository
from models.contato import Contato
from models.endereco import Endereco
from database.database_config import DatabaseConfig
from datetime import datetime
# DatabaseConfig.create_tables()
create_contact = {'id': 2, 'nome': 'Roberta Souza', 'data_nascimento': '1992-03-22', 'endereco': {'id': 2, 'rua': 'Av. Paulista', 'numero': "40", 'complemento': "casa 77", 'bairro': 'BARRA', 'municipio': 'São Paulo', 'estado': 'RJ', 'cep': '01511-200', 'contato_id': 2}, 'telefones': [{'id': '2', 'telefone': '21988887777', 'contato_id': 2}, {'id': '16', 'telefone': '21988889999', 'contato_id': 2}], 'emails': [{'id': '2', 'email': 'ana.souza@email.com', 'contato_id': 2}, {'id': '16', 'email': 'ana_trabalho@email.com', 'contato_id': 2}]}
EnderecoService.criar_endereco(create_contact["endereco"])