from repositories.contato_repository import ContatoRepository
from services.contato_service import ContatoService
from repositories.endereco_repository import EnderecoRepository
from repositories.email_repository import EmailRepository
from repositories.telefone_repository import TelefoneRepository
from models.contato import Contato
from database.database_config import DatabaseConfig
# DatabaseConfig.create_tables()
create_contact = {'nome': 'Patrícia Carvalho', 'data_nascimento': '1987-01-28', 'endereco': {'rua': 'Rua 7 de Setembro', 'numero': '789', 'complemento': None, 'bairro': 'Boa Viagem', 'municipio': 'Recife', 'estado': 'PE', 'cep': '51020-320'}, 'telefones': [{'telefone': 'TESTE 31922223333 TESTE'}, {'telefone': '31922224444 TESTE TESTE'}], 'emails': [{'email': 'patricia@email.com'}]}
# create_contact = {'id': 12, 'nome': 'Patrícia Carvalho', 'data_nascimento': '1987-01-28', 'endereco': {'id': 12, 'rua': 'Rua 7 de Setembro', 'numero': '789', 'complemento': None, 'bairro': 'Boa Viagem', 'municipio': 'Recife', 'estado': 'PE', 'cep': '51020-320'}, 'telefones': [{'id': '1002', 'telefone': 'TESTE 31922223333 TESTE', 'contato_id': 12}, {'id': '25', 'telefone': '31922224444 TESTE TESTE', 'contato_id': 12}], 'emails': [{'id': '12', 'email': 'patricia@email.com', 'contato_id': 12}]}
# print(ContatoService.consultar_contatos())
# print(ContatoService.consultar_contato(1))

ContatoService.criar_contato(create_contact)
contato = Contato(nome="") 
