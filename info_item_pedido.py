from prato import Prato


class InfoItemPedido(Prato):
    def __init__(self, id_pedido, id_item,  id_prato, nome_prato, quantidade,  preco, validade, peso):
        super().__init__(id_prato, nome_prato, preco, validade, peso)
        self._id_item = id_item
        self._id_pedido = id_pedido
        self. _quantidade = quantidade

    @property
    def id_item(self):
        return self._id_item

    @id_item.setter
    def id_item(self, novo_id_item):
        self._id_item = novo_id_item

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

    def __repr__(self):
        return f'\n{self.id_item}   {self.id_pedido}   {self.id_prato}   ' \
               f'{self.nome_prato}          {self.quantidade}     {self.preco}'
