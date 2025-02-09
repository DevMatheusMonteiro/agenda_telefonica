from datetime import date
from .endereco import Endereco
from .telefone import Telefone
from .email import Email
class Contato:
    def __init__(self, id:int=None, nome:str=None, data_nascimento:date=None, endereco:Endereco=None):
        self.__id = id
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
        self.__telefones = []
        self.__emails = []
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome:str):
        if nome != None or nome.strip() != "":
            self.__nome = nome
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento:date):
        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco:Endereco):
        if isinstance(endereco, Endereco):
            self.__endereco = endereco
    @property
    def telefones(self):
        return self.__telefones
    def add_telefone(self, telefone:Telefone):
        if isinstance(telefone, Telefone):
            self.__telefones.append(telefone)
    @property
    def emails(self):
        return self.__emails
    def add_email(self, email:Email):
        if isinstance(email, Email):
            self.__emails.append(email)