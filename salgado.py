from prato import Prato


class Salgado(Prato):
    def __init__(self, id_prato, nome: str, preco: float, validade: str, peso: int, massa: str, recheio: list):
        super().__init__(id_prato, nome, preco, validade, peso)
        self._massa = massa
        self._recheio = recheio

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
