class Cliente:
    def __init__(self, id_cliente: int, nome_cliente: str, telefone, rua, cidade, cod_postal, historico_pedidos):
        self._id_cliente = id_cliente
        self._nome_cliente = nome_cliente
        self._telefone = telefone
        self._rua = rua
        self._cidade = cidade
        self._cod_postal = cod_postal
        self._historico_pedidos = historico_pedidos

    def __str__(self):
        return f"{self.id_cliente}. {self.nome_cliente} {self.telefone}"

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, novo_id_cliente):
        self._id_cliente = novo_id_cliente

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, novo_nome_cliente):
        self._nome_cliente = novo_nome_cliente

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, novo_rua):
        self._rua = novo_rua

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, nova_cidade):
        self._cidade = nova_cidade

    @property
    def cod_postal(self):
        return self._cod_postal

    @cod_postal.setter
    def cod_postal(self, value):
        self._cod_postal = value

    @property
    def historico_pedidos(self):
        return self._historico_pedidos

    @historico_pedidos.setter
    def historico_pedidos(self, value):
        self._historico_pedidos = value


