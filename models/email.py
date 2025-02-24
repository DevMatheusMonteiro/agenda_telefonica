class Email:
    __id:int=None
    __email:str=None
    __contato_id:int=None
    def __init__(self, id:int=None, email:str=None, contato_id:int=None):
        self.validar_email(id=id, email=email, contato_id=contato_id)
    def validar_email(self, id:int, email:str, contato_id:int):
        self.id = id
        self.email = email
        self.contato_id = contato_id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id:int):
        self.__id = id
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email:str):
        if isinstance(email, str) and email.strip() != "":
            self.__email = email
    @property
    def contato_id(self):
        return self.__contato_id
    @contato_id.setter
    def contato_id(self, contato_id:int):
        self.__contato_id = contato_id
    def to_dict(self):
        return {"id": self.id, "email": self.email, "contato_id": self.contato_id}