from datetime import date
from .endereco import Endereco
from .telefone import Telefone
from .email import Email
class Contato:
    __id:int=None
    __nome:str=""
    __endereco:str=None
    __telefones = []
    __emails = []
    def __init__(self, id:int=None, nome:str=None, data_nascimento:date=None, endereco:Endereco=None):
        # self.__nome = nome
        self.__id = id
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
        self.__telefones = []
        self.__emails = []
        self.validar_contato(nome=nome)
        
    @property
    def id(self):
        return self.__id
    @property
    def nome(self):
        return self.__nome
    
    def validar_contato(self, nome):
        self.nome = nome
        
    @nome.setter
    def nome(self, nome:str):
        if nome is None or (isinstance(nome, str) and nome.strip() == ""):
            print("Campo nome inválido.")
        self.__nome = nome
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento:date|str):
        if not isinstance(data_nascimento, date) or (isinstance(data_nascimento, str) and data_nascimento.strip() == ""):
            return "Campo data_nascimento inválido."
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
    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "data_nascimento": self.data_nascimento, "endereco": self.endereco.to_dict() if self.endereco is not None else self.endereco, "telefones": [telefone.to_dict() for telefone in self.telefones], "emails": [email.to_dict() for email in self.emails]}