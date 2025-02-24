class Telefone:
    __id:int=None
    __telefone:int=None
    __contato_id:int=None
    def __init__(self, id:int=None, telefone:str=None, contato_id:int=None):
        self.validar_telefone(id=id, telefone=telefone, contato_id=contato_id)
    def validar_telefone(self, id:int, telefone:str, contato_id:int):
        self.id = id
        self.telefone = telefone
        self.contato_id = contato_id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id:int):
        self.__id = id
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
    @contato_id.setter
    def contato_id(self, contato_id:int):
        self.__contato_id = contato_id
    def to_dict(self):
        return {"id": self.id, "telefone": self.telefone, "contato_id": self.contato_id}