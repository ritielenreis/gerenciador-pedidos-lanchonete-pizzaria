from prato import Prato


class Lanche(Prato):
    def __init__(self, id_prato, nome, preco, validade, peso, pao, recheio, molho):
        super().__init__(id_prato, nome, preco, validade, peso)
        self._pao = pao
        self._recheio = recheio
        self._molho = molho

    @property
    def pao(self):
        return self._pao

    @pao.setter
    def pao(self, novo_pao):
        self._pao = novo_pao

    @property
    def recheio(self):
        return self._recheio

    @recheio.setter
    def recheio(self, novo_recheio):
        self._recheio = novo_recheio

    @property
    def molho(self):
        return self._molho

    @molho.setter
    def molho(self, novo_molho):
        self._molho = novo_molho
