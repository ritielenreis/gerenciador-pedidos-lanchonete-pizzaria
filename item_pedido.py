class ItemPedido():
    def __init__(self, id_item, id_pedido, id_prato, quantidade):
        self._id_item = id_item
        self._id_pedido = id_pedido
        self._id_prato = id_prato
        self. _quantidade = quantidade

    @property
    def id_pedido(self):
        return self._id_pedido

    @id_pedido.setter
    def id_pedido(self, novo_id_pedido):
        self._id_pedido = novo_id_pedido

    @property
    def id_prato(self):
        return self._id_prato

    @id_prato.setter
    def id_prato(self, novo_id_prato):
        self._id_prato = novo_id_prato

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade

    def __str__(self):
        return f"{self._id_pedido}={self._id_prato}x{self.quantidade}"
