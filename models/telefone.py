class Telefone:
    def __init__(self, id:int=None, telefone:str=None, contato_id:int=None):
        self.__id = id
        self.__telefone = telefone
        self.__contato_id = contato_id
    @property
    def id(self):
        return self.__id
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone:str):
        if telefone != None and telefone.strip() != "":
            self.__telefone = telefone
    @property
    def contato_id(self):
        return self.__contato_id
    def to_dict(self):
        return {"id": self.id, "telefone": self.telefone, "contato_id": self.contato_id}