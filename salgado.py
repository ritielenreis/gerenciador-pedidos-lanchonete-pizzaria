from prato import Prato


class Salgado(Prato):
    def __init__(self, id_prato, nome_prato: str, preco: float, validade: str, peso: int, massa: str, recheio: list, tipo: str):
        super().__init__(id_prato, nome_prato, preco, validade, peso)
        self._massa = massa
        self._recheio = recheio
        self._tipo = tipo

    @property
    def massa(self):
        return self._massa

    @massa.setter
    def massa(self, nova_massa):
        self._massa = nova_massa

    @property
    def recheio(self):
        return self._recheio

    @recheio.setter
    def recheio(self, novo_recheio):
        self._recheio = novo_recheio

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo

    def __str__(self):
        return f'{self.id_prato}, {self.nome_prato}, {self.preco}, {self.massa},{self.recheio}, {self.tipo}, {self.preco}'
