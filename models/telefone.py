class Telefone:
    def __init__(self, telefone:str=None):
        self.__telefone = telefone
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone:str):
        if telefone != None and telefone.strip() != "":
            self.__telefone = telefone