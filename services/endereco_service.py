from repositories.endereco_repository import EnderecoRepository
class EnderecoService:
    @staticmethod
    def criar_endereco(data:dict):
        for key, value in data.items():
            if key != "id" and key != "contato_id":
                if ((key == "complemento"
                    and (value is not None and (not isinstance(value, str) or value.strip() == "")))
                    or (key != "complemento" and not isinstance(value, str))
                    or (isinstance(value, str) and value.strip() == "")):
                    return print(f"Campo '{key}' inválido.")
        return EnderecoRepository.criar_endereco(data)
    @staticmethod
    def atualizar_endereco(data:dict):
        endereco = EnderecoRepository.consultar_endereco(data.get("id"))
        if not endereco:
            return print("Endereço não encontrado.")
        dict_endereco = endereco.to_dict()
        endereco_atualizado = {"id": data.get("id")}
        del data["id"]
        if data.get("contato_id"): del data["contato_id"]
        for key, value in data.items():
            if dict_endereco[key] != value:
                if ((key == "complemento"
                    and (value is None or (isinstance(value, str) and value.strip() != "")))
                    or (isinstance(value, str) and value.strip() != "")):
                    endereco_atualizado.update({key: value})
                else:
                    return print(f"Campo '{key}' inválido.")
        if len(endereco_atualizado) > 1:
            return EnderecoRepository.atualizar_endereco(endereco_atualizado)
    @staticmethod
    def remover_endereco(id:int):
        endereco = EnderecoRepository.consultar_endereco(id)
        if not endereco:
            return print("Endereço não encontrado.")
        return EnderecoRepository.remover_endereco(id)