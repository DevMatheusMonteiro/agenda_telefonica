class Endereco:
    def __init__(self, id:int=None, rua:str=None, numero:str=None, complemento:str=None, bairro:str=None, municipio:str=None, estado:str=None, cep:str=None, contato_id:int=None):
        self.__id = id
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__municipio = municipio
        self.__estado = estado
        self.__cep = cep
        self.__contato_id = contato_id
    @property
    def id(self):
        return self.__id
    @property
    def rua(self):
        return self.__rua
    @rua.setter
    def rua(self, rua:str):
        if rua != None and rua.strip() != "":
            self.__rua = rua
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero:str):
        if numero != None and numero.strip() != "":
            self.__numero = numero
    @property
    def complemento(self):
        return self.__complemento
    @complemento.setter
    def complemento(self, complemento:str):
        if complemento != None and complemento.strip() != "":
            self.__complemento = complemento
    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, bairro:str):
        if bairro != None and bairro.strip() != "":
            self.__bairro = bairro
    @property
    def municipio(self):
        return self.__municipio
    @municipio.setter
    def municipio(self, municipio:str):
        if municipio != None and municipio.strip() != "":
            self.__municipio = municipio
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado:str):
        if estado != None and estado.strip() != "":
            self.__estado = estado
    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, cep:str):
        if cep != None and cep.strip() != "":
            self.__cep = cep
    @property
    def contato_id(self):
        return self.__contato_id
    def to_dict(self):
        return {
            "id": self.id,
            "rua": self.rua,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "municipio": self.municipio,
            "estado": self.estado,
            "cep": self.cep,
            "contato_id": self.contato_id
        }