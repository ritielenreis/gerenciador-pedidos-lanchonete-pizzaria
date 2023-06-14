from typing import Optional


class Pedido:
    def __init__(self, id_cliente, id_pedido: Optional[int] = None, status='pendente'):
        self._id_cliente: int = id_cliente
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

    def __str__(self):
        return f'Pedido número {self._id_pedido}'
