from datetime import datetime
from .endereco import Endereco
from .telefone import Telefone
from .email import Email
class Contato:
    __id:int=None
    __nome:str=None
    __data_nascimento:datetime=None
    __endereco:Endereco=None
    __telefones = []
    __emails = []
    def __init__(self, id:int=None, nome:str=None, data_nascimento:datetime|str=None, endereco:Endereco=None):
        self.validar_contato(id=id,nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    def validar_contato(self, id:int, nome:str, data_nascimento:datetime|str, endereco:Endereco):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id:int):
        self.__id = id
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome:str):
        if (isinstance(nome, str) and nome.strip() != ""):
            self.__nome = nome
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento:datetime|str):
        if isinstance(data_nascimento, datetime) or (isinstance(data_nascimento, str) and self.__validar_data_nascimento(data_nascimento)):
            self.__data_nascimento = data_nascimento
    def __validar_data_nascimento(self, data_nascimento:datetime):
        try:
            datetime.strptime(data_nascimento, "%Y-%m-%d")
            return True
        except:
            return False
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
    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "data_nascimento": self.data_nascimento, "endereco": self.endereco.to_dict() if self.endereco is not None else self.endereco, "telefones": [telefone.to_dict() for telefone in self.telefones], "emails": [email.to_dict() for email in self.emails]}