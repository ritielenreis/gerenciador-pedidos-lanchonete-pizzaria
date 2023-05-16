from cliente import Cliente
from item_pedido import ItemPedido
from typing import List, Optional
from preco_item_pedido import PrecoItemPedido

class Pedido:
    def __init__(self, id_cliente: Cliente.id_cliente,
                       id_pedido: Optional[int] = None,
                       itens_pedido: Optional[List[ItemPedido]] = None,
                       taxa_servico: Optional[float] = None,
                       status = 'pendente'):
        self._id_cliente: Cliente = id_cliente
        self._id_pedido: int = id_pedido
        self._taxa_servico: float = taxa_servico
        self._itens_pedido: List[ItemPedido] = itens_pedido
        self._status = status

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, novo_id_cliente):
        self._id_cliente = novo_id_cliente
        
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
    def itens_pedido(self):
        return self._itens_pedido

    @itens_pedido.setter
    def itens_pedido(self, alterar_itens_pedido):
        self._itens_pedido = alterar_itens_pedido

    @property
    def taxa_servico(self):
        return self._taxa_servico

    @taxa_servico.setter
    def taxa_servico(self, alterar_taxa: int):
        self._taxa_servico = alterar_taxa

    def __str__(self):
        return f'Pedido numero {self._id_pedido}'

    @staticmethod
    def calcular_preco_pedido(taxa_servico: float, precosPedido: list[PrecoItemPedido] ) -> float:
        montante = taxa_servico
        for precoPedido in precosPedido:
            montante += precoPedido.calcular_preco()
        return montante

'''
    def __str__(self):
       return f' Cliente {self._nome_cliente} fez pedido de {self._itens_pedido} ' \
               f'e a taxa de serviço é {self._taxa_servico}.' \
               f'total: {self.total()}'

    def __troco_para(self, valor_pago: float):
        self.valor_pago = valor_pago
        troco: float = valor_pago - self.total()
        return f'Valor recebido: {self.valor_pago}\n' \
               f'Troco: R${troco}'

    def fatura(self, valor_pago: float):
        print('=' * 10, 'Fatura', '=' * 10)
        print(f'Cliente: {self.nome_cliente}')
        print(f'Pedido:')
        for prato in self._itens_pedido:
            print(f'1  {prato.nome_prato} \t {prato.preco}')
        print(f'Taxa de Serviço: \t{self._taxa_servico}\n')
        print(f'\nValor total: \t{self.total()}')
        print(f'{self.__troco_para(valor_pago)}\n\n')
'''