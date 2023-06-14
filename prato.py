class Prato:
    def __init__(self, id_prato: int, nome_prato: str, preco: float, validade: str, peso: int):
        self._id_prato = id_prato
        self._nome_prato = nome_prato
        self._preco = preco
        self._validade = validade
        self._peso: int = peso

    @property
    def id_prato(self):
        return self._id_prato

    @id_prato.setter
    def id_prato(self, novo_id_prato):
        self._id_prato = novo_id_prato

    @property
    def nome_prato(self):
        return self._nome_prato

    @nome_prato.setter
    def nome_prato(self, novo_nome_prato):
        self._nome_prato = novo_nome_prato

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    @property
    def validade(self):
        return self._validade

    @validade.setter
    def validade(self, nova_validade):
        self._validade = nova_validade

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, novo_peso):
        self._peso = novo_peso
