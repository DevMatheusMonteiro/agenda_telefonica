class Email:
    def __init__(self, id:int=None, email:str=None, contato_id:int=None):
        self.__id = id
        self.__email = email
        self.__contato_id = contato_id
    @property
    def id(self):
        return self.__id
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email:str):
        if email != None and email.strip() != "":
            self.__email = email
    @property
    def contato_id(self):
        return self.__contato_id
    def to_dict(self):
        return {"id": self.id, "email": self.email, "contato_id": self.contato_id}