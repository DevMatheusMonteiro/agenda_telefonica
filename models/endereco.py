class Endereco:
    __id:int=None
    __rua:str=None
    __numero:str=None
    __complemento:str=None
    __bairro:str=None
    __municipio:str=None
    __estado:str=None
    __cep:str=None
    __contato_id:int=None
    def __init__(self, id:int=None, rua:str=None, numero:str=None, complemento:str=None, bairro:str=None, municipio:str=None, estado:str=None, cep:str=None, contato_id:int=None):
        self.validar_endereco(id=id, rua=rua, numero=numero, complemento=complemento, bairro=bairro, municipio=municipio, estado=estado, cep=cep, contato_id=contato_id)
    def validar_endereco(self, id:int, rua:str, numero:str, complemento:str, bairro:str, municipio:str, estado:str, cep:str, contato_id:int):
        self.id = id
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep
        self.contato_id = contato_id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id:int):
        self.__id = id
    @property
    def rua(self):
        return self.__rua
    @rua.setter
    def rua(self, rua:str):
        if isinstance(rua, str) and rua.strip() != "":
            self.__rua = rua
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero:str):
        if isinstance(numero, str) and numero.strip() != "":
            self.__numero = numero
    @property
    def complemento(self):
        return self.__complemento
    @complemento.setter
    def complemento(self, complemento:str):
        self.__complemento = complemento
    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, bairro:str):
        if isinstance(bairro, str) and bairro.strip() != "":
            self.__bairro = bairro
    @property
    def municipio(self):
        return self.__municipio
    @municipio.setter
    def municipio(self, municipio:str):
        if isinstance(municipio, str) and municipio.strip() != "":
            self.__municipio = municipio
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado:str):
        if isinstance(estado, str) and estado.strip() != "":
            self.__estado = estado
    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, cep:str):
        if isinstance(cep, str) and cep.strip() != "":
            self.__cep = cep
    @property
    def contato_id(self):
        return self.__contato_id
    @contato_id.setter
    def contato_id(self, contato_id:str):
        self.__contato_id = contato_id
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