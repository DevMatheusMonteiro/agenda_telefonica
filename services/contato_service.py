from repositories.contato_repository import ContatoRepository, Contato, Endereco, Telefone, Email, EmailRepository
class ContatoService:
    @staticmethod
    def consultar_contatos():
        contatos = ContatoRepository.consultar_contatos()
        if not contatos:
            return "Nenhum contato encontrado"
        return [contato.to_dict() for contato in contatos]
    @staticmethod
    def consultar_contato(id:int):
        contato = ContatoRepository.consultar_contato(id)
        if not contato:
            return f"Contato com o id {id} não encontrado"
        return contato.to_dict()
    @staticmethod
    def criar_contato(data: dict):
        nome = data.get("nome")
        data_nascimento = data.get("data_nascimento")
        endereco = data.get("endereco")
        emails = data.get("emails")
        telefones = data.get("telefones")
        if not nome or nome.strip() == "":
            return "Nome é obrigatório."
        if not data_nascimento or (isinstance(data_nascimento, str) and data_nascimento.strip() == ""):
            return "Data de nascimento é obrigatória."
        if endereco:
            if any(not value or value.strip() == "" for key, value in endereco.items() if key not in ["complemento", "id", "contato_id"]):
                return "Campos de endereço inválidos."
        if emails:
            for email in emails:
                if not email.get("email") or email.get("email").strip() == "":
                    return "Email é obrigatório."
        if telefones:
            for telefone in telefones:
                if not telefone.get("telefone") or telefone.get("telefone").strip() == "":
                    return "Telefone é obrigatório"
        return ContatoRepository.criar_contato(data)
    @staticmethod
    def atualizar_contato(data:dict):
        contato = ContatoRepository.consultar_contato(data.get("id"))
        if not contato:
            return print(f"Contato com o id {data.get("id")} não encontrado")
        nome = data.get("nome")
        data_nascimento = data.get("data_nascimento")
        if nome and contato.nome != nome:
            if nome.strip() == "":
                return "Campo nome inválido."
            contato.nome = nome
        if data_nascimento and contato.data_nascimento != data_nascimento:
            if isinstance(data_nascimento, str) and data_nascimento.strip() == "":
                return "Campo data de nascimento inválido."
            contato.data_nascimento = data_nascimento