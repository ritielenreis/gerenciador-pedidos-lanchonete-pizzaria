class Adm:
    def __init__(self, id_adm: int, nome_adm: str, senha):
        self._id_adm = id_adm
        self._nome_adm = nome_adm
        self._senha = senha

    def __str__(self):
        return f"{self.id_adm}. {self.nome_adm} {self._senha}"

    @property
    def id_adm(self):
        return self._id_adm

    @id_adm.setter
    def id_adm(self, novo_id_adm):
        self._id_adm = novo_id_adm

    @property
    def nome_adm(self):
        return self._nome_adm

    @nome_adm.setter
    def nome_adm(self, novo_nome_adm):
        self._nome_adm = novo_nome_adm

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha
