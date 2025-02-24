from repositories.endereco_repository import EnderecoRepository
class EnderecoService:
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
                if (key == "complemento"
                    and (value is None or (isinstance(value, str) and value.strip() != ""))):
                    endereco_atualizado.update({key: value})
                elif (isinstance(value, str) and value.strip() != ""):
                    endereco_atualizado.update({key: value})
                else:
                    return print(f"Campo '{key}' inválido.")
        if len(endereco_atualizado) > 1:
            print("Tamanho", len(endereco_atualizado))
            EnderecoRepository.atualizar_endereco(endereco_atualizado)