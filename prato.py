class Prato:
    def __init__(self, id_prato: int, nome: str, preco: float, validade: str, peso: int):
        self._id_prato = id_prato
        self._nome = nome
        self._preco = preco
        self._validade = validade
        self._peso: int = peso

    def __str__(self):
        return f"{self._nome}:{self._preco}"

    @property
    def id_prato(self):
        return self._id_prato

    @id_prato.setter
    def id_prato(self, novo_id_prato):
        self._id_prato = novo_id_prato

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

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
