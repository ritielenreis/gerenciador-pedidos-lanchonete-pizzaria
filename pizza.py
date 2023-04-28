from prato import Prato


class Pizza(Prato):
    def __init__(self, id_prato: int, nome: str, preco: float, validade: str, peso: int, recheio: str,
                 borda: str, molho: str):
        super().__init__(id_prato, nome, preco, validade, peso)
        self._recheio = recheio
        self._borda = borda
        self._molho = molho

    @property
    def recheio(self):
        return self._recheio

    @recheio.setter
    def recheio(self, novo_recheio):
        self._recheio = novo_recheio

    @property
    def borda(self):
        return self._borda

    @borda.setter
    def borda(self, nova_borda):
        self._borda = nova_borda

    @property
    def molho(self):
        return self._molho

    @molho.setter
    def molho(self, novo_molho):
        self._molho = novo_molho
