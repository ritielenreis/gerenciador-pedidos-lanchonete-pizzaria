class PedidoInfo:
    def __init__(self, id_cliente, nome_cliente, id_pedido: int = None, status='pendente'):
        self._id_cliente: int = id_cliente
        self._nome_cliente: int = nome_cliente
        self._id_pedido: int = id_pedido
        self._status = status

    @property
    def id_pedido(self):
        return self._id_pedido

    @id_pedido.setter
    def id_pedido(self, alterar_id_pedido):
        self._id_pedido = alterar_id_pedido

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, alterar_id_cliente):
        self._id_cliente = alterar_id_cliente

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, novo_nome_cliente):
        self._nome_cliente = novo_nome_cliente

    def __str__(self):
        return f'{self._id_pedido},{self._id_cliente},{self._nome_cliente},{self._status}'
